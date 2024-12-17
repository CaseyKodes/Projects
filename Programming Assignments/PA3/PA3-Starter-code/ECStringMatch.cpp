//  ECStringMatch.cpp

#include "ECStringMatch.h"
#include <iostream>
#include <math.h>

// Brute-force matching: given text strText and pattern strPattern
// return true if strPattern is an exact substring of strText, and false otherwise
bool ECStrMatchBruteForce(const string &strText, const string &strPattern)
{
    // this should just be checking substrings at every index
    int Flen = strText.length();
    int Plen = strPattern.length();
    for (int i=0;i<Flen;i++)
    {
        string check = strText.substr(i, Plen);
        if (strPattern.compare(check) == 0)
        {
            return true;
        }
    }
    return false;
}

// C++ library based striing matching: simply call C++ string's find function
// This function is given; DON'T CHANGE IT
bool ECStrMatchBuiltIn(const string &strText, const string &strPattern)
{
    return strText.find(strPattern) != string::npos;
}

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
bool ECStrMatchNumCompare(const string &strText, const string &strPattern, int d, int q)
{   
    /* 
    not passing test cases 3 and 4
    I believe it to be by the fact that these test cases have a 
    repeating series of letters until the very end with a different letter 
    at the very end
    but it is strange that this would be working for all the other cases
    */

    // setting up variables
    int n = strText.length();
    int m = strPattern.length();
    int i, j;

    int p = 0;
    int tNot = 0;
    int h = 1;

    // calculate h
    for (int i = 0; i < m - 1; i++)
    {  
        h = (d*h) %q;
    }

    // for testing
    // cout << endl << "Text is    : " << strText << endl;
    // cout << "Pattern is : " << strPattern << endl;

    // preprocessing
    for (int s=0; s<m; s++)
    {
        p = ((d*p) +strPattern[s]) % q;
        tNot = ((d*tNot) +strText[s]) % q;
    }

    //cout << endl << "The hash of the pattern 'p': " << p << endl;

    // matching
    for(i=0; i<n-m+1; i++)
    {
        //cout << "The hash of the current string 'tNot': " << tNot << endl;
        if (p==tNot)
        {
            bool correct = true;
            for (j=0; j<m; j++)
            {
                if (strText[i+j] != strPattern[j])
                {
                    correct = false;
                    break;
                }
            }
            if (correct)
            {
                cout << "Pattern found at index: " << i << endl;
                cout << "------------- ";
                return true;
            }
        }
        if (i<n-m+1)
        {
            tNot = (d* (tNot- (strText[i]*h)) +strText[i+m]) %q;

            // if tNot is negative we make is positive
            if (tNot<0)
            {
                tNot+=q;
            }
        }
    }
    return false;
}

