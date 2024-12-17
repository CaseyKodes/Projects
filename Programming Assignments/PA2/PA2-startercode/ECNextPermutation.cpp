#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

void helper(int *listNumbers, int sz)
{
  int i;
  for (i = 0; i <sz; i++)
  {
    cout << listNumbers[i] << " ";
  }
  cout << endl;
}

// You are given a list of integers listNumbers and its size
// These numbers are the permutaiton of the first sz integers, starting from 1
// After the function returns, listNumbers would contain the next permutation
// For example, if the list is 1 3 4 2  ==> 1 4 2 3
// Note: you don't need to check whether the given input is indeed a permutation
// That is, listNumbers always contains a valid permutation
void ECNextPermutation(int *listNumbers, int sz)
{
  int i, hold;
  /*
  cout << "Given - ";
  helper(listNumbers, sz);
  */

  /*
  the last time that the list elements continuted to go up 
  ex. [2,1,4,3] would be index 1 since index 2 is greater than index 1 and after index 2 the numbers go dwown
  we increase index 2 to the next highest useable value
  a useable value is a value <sz that was not already used in the array 
  since 2 was used already the next useable value is 3
  then for the values at indecies after 1 we should have them valued in increasing order 
  to have a next permutation of [2,3,1,4]
  */

  int lastUp = sz;
  int inOrder = 1;
  for (i = 0; i<sz-1; i++)
  {
    if (listNumbers[i] < listNumbers[i+1])
    {
      lastUp = i;
    }
    else
    {
      inOrder = 0;
    }
  }
  if (inOrder) // edge case if the list is in order we just need to swap the last two values
  {
    hold = listNumbers[sz-1];
    listNumbers[sz-1] = listNumbers[sz-2];
    listNumbers[sz-2] = hold;
    return;
  }  

  // doing this in a differnet loop to make the first loop even faster
  int useable[sz];
  for (i=0;i<sz;i++) 
  {
    useable[i] = listNumbers[i];
  }
  /*
  cout << "Useable before sort: ";
  helper(useable, sz); 
  */

  sort(useable, useable+sz);

  /*
  cout << "Useable afte sort: ";
  helper(useable, sz);

  */
    
  // edge case if the list is in reverse order
  if (lastUp == sz)
  {
    for (i= 0; i<sz/2; i++)
    {
      hold = listNumbers[i];
      listNumbers[i] = listNumbers[sz-i-1];
      listNumbers[sz-i-1] = hold;
    }
    //cout << "Final - ";
    //helper(listNumbers, sz);
    return;
  }

  // most cases should end up here
  int value;
  int toIncrease = listNumbers[lastUp];

  // we need to see what the lowest useable number is to decide where we need to delete values from in useable
  if (useable[0] == 0)
  {
    for (i = 0; i<lastUp; i++)
    {
      value = listNumbers[i];
      useable[value] = -1;
    } 
  }
  else if (useable[0] == 1)
  {
    for (i = 0; i<lastUp; i++)
    {
      value = listNumbers[i];
      useable[value-1] = -1;
    } 
  }
  
  for (i = 0; i<sz; i++)
  {
    if(useable[i] > toIncrease)
    {
      listNumbers[lastUp] = useable[i];
      useable[i] = -1;
      break;
    }
  }
  int counter = 1;

  // more printing for understanding
  /*
  cout << "Current - ";
  helper(listNumbers, sz);
  cout << "Useable - ";
  helper(useable, sz);
  */

  for (i=0; i<sz; i++)
  {
    if(useable[i] != -1)
    {
      listNumbers[lastUp+counter] = useable[i];
      useable[i]=-1;
      counter++;
    }
  }

  //cout << "Final - ";
  //helper(listNumbers, sz);
  return;
}
