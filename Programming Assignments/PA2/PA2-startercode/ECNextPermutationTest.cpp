#include <iostream>
using namespace std;

// test code
// Build: g++ ECNextPermutation.cpp ECNextPermutationTest.cpp -o test
extern void ECNextPermutation(int *listNums, int sz);

// for testing: it uses template
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

// test code
static void Test1()
{
  cout << "test 1\n";
  // 
  const int SZ = 4;
  int listInts[SZ] = {1, 2, 3, 4};
  ECNextPermutation(listInts, SZ);
  // chec the output
  ASSERT_EQ( listInts[0], 1);
  ASSERT_EQ( listInts[1], 2);
  ASSERT_EQ( listInts[2], 4);
  ASSERT_EQ( listInts[3], 3);
}

static void Test2()
{
  cout << "test 2\n";
  //
  const int SZ = 4;
  int listInts[SZ] = {2,1,4,3};
  ECNextPermutation(listInts, SZ);
  // chec the output
  ASSERT_EQ( listInts[0], 2);
  ASSERT_EQ( listInts[1], 3);
  ASSERT_EQ( listInts[2], 1);
  ASSERT_EQ( listInts[3], 4);
}

static void Test3()
{
  cout << "test 3\n";
  //
  const int SZ = 5;
  int listInts[SZ] = {1, 3, 5, 4, 2};
  ECNextPermutation(listInts, SZ);
  // chec the output: should be 1 4 2 3 5
  ASSERT_EQ( listInts[0], 1);
  ASSERT_EQ( listInts[1], 4);
  ASSERT_EQ( listInts[2], 2);
  ASSERT_EQ( listInts[3], 3);
  ASSERT_EQ( listInts[4], 5);
}

static void Test4()
{
  cout << "test 4\n";
  //
  const int SZ = 5;
  int listInts[SZ] = {0,4,3,1,2};

  ECNextPermutation(listInts, SZ);
  // chec the output: should be 1 2 3 4
  ASSERT_EQ( listInts[0], 0);
  ASSERT_EQ( listInts[1], 4);
  ASSERT_EQ( listInts[2], 3);
  ASSERT_EQ( listInts[3], 2);
  ASSERT_EQ( listInts[4], 1);
}

int main()
{
  Test1();
  cout << endl;
  Test2();
  cout << endl;
  Test3();
  cout << endl;
  Test4();
}


