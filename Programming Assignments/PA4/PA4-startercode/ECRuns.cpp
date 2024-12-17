#include <string>
#include <iostream>
using namespace std;

// Return the number of runs, and the list of starting positions of runs in the passed in array (which you can assume it is large enough)
int ECRuns(const string &str, int *pListPositions )
{
    if (str.length() == 0)
    {
        return 0;
    }
    cout << str << endl;
    // start counting
    int nextStart = 1;
    int runNum = 1;
    pListPositions[0] = 0;
    for (int j=0; j<str.length()-1; j++)
    {
        if (0!=((str.substr(j, 1)).compare(str.substr(j+1,1))))
        {
            pListPositions[runNum] = nextStart;
            runNum++;
        }
        nextStart++;
    }
    return runNum;
}

