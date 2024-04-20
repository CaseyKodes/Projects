#include <stdio.h>    
     
//isHappyNumber() will determine whether a number is happy or not    
int isHappyNumber(int num){    
    int rem = 0, sum = 0;    
        
    //Calculates the sum of squares of digits    
    while(num > 0){    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num/10;    
    }    
    return sum;    
}    
        
int main()    
{    
    int n;   
	printf("n = ");
	scanf("%d",&n); 
    int result = n;    
        
    while(result != 1 && result != 4){    
        result = isHappyNumber(result);   
		printf("%d\n", result);
    }    
    //Happy number always ends with 1   
	if(result == 1)    
        printf("%d is a happy number.", n);    
    //Unhappy number ends in a cycle of repeating numbers which contains 4    
    else if(result == 4)    
        printf("%d is NOT a happy number.", n); 
	return 0;    
}    