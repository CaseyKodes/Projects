// This function returns the smallest non-negative integral root of a polynomial (as specified by a list of coefficients and degree) 
//  that is no larger than xmax. Return -1 if there is no roots within the range.
// To be specific: for each integer 0 <=i <= degree, listCoeffs[d] = the coefficient of the degree d term. For example, 
#include <math.h>

int ECFindRoot(int *listCoeffs, int degree, int xmax)
{
  // listCoeffs: pointer to the array of integers as the coefficients of a polynomial; listCoeffs[0] is the constant term and so on
  // degree: highest degree term. That is, the number of coefficients in the array = degree+1
  // xmax: the largest value of root to search

  int start = 0;
  int total;
  // in this loop we are testing to see if numbers 1 to xmax are a root of the function
  while (start <= xmax)
  {
    total = 0;
    // now in each iteration we need to create the function that is represented by the array
    for (int i = degree; i>=0; i--)
    {
      // in this loop we will be raiseing start to the power i and multiplying it by the coefficient in index i of the array
      total = total * start + listCoeffs[i];
    }
    if (total==0)
    {
      return start;
    }
    start++;
  }
  return -1; // did not find a root
}