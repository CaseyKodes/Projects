#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

//TODO
//Implement the below function
//Simulate one particle moving n steps in random directions
//Use a random number generator to decide which way to go at every step
//When the particle stops at a final location, use the memory pointed to by grid to 
//record the number of particles that stop at this final location
//Feel free to declare, implement and use other functions when needed
void one_particle(int *grid, int n)
{
	int x=0,y=0,z=0, r;
	for (int i =0; i<n; i++)
	{
		r = rand()%6;
		switch (r)
		{
			case(0)://left x-
			{
				x-=1;
				break;
			}
			case(1)://right x+
			{
				x+=1;
				break;

			}
			case(2)://up y
			{
				y+=1;
				break;
			}
			case(3)://down y 
			{
				y-=1;
				break;
			}
			case(4)://up z
			{
				z+=1;
				break;
			}
			case(5)://down z
			{
				z-=1;
				break;
			}
		}
	}
	// now we need to add 1 to the final point the partical is at within the grid
	int distance = (x*x+y*y+z*z); // this values is really distance^2
	grid[distance] += 1;
}

//TODO
//Implement the following function
//This function returns the fraction of particles that lie within the distance
//r*n from the origin (including particles exactly r*n away)
//The distance used here is Euclidean distance
//Note: you will not have access to math.h when submitting on Mimir
double density(int *grid, int n, double r)
{
	// to get around not having math.h instea of comparing n=sqrt(x^2+y^2+x^2) 
	// compart n^2=x^2+y^2+x^2 this is taken care of in the function one_partical
	int partial =0, full=0;
	for (int i=0; i<n*n; i++)
	{
		if(i<=(r*n)*(r*n))// since (r*n)^2 can be less than n^2 we need to make sure we stay in the bounds
		{
			partial += grid[i];
		}
		full += grid[i]; // this will get all the grid spots while the call in the if statment wont
	}
	double fraction = (double)partial/full;
	return fraction;    
}

//use this function to print results
void print_result(int *grid, int n)
{
    printf("radius density\n");
    for(int k = 1; k <= 20; k++)
    {
        printf("%.2lf   %lf\n", 0.05*k, density(grid, n, 0.05*k));
    }
}

//TODO
//Finish the following function
//See the assignment decription on Piazza for more details
void diffusion(int n, int m)
{
	//fill in a few line of code below
	// allocate the memory needed to store all the possible positions 
	int *grid = (int*) malloc(n*n*sizeof(int)); // needs to be 3 dimensional 

	for(int i = 1; i<=m; i++) one_particle(grid, n);

	print_result(grid, n);
	//fill in some code below
	//now we need to free the memory we malloced to 
	free(grid);

}

int main(int argc, char *argv[])
{
	
	if(argc != 3)
	{
		printf("Usage: %s n m\n", argv[0]);
		return 0; 
	}
	int n = atoi(argv[1]);
	int m = atoi(argv[2]);

	assert(n >= 1 && n <=50);
	assert(m >= 1 && m <= 1000000);
	srand(12345);
	diffusion(n, m);
	return 0;
}