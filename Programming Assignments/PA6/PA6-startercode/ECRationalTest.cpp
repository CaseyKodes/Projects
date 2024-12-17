// Note this test includes ECPolynomial code
// To build the code:
// g++ ECRationalTest.cpp ECPolynomial.cpp  -std=c++17
// You can comment out this part if you don't want to test ECPolynomial part
#include <iostream>
using namespace std;

#include "ECRational.h"
#include "ECPolynomial.h"

void Test1()
{
  cout << "******Test1:\n";
  // test rational of ints 
  ECRational<int> r1(1,2), r2(3,2);
  cout << "r1: " << r1.GetNumerator() << "/" << r1.GetDenominator() << endl;
  cout << "r2: " << r2.GetNumerator() << "/" << r2.GetDenominator() << endl;
  ECRational <int> r3 = r1+r2;
  cout << "r1+r2=" << r3.GetNumerator() << "/" << r3.GetDenominator() << endl;
  ECRational <int> r4 = r1-r2;
  cout << "r1-r2=" << r4.GetNumerator() << "/" << r4.GetDenominator() << endl;
  ECRational <int> r5 = r1*r2;
  cout << "r1*r2=" << r5.GetNumerator() << "/" << r5.GetDenominator() << endl;
  ECRational <int> r6 = r1/r2;
  cout << "r1/r2=" << r6.GetNumerator() << "/" << r6.GetDenominator() << endl;
}

void Test2()
{
  // more test rational of ints 
  cout << "******Test2:\n";
  ECRational<int> r1(2);
  cout << "r1=" << r1.GetNumerator() << "/" << r1.GetDenominator() << endl;
  ECRational<int> r2 = r1/3;
  cout << "r2 = r1/3 = " << r2.GetNumerator() << "/" << r2.GetDenominator() << endl;
  ECRational<int> r3 = 3/r1;
  cout << "3/r1 = " << r3.GetNumerator() << "/" << r3.GetDenominator() << endl;
  ECRational<int> r4 = r2 + 1;
  cout << "r2 + 1 = " << r4.GetNumerator() << "/" << r4.GetDenominator() << endl;
  ECRational<int> r5 = 1 + r2;
  cout << "1 + r2 = " << r5.GetNumerator() << "/" << r5.GetDenominator() << endl;
  ECRational<int> r6 = r2 * 5;
  cout << "r2 * 5 = " << r6.GetNumerator() << "/" << r6.GetDenominator() << endl;
  ECRational<int> r7 = 5 * r2;
  cout << "5 * r2 = " << r7.GetNumerator() << "/" << r7.GetDenominator() << endl;
}

void Test3()
{
    cout << "******Test3:\n";
  // test rational of polynomials
  ECPolynomial p1(2), p2(2), p3(1);
  // p1=1-x+x^2
  p1.SetCoeffAt(0, 1);
  p1.SetCoeffAt(1, -1);
  p1.SetCoeffAt(2, 1);
  // p2=1-x^2
  p2.SetCoeffAt(0, 1);
  p2.SetCoeffAt(2, -1);
  // p3=1+2x
  p3.SetCoeffAt(0, 1);
  p3.SetCoeffAt(1, 2);
  // Create rational: p1/p2 and p2/p3
  ECRational<ECPolynomial> r1(p1, p2), r2(p2, p3);
  ECRational<ECPolynomial> r3 = r1+ r2;
  // r1+r2= ( 2+ x -3x^2+ 2x^3+ x^4)/ ( 1+ 2x -x^2 -2x^3) 
  cout << "r1+r2=";
  r3.GetNumerator().Dump();
  cout << "/";
  r3.GetDenominator().Dump();
  cout << endl;
  ECRational<ECPolynomial> r4 = r1 * r2;
  // r1*r2= ( 1- x + x^3 - x^4)/ ( 1+ 2x -x^2 -2x^3) 
  cout << "r1*r2=";
  r4.GetNumerator().Dump();
  cout << "/";
  r4.GetDenominator().Dump();
  cout << endl;

  // skip division for now
}


int main()
{
  Test1();
  Test2(); // relies on friend functions for operators
  Test3(); // relies on polynomial to be fully implimented 
}
