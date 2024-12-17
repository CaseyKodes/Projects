#include <iostream>
using namespace std;

#include "ECCommonNumber.cpp"

template<class T>
void ASSERT_EQ(T x, T y)
{
  if( x == y )
  {
    cout << "Test passed: equal: " << x << "  " << y << endl;
  }
  else
  {
    cout << "Test FAILED: equal: " << x << "  " << y << endl;
  }
}

int main()
{
  int arr1[] = {1, 3, 5, 1};
  int arr2[] = {3, 7, 2, 1};
  int valCommon;
  bool f1 = ECCommonNumber(arr1, 4, arr2, 4, valCommon);
  ASSERT_EQ(f1, true);
  ASSERT_EQ(valCommon, 1);
  int arr3[] = {7, 2, 100, -3, 0};
  int valCommon2;
  bool f2 = ECCommonNumber(arr1, 4, arr3, 5, valCommon2);
  ASSERT_EQ(f2, false);
}

