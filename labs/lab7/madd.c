#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include "matrix.h"

#define     NUM_THREADS     2

typedef struct {
    unsigned int id;
    TMatrix *m, *n, *t;
} thread_arg_t;

/* the main function of threads */
static void * thread_main(void * p_arg)
{
    // TODO
    thread_arg_t *toUse;
    toUse = (thread_arg_t *) p_arg;
    
    int n = toUse -> m -> nrows;

    if (toUse -> id == 0)
    {
        // add top half
        for (int i = 0; i < n/2; i ++)
        {
            for (int j = 0; j <toUse-> m->ncols; j++)
            {
                toUse->t->data[i][j] = toUse->m->data[i][j] + toUse->n->data[i][j];
            }
        }
    }
    else
    {
        // add bottom half
        for (int i = n/2; i < toUse->m->nrows; i++)
        {
            for (int j = 0; j < toUse->m->ncols; j++)
            {
                toUse->t->data[i][j] = toUse->m->data[i][j] + toUse->n->data[i][j];
            }
        }
    }

    return NULL;
}

/* Return the sum of two matrices. The result is in a newly created matrix. 
 *
 * If a pthread function fails, report error and exit. 
 * Return NULL if something else is wrong.
 *
 * Similar to addMatrix, but this function uses 2 threads.
 */
TMatrix * addMatrix_thread(TMatrix *m, TMatrix *n)
{
    if (    m == NULL || n == NULL
         || m->nrows != n->nrows || m->ncols != n->ncols )
        return NULL;

    TMatrix * t = newMatrix(m->nrows, m->ncols);
    if (t == NULL)
    {
        return t;
    }

    // TODO

    // create thread IDs 
    pthread_t idA;
    pthread_t idB;

    // need to put the two matries into a single argument to pass
    int number_of_threads = 2;
    thread_arg_t arr[number_of_threads];
    for (int i = 0; i <number_of_threads; i++)
    {
        arr[i].id = i;
        arr[i].m = m;
        arr[i].n = n;
        arr[i].t = t;
    }

    void * topass0 = &arr[0];
    void * topass1 = &arr[1];

    // start multie threading
    pthread_create(&idA, NULL, (void*)thread_main, topass0);
    pthread_create(&idB, NULL, (void*)thread_main, topass1);

    // join threads
    pthread_join(idA, NULL);
    pthread_join(idB, NULL);

    return t;
}