#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <assert.h>
#include "linked-list.h"

#define MAX 10

typedef struct {
    node    *head, *tail;
    pthread_mutex_t mutex;
} list_t;

typedef struct {
	int size;
    int buf[MAX][3];
    int remain;
    int counts[3];            //current indexes
    pthread_mutex_t mutex;
    pthread_cond_t produce_cond;
    pthread_cond_t consume_cond;
}two_d_buffer;

/*
adds items to the end of the column in the 2d buffer labeled by col
block if col is full
when added successful should update remain variable associated with 2d buffer 
try to wake up remove_from_buffer
*/
void add_to_buffer(int item, int col, two_d_buffer *p)
{
	//TODO
	//fill in code below
	pthread_mutex_lock(&p->mutex);
	// now add the thing to the buffer
	// first need to check if that column is full
	while (p->counts[col] == p->size)
	{
		// now we need to wait until an item is removed from the buffer 
		pthread_cond_wait(&p->produce_cond, &p->mutex);
	}
	// now the col should not be full we just want to add an item to the column and we are done
	p->buf[p->counts[col]][col] = item;
	p->counts[col] += 1;
	p->remain -= 1;

	// trying to wake up remove_from_buffer
	pthread_cond_signal(&p -> consume_cond);
	// we are done editing the buffer now
	pthread_mutex_unlock(&p->mutex);
}

/*
tries to remove all three items a, b, c from the first row in 2d buffer
should block if not all three items are ready 
if all items removed move rest of items in 2d buffer up one row 
	# just need to change the head of the linked list
try to wake up add_to_buffer
*/
void remove_from_buffer(int *a, int *b, int *c, two_d_buffer *p)
{
	//TODO
	//fill in code below

	pthread_mutex_lock(&p->mutex);
	/* we now have access to the buffer 
		a b c need to become the items from col 0 1 2 for the buffer respectivly
		then we need to move the rest of the items in the buffer down a slot
	*/
	// need all three slots from the buffer we want to take from to have items in them
	while(p->counts[0]==0 || p->counts[1]==0 || p->counts[2]==0)
	{
		pthread_cond_wait(&p->consume_cond, &p->mutex);
	}
	// there should be an item in each row for us to take 
		// getting a warning here a little confused on how to fix
	*a = p->buf[0][0];
	*b = p->buf[0][1];
	*c = p->buf[0][2];
	for (int i=0; i<3; i++)
	{
		p->counts[i] -= 1;
	}
	// now we need to move things in the buffer
		// i think this might be the hard part but it is also the last thing TODO
	for (int i=0; i<p->size-1; i++)
	{
		for (int j=0; j<3; j++)
		{
			p->buf[i][j] = p->buf[i+1][j];
		}
	}
	for (int j=0; j<3; j++)
	{
		p->buf[j][MAX-1] = 0;
	}
	// trying to wake up add_to_buffer
	pthread_cond_signal(&p -> produce_cond);
	pthread_mutex_unlock(&p->mutex);
}

void prepare(int item)
{
	usleep((item + 1)*100);
}

struct thread_data
{
	int id;
    list_t *p; 						// linked list pointers to head and tail, with mutex
    two_d_buffer *q;
	int total;						// total items produced by a producer
	pthread_barrier_t *p_barrier;	// used to stop threads when items are not ready
};

void* thread_consume(void* threadarg)
{
    struct thread_data* my_data = (struct thread_data*) threadarg;
	int id = my_data->id;
	list_t *p = my_data->p;

	node *n1 = create_node(0);
	node *n2 = create_node(1);
	node *n3 = create_node(2);
	
	//TODO
	//fill in code below to add n1, n2, and n3 to the linked-list pointed by p
	/*
		n1, n2, and n3 are the drink fries and buger the consumer ordered
		these are added to the linked list so the producers know the make them
	*/
	pthread_mutex_lock(&p->mutex);
	add_last(&p->head, &p->tail, n1);
	add_last(&p->head, &p->tail, n2);
	add_last(&p->head, &p->tail, n3);
	pthread_mutex_unlock(&p->mutex);

	pthread_barrier_t *p_barrier = my_data->p_barrier;
	pthread_barrier_wait(p_barrier);

	two_d_buffer *q = my_data->q;
	int a, b, c;
	remove_from_buffer(&a, &b, &c, q);
	printf("consumer %04d (%d %d %d)\n", id, a, b, c);		
	pthread_exit(NULL);
}

/*
order of operations
	first get item from linked list
		this will involve calling the mutex on the linked list pulling an item out then changing the head/tail of the list
	second make the item 
		use the prepare function to simulate the code is taking time to do something
	third we add the item to the buffer
		to add an item the column the item should go to should not be full, if it is we need to wait for an item to be removed
	finally update the number of things that need to be and have been created 
*/
void* thread_produce(void* threadarg)
{   
	struct thread_data* my_data = (struct thread_data*) threadarg;
    list_t *p = my_data->p;
    pthread_barrier_t *p_barrier = my_data->p_barrier;
    pthread_barrier_wait(p_barrier);
	two_d_buffer *q = my_data->q;

	while(p->head != NULL)
	{
		//TODO
		//fill in code below
		node *toMake;

		// getting item from linked list and making it
		pthread_mutex_lock(&p->mutex);
		toMake = remove_first(&p->head, &p->tail);
		pthread_mutex_unlock(&p->mutex);
		prepare(toMake->v);
		my_data->total+=1;
		
		//put item into the buffer
		add_to_buffer(toMake->v, toMake->v, q);

		// need to free the memory we allocated for the node
		free(toMake);
	}

    pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
	if(argc < 4) {
		printf("Usage: %s n_consumer n_producer buffer_size\n", argv[0]);
		return -1;
	}
	int n_consumer = atoi(argv[1]);
	assert(n_consumer <= 3000);
	int n_producer = atoi(argv[2]);
	assert(n_producer <= 3000);
	int size = atoi(argv[3]);
	assert(size <= MAX);
	//initilize the list
	list_t *p = (list_t *)malloc(sizeof(list_t));
	
	if(p==NULL)
	{
		perror("Cannot allocate memeory.\n");
		return -1;
	}
	p->head = NULL;
	p->tail = NULL;
	pthread_mutex_init(&p->mutex, NULL);
	
	//initilize the 2d buffer
	two_d_buffer *q = malloc(sizeof(two_d_buffer));
    q->size = size;
    q->remain = 3*n_consumer;
    q->counts[0] = 0; q->counts[1] = 0; q->counts[2] = 0;
	pthread_mutex_init(&q->mutex, NULL);
    pthread_cond_init (&q->produce_cond, NULL);
    pthread_cond_init (&q->consume_cond, NULL);

	pthread_barrier_t barrier;
	pthread_barrier_init(&barrier, NULL, n_consumer + n_producer); 
    pthread_t threads[n_consumer + n_producer];
    struct thread_data thread_data_array[n_consumer + n_producer];
    int rc, t;

	for(t=0; t<n_consumer; t++ ) {
        thread_data_array[t].id = t;
		thread_data_array[t].p = p;
		thread_data_array[t].q = q;
		thread_data_array[t].total = 0;
		thread_data_array[t].p_barrier = &barrier;

		//TODO
		//complete the following line of code
			// should be done just added what thread function to call
		rc = pthread_create(&threads[t], NULL, thread_consume , &thread_data_array[t]);
        	if (rc) 
			{
            	printf("ERROR; return code from pthread_create() is %d\n", rc);
            	exit(-1);
        	}
    	}

        for(t=0; t<n_producer; t++ ) 
		{
            thread_data_array[n_consumer + t].id = t;
            thread_data_array[n_consumer + t].p = p;
            thread_data_array[n_consumer + t].q = q;
			thread_data_array[n_consumer + t].total = 0;
			thread_data_array[n_consumer + t].p_barrier = &barrier;

			//TODO
			//complete the follow line of code
				// should be done just added what thread function to call
            rc = pthread_create(&threads[n_consumer + t], NULL, thread_produce, &thread_data_array[n_consumer + t]);
            if (rc) 
			{
                printf("ERROR; return code from pthread_create() is %d\n", rc);
                exit(-1);
            }
        }

    	for(t=0; t<n_consumer + n_producer; t++ ) 
    	{
        	rc = pthread_join( threads[t], NULL );
        	if(rc)
			{
            	printf("ERROR; return code from pthread_join() is %d\n", rc);
            	exit(-1);
        	}
    	}

	int total = 0;

	//TODO
	//fill in code below
	/*
		is this just to update the total variable
	*/
	for(int i=0; i < n_producer + n_consumer; i++) {
		total += thread_data_array[i].total; 
	}
	
	printf("total = %d\n", total);
 
    pthread_mutex_destroy(&p->mutex);
    free(p);

	pthread_mutex_destroy(&q->mutex);
	pthread_cond_destroy(&q->consume_cond);
	pthread_cond_destroy(&q->produce_cond);
	free(q);

	pthread_barrier_destroy(&barrier);	
    return 0;
}