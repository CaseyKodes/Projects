#include <string>
#include <vector>
#include <iostream>
using namespace std;

void RemoveDupPointers(vector<string *> &arrayPtrs)
{
    // arrayPtrs: STL vector of pointers to strings
    // remove pointers that are pointed to identical strings in the array
    
    string check, checknext;
    for (int j=0; j<arrayPtrs.size(); j++)
    {
        for (int i=j+1; i<arrayPtrs.size(); i++)
        {   
            // make into string for easy call to compare function
            check = *arrayPtrs[i];
            checknext = *arrayPtrs[j];
            if (check.compare(checknext) == 0)
            {
                arrayPtrs.erase(arrayPtrs.begin()+i);
                i--;
            }
        }
    }
}

/*
int main()
{
    string s1="abc", s2="bcd", s3="abc";
    vector <string *> array = {&s1, &s2, &s3, &s1};

    cout << "Before function" << endl;
    for (int i=0; i<array.size(); i++)
    {
        cout << *array[i] << " "; 
    }
    
    // actual function call
    // working but i do not like the nested loop
    RemoveDupPointers(array);

    cout << "\n\nAfter function" << endl;
    for (int i=0; i<array.size(); i++)
    {
        cout << *array[i] << " "; 
    }
    cout << endl;
} 
*/