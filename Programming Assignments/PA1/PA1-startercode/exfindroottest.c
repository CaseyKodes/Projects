// Test code for ECFindRoot
// To build: c++ ECFindRootTest.cpp -o test
// To test: ./test

#include <stdio.h>
#include <string.h>
#include "ECFindRoot.cpp"

int main()
{
  int test1[] = {4, -4, 1};
  // root = 2 for 4-4x+x^2=0
  printf("%d", ECFindRoot(test1, 2, 10));
  // should return -1 (no root)
  int test2[] = {1, -3, 1};
  printf("\n%d", ECFindRoot(test2, 2, 10));
  // should return -1
  printf("\n%d", ECFindRoot(test2, 0, 10));
  int test4[] = {-9576, 3126, 565, -151, -13, 1};
  // should return 3
  printf("\n%d", ECFindRoot(test4, 5, 10));
}

