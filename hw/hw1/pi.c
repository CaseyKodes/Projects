#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n, i;

	printf("n = ");
	scanf("%d", &n);

	double pi = 0.;
	//TODO
	//add code below 
	
    /*
    approximation for pi for this lab is the sum from i = 0 to n of 
    (4/(8i+1)-2/(8i+4)-1/(8i+5)-1/(8i+6))*1/(16^i)
    not aloowed to use power function 
    */
   
   double pi1, pi2;
   int j;
   double part1, part2, part3, part4;

   for (i=0; i<=n; i++)
   {
        pi1=0., pi2=1.0;
        pi1 = 4/((8.*i)+1)-2/((8.*i)+4)-1/((8.*i)+5)-1/((8.*i)+6);

        j=0;
        while (j < i)
        {
            pi2 = pi2*(1/16.);
            ++j;
        }
        pi = pi+(pi1*pi2);
    }

	printf("PI = %.10f\n", pi);
	return 0;
}