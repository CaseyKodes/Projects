//  ECStringMatch.h
//  
//  Created by Yufeng Wu on 6/16/24.
//  Perform string matching: given a text string T, a pattern string P,
//  you are to decide whether P is a subtring of T
//  For example, T=mississippi, and P=iss, then P does appear in T. 
//  But for P'=ssp, then P' doesn't appear in T
//  You are to implement three functions for this task
//  (i) Brute-force matching: simply compare each substring of T (of the same length of P)
//  with P letter by letter
//  (ii) Use C++ provided function: use C++ string's built-in function find
//  (iii) Implement a numerical-based comparison algorithm (see below)

#ifndef ECStringMatch_h
#define ECStringMatch_h

#include <string>
using namespace std;

// Brute-force matching: given text strText and pattern strPattern
// return true if strPattern is an exact substring of strText, and false otherwise
bool ECStrMatchBruteForce(const string &strText, const string &strPattern);

// C++ library based striing matching: simply call C++ string's find function
bool ECStrMatchBuiltIn(const string &strText, const string &strPattern);

// Implement a slightly more complicated algorithm based on nummerical computation
// given text strText and pattern strPattern, an integer d, a prime number q 
// return true if strPattern is an exact substring of strText, and false otherwise
// The algorithm would work as follows:
// For each position i of strText, convert the subtring strText[i..i+length(strPattern)]
// to an integer (where d is the base of this integer) and then take modulo of q
// We also convert strPattern to an integer P in the same way. Then we simply compare 
// the integers constructed from strText. The key is, if the text integer doesn't match
// P, then the corresponding substring cannot match strPattern. Only when 
// P is equal to the text integer, we would conduct a letter-by-letter check to see if
// there is indeed a match at this position 
// Be careful: you need to implement the above procedure efficiently; 
// a naive implementation would be even slower than the brute-force!
// Be sure to look for ways to make your code more efficient.
bool ECStrMatchNumCompare(const string &strText, const string &strPattern, int d = 27, int q = 51839);

#endif /* ECStringMatch_h */
