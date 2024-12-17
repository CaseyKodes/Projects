// Test code for ECRuns.cpp
#include <string>
#include <iostream>
using namespace std;

#include "ECRuns.cpp"

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

// to build: c++ ParenthesesCheck.cpp ParenthesesCheckTest.cpp -o test
extern int ECRuns(const string &str, int *pList);

static void Test1()
{
  // 1 3 3 7 7 7 2 2 1 1
  string str1 = "1337772211";
  int arr[100];
  int nr1 = ECRuns(str1, arr);
  ASSERT_EQ(nr1, 5);
  ASSERT_EQ(arr[0], 0);
  ASSERT_EQ(arr[1], 1);
  ASSERT_EQ(arr[2], 3);
  ASSERT_EQ(arr[3], 6);
  ASSERT_EQ(arr[4], 8);
}

int main()
{
  Test1();
}

