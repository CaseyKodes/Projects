// Given two arrays of integers, return true (and also store the smallest integer that is in both arrays). Return false if no such integer exists 
// For example, suppose A1={1, 5, 3, 1} and A2={3, 7, 2}. Then ECCommonNumber(A1, 4, A2, 3, val) would return true (and val would be 3 after function call returns). Here, A1 is the first array, 4 is the size of the first array, A2 is the second array and 3 is the size of the second array. 
// Note: you must implement your algorithm as efficiently as possible
// Also, you need to define the function yourself: how are you going to take
// Tip: don't reinvent the wheel; try to use C++ standard library functions

#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;


bool ECCommonNumber(const int nums1[], int size1, const int nums2[], int size2, int &val)
{
  // // printing for testing
  // for (int i=0; i<size1; i++)
  // {
  //   cout << nums1[i] << " ";
  // }
  // cout << endl;
  // for (int i=0; i<size2; i++)
  // {
  //   cout << nums2[i] << " ";
  // }

  //edge case we get an empty array
  if(size1 == 0 || size2 == 0)
  {
    return false;
  }

  // sort the input array then use binary search to find the smallest shared value


  vector <int> hold1;
  vector <int> hold2;
  copy(nums1, nums1+size1, back_inserter(hold1));
  copy(nums2, nums2+size2, back_inserter(hold2));

  sort(hold1.begin(), hold1.end());
  sort(hold2.begin(), hold2.end());

  // now we want to call binary search between the arrays
  for (auto x : hold1)
  {
    // call binary search for x in hold2
    if (binary_search(hold2.begin(), hold2.end(), x))
    {
      // this will not be seen outside of the function call
      // how do i make it so it is seen outside of the function call
      val = x; 
      return true;
    }
  }
  return false;
}


