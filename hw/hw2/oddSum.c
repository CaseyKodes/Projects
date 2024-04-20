#include <stdio.h>
#include <stdlib.h>

int oddSumHelp(int count, int bound, int value)
{
	//fill in your code below
	// count is the number of odd numbers to be used 
	// bound is the highest an odd number can be 
	// value is the value to be summed to 

	// Base case
	if(count == 0 && value==0) 
	{// solution found
		return 1; 
	}
	else if (value!=0 && count==0)
	{// no solution found 
		return 0; 
	}
	if(value < 0 || bound <= 0) 
	{
		return 0; // something wrong with the subtraction 
	}
	// actual recurssive part
    if(oddSumHelp(count-1, bound-2, value-bound)==1) 
    {
        printf("%d ", bound); 
        return 1;
    }
    else
    {
        return oddSumHelp(count, bound-2, value); // check the next odd number
    }
} 

//Do not change the code below
void oddSum(int count, int bound, int value)
{
    	if(value <= 0 || count <= 0 || bound <= 0) return;
    
    	if(bound % 2 == 0) bound -= 1;

    	if(!oddSumHelp(count, bound, value)) printf("No solutions.\n");
	else printf("\n");
}

int main(int argc, char *argv[])
{
	if(argc != 4) return -1;

	int count = atoi(argv[1]); // Number of nums
	int bound = atoi(argv[2]); // Range of nums
	int value = atoi(argv[3]); // Sum of nums

	//oddSum(12,30,200);
	//oddSum(10,20,100);
	//oddSum(20,20,200);
	oddSum(count, bound, value);
	return 0;
}