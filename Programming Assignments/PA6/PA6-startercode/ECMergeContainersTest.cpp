// Test merge containers. To compile: c++ ECMergeContainersTest.cpp -o test
#include "ECMergeContainers.cpp"
#include <vector>
#include <set>
#include <iostream>
using namespace std;

template<class T>
void ASSERT_EQ(T x, T y)
{
  if( x == y )
  {
    cout << "Test passed!\n";
  }
  else
  {
    cout << "Test FAILED: equal: Returned- " << x << "  Expected- " << y << endl;
  }
}

void Test1( )
{
  vector<vector<int> > listListNums;
  vector<int> lis1;
  lis1.push_back(1);
  lis1.push_back(3);
  lis1.push_back(2);
  vector<int> lis2;
  lis2.push_back(3);
  lis2.push_back(1);
  listListNums.push_back(lis1);
  listListNums.push_back(lis2);
  vector<int> lisOut;
  ECMergeContainers(listListNums, lisOut);
  ASSERT_EQ((int)lisOut.size(), 5);
  ASSERT_EQ(lisOut[0], 1);
  ASSERT_EQ(lisOut[1], 1);
  ASSERT_EQ(lisOut[2], 2);
  ASSERT_EQ(lisOut[3], 3);
  ASSERT_EQ(lisOut[4], 3);
}

void Test2()
{
  set<set<int> > listListNums;
  set<int> lis1;
  lis1.insert(1);
  lis1.insert(3);
  lis1.insert(2);
  set<int> lis2;
  lis2.insert(3);
  lis2.insert(1);
  listListNums.insert(lis1);
  listListNums.insert(lis2);
  vector<int> lisOut;
  ECMergeContainers(listListNums, lisOut);
  ASSERT_EQ((int)lisOut.size(), 5);
  ASSERT_EQ(lisOut[0], 1);
  ASSERT_EQ(lisOut[1], 1);
  ASSERT_EQ(lisOut[2], 2);
  ASSERT_EQ(lisOut[3], 3);
  ASSERT_EQ(lisOut[4], 3);
}
int main()
{
  Test1();
  Test2();
}
