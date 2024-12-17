#include <iostream>
#include <string>
using namespace std;

// Test whether strInput is a string composed of consecutive and increasing integers (in decimal formats)
// Return true if yes and false otherwise (return false if there are unexpected characters)
// For example, 1234578 would return false, while 1213141516 would return true (12 13 14 15 16)
// You may assume the integers is at most 999999 and there is no any seperators between numbers
// You may also assume integers are all non-negatives

// Tip: try to use library functions instead of writing a lot of code yourself
// functions in C++ string you may find useful:
// substr: extract a substring from a string
// stoi:  convert string to integer (be careful about how to handle exception)
// and so on..

bool ECConsecutiveInts(const string &strInput)
{
  int len = strInput.length();
  int half = len/2;
  // there is no way for the number to contain consecutive integers if 
  // the length of one choice integer is over half the length of the string
  for (int i = 0; i<half; i++)
  {
    if (i>6) // said we can assume no number larger than 999999
    {
      return false;
    }
    // the first number from the string is i+1 digits long and starts at index 0
    string check = strInput.substr(0, i+1);
    int num = atoi(check.c_str());

    // while loop until the new_string is the same length input string
    // changed from comparing strings with == to the built in compare function
    while (check.length() < len) 
    {
      num++;
      // add the next number to the string
      check += to_string(num);
    }
    // check if strings equal each other
    if (strInput.compare(check) == 0) 
    {
      return true;
    }
  }
  return false;
}

