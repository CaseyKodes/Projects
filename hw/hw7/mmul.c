#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include "matrix.h"

// Search TODO to find the locations where code needs to be completed

#define     NUM_THREADS     2

typedef struct {
    unsigned int id;
    TMatrix *m, *n, *t;
} thread_arg_t;

static void * thread_main(void * p_arg)
{
    // TODO
    thread_arg_t *toUse;
    toUse = (thread_arg_t *) p_arg;
    
    if (toUse -> id == 0)
    {
        for (unsigned int i = 0; i < (toUse->m->nrows)/2; i++)  
        {
            for (unsigned int j = 0; j < toUse->n->ncols; j++) 
            {
                TElement sum = (TElement)0;
                for (unsigned int k = 0; k < toUse->m->ncols; k++)
                    sum += toUse->m->data[i][k] * toUse->n->data[k][j];
                toUse->t->data[i][j] = sum;
            }
        }
    }
    else if (toUse -> id == 1)
    {
        for (unsigned int i = (toUse->m->nrows)/2; i < (toUse->m->nrows); i++)  
        {
            for (unsigned int j = 0; j < toUse->n->ncols; j++) 
            {
                TElement sum = (TElement)0;
                for (unsigned int k = 0; k < toUse->m->ncols; k++)
                    sum += toUse->m->data[i][k] * toUse->n->data[k][j];
                toUse->t->data[i][j] = sum;
            }
        }
    }
    return NULL;
}

/* Return the sum of two matrices.
 *
 * If any pthread function fails, report error and exit. 
 * Return NULL if anything else is wrong.
 *
 * Similar to mulMatrix, but with multi-threading.
 */
TMatrix * mulMatrix_thread(TMatrix *m, TMatrix *n)
{
    if (m == NULL || n == NULL || m->ncols != n->nrows )
        return NULL;

    TMatrix * t = newMatrix(m->nrows, n->ncols);
    if (t == NULL)
        return t;

    // TODO
    
    // create thread IDs 
    pthread_t idA;
    pthread_t idB;

    // need to put the two matries into a single argument to pass
    thread_arg_t arr[NUM_THREADS];
    for (int i = 0; i < NUM_THREADS; i++)
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