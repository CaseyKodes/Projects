#include <stdio.h>

int main (void)
{
    int counter = 1;
    double average, x, total=0.0;

    while (scanf("%lf", &x) == 1) 
    { // pay attention to %lf
        total += x;
        average = total/counter;
        printf("Total=%f Average=%f\n", total, average);
        counter++;
    }
}