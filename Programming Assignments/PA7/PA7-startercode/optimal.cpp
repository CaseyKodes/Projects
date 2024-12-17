#include <bits/stdc++.h>
using namespace std;
 
// Function to check whether a page exists
// in a frame or not
bool search(int key, vector<int>& fr)
{
    for (int i = 0; i < fr.size(); i++)
        if (fr[i] == key)
            return true;
    return false;
}
 
// Function to find the frame that will not be used
// recently in future after given index in pg[0..pn-1]
int predict(int pg[], vector<int>& fr, int pn, int index)
{
    // pg = requests
    // fr = hitcountmem
    // pn = requests.size
    // index = current index in requests

    // Store the index of pages which are going
    // to be used recently in future
    int res = -1, farthest = index;
    for (int toreturn = 0; toreturn < fr.size(); toreturn++) {
        int j;
        for (j = index; j < pn; j++) {
            if (fr[toreturn] == pg[j]) {
                if (j > farthest) {
                    farthest = j;
                    res = toreturn;
                }
                break;
            }
        }
        // If a page is never referenced in future,
        // return it.
        if (j == pn)
            return toreturn;
    }
    // If all of the frames were not in future,
    // return the one that was farthest away
    return (res == -1) ? 0 : res;
}
 
void optimalPage(int pg[], int pn, int fn)
{
    // Create an array for given number of
    // frames and initialize it as empty.
    vector<int> fr;
 
    // Traverse through page reference array
    // and check for miss and hit.
    int hit = 0;
    int miss = 0;
    for (int i = 0; i < pn; i++) 
    {
        // Page found in a frame : HIT
        if (search(pg[i], fr)) 
        {
            continue;
        }
        // Page not found in a frame : MISS
        // If there is space available in frames.
        if (fr.size() < fn)
        {
            fr.push_back(pg[i]);
            miss++;
        }
        // Find the page to be replaced.
            // only need to be concerned with this final else
        else 
        {
            int j = predict(pg, fr, pn, i + 1);
            fr[j] = pg[i];
            miss++;
        }
    }
    cout << "Faults = " << miss << endl;
}
 
// Driver Function
int main()
{
    int pg[] = {7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1};
    int pn = sizeof(pg) / sizeof(pg[0]);
    int fn = 3;
    cout << "should be 9 faults.\n";
    optimalPage(pg, pn, fn);
    return 0;
}
 