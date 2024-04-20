#include <stdio.h>
#include <stdlib.h>

double two_d_random(int n)
{
	//Fill in code below
	//The random walk should stop once the x coordinate or y coordinate reaches $-n$ or $n$. 
	//The function should return the fraction of the visited $(x, y)$ coordinates inside (not including) the square.
	int visited=0; // counter to show how many points in n*n grid have been visited 
	int x=0, y=0; // x position and y position of walker
	int limitPart = 2*n-1;
	int Limit = limitPart*limitPart;


	// structure to hold the coordinate values 
	struct coordinate{
		int x;
		int y;
	};

	struct coordinate coords[Limit];

	while (x<n && x>-1*n && y<n && y>-1*n)
	{
		//When deciding which way to go for the next step, generate a random number as follows.
		//Treat r = 0, 1, 2, 3 as up, right, down and left respectively.
		int r = rand() % 4;

		int checker = 0;
		for (int i=0; i<visited; i++)
		{
			if (coords[i].x==x && coords[i].y==y)
			{
				checker =-1;
			}
		}
		if(checker==0 && visited<Limit)
		{
			coords[visited].x=x;
			coords[visited].y=y;
			visited+=1;
		}

		switch (r)
		{
			case 0:
			{// move up
				y+=1;
				break;
			}
			case 1:
			{// move right
				x+=1;
				break;
			}
			case 2:
			{// move down 
				y-=1;
				break;
			}
			case 3:
			{// move left
				x-=1;
				break;
			}
		}
	}
	double percent = (double) visited / Limit;
	return (percent);
}

//Do not change the code below
int main(int argc, char *argv[])
{
	int trials = 1000;
	int i, n, seed;
	if (argc == 2) seed = atoi(argv[1]);
	else seed = 12345;

	srand(seed);
	for(n=1; n<=64; n*=2)
	{	
		double sum = 0.;
		for(i=0; i < trials; i++)
		{
			double p = two_d_random(n);
			sum += p;
		}
		printf("%d %.3lf\n", n, sum/trials);
	}
	return 0;
}