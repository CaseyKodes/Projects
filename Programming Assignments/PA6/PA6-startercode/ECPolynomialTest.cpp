// To build: g++ ECPolynomial.cpp ECPolynomialTest.cpp -std=c++17

#include <iostream>
using namespace std;

#include "ECPolynomial.cpp"

int main()
{
  vector<double> vec1;
  vec1.push_back(-3);
  vec1.push_back(1);
  ECPolynomial poly1(vec1);

  vector<double> vec2 ;
  vec2.push_back(-4);
  vec2.push_back(0);
  vec2.push_back(-2);
  vec2.push_back(1);
  ECPolynomial poly2(vec2);
  
  cout << "poly1 ";
  poly1.Dump();
  cout  << "poly2: ";
  poly2.Dump();

  // ECPolynomial poly3 = poly1+poly2;
  // cout << "poly1+poly2 = ";
  // poly3.Dump();

  // ECPolynomial poly4 = poly1* poly2;
  // cout << "poly1*poly2 = ";
  // poly4.Dump();
 
  ECPolynomial poly5 = poly2 / poly1;
  cout << "\nDivide poly2 by poly1 = ";
  poly5.Dump();
  cout << "should be: +3 + 1x^1 + 1x^2\n";
  ECPolynomial poly6 = poly2 % poly1;
  cout << "remainder: ";
  poly6.Dump();
  cout << "should be: 5\n";

  // ECPolynomial poly7 = poly1.Scale(2.0);
  // cout << "poly1*2: ";
  // poly7.Dump();
}

