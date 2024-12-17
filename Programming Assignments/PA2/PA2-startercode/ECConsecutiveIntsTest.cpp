// To build: c++ ECConsecutiveIntsTest.cpp ECConsecutiveInts.cpp -o test
#include <string>
#include <iostream>

using namespace std;

extern bool ECConsecutiveInts(const string &strInput);

int main()
{
  string a = "99100"; // yes
  bool fa = ECConsecutiveInts(a);
  if(fa)
  {
    cout << "Consecutive\n";
  }
  else
  {
    cout << "NOT Consecutive\n";
  }
  string b = "111212141516"; // no
  bool fb = ECConsecutiveInts(b);
  if(fb)
  {
    cout << "Consecutive\n";
  }
  else
  {
    cout << "NOT Consecutive\n";
  }
  string c = "123124125126"; // yes
  bool fc = ECConsecutiveInts(c);
  if(fc)
  {
    cout << "Consecutive\n";
  }
  else
  {
    cout << "NOT Consecutive\n";
  }
  string d = "123412351236123712381239"; // yes
  bool fd = ECConsecutiveInts(d);
  if(fd)
  {
    cout << "Consecutive\n";
  }
  else
  {
    cout << "NOT Consecutive\n";
  }
}

