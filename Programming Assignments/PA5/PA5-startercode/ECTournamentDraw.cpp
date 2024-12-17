#include "ECTournamentDraw.h"
#include <bits/stdc++.h>
using namespace std;

//*****************************************************************************
// Please note:
// (1) Try to avoid long functions
// (2) Try to reduce nested loops; only use double loops when necessary; avoid triple loops
// (3) Try to reduce conditional statements
// My code has 1 double loop, 5 single loops, 4 if-conditional, longest function has 20 LOC, total LOC is 132 (incl. comments). 
// Try to write your code that has similar complexity
// Tips
// Consider using STL algorithms such as std::copy and inserters to remove explicity loops
//*****************************************************************************

// predefined rule bools
bool dupRanks = false;
bool allow2Plus = false;
bool anyRound = false;
bool noSeedCheck = false;

bool countNumber (const vector<int> &input, int max) // make sure there are no more than max elements in a vector
{
    map <int,int> count;
    for (auto x : input)
    {
        count[x]++;
        if (count[x]>max)
        {
            return false;
        }
    }
    return true;
}

bool checkrounds (const vector<int> &input) // break contries numers into sublist of 4 elements that do not have elements repeat
{
    bool result;
    std::vector<int> groups;
    for(int i=0; i<input.size()-4; i+=4)
    {
        groups.clear();    
        copy(input.begin()+i, input.begin()+i+4, inserter(groups, groups.end()));
        result = countNumber(groups, 1);
    }
    return result;
}

bool numberOfPartitions (const vector<int> &input, int partitions)
{
    bool result = true;
    int toAdd;
    vector <int> remaped;
    int splits = input.size()/partitions;

    for (int j=0; j<partitions; j++)
    {
        remaped.clear();
        for (int i = j*splits; i<(1+j)*splits; i++)
        {
            toAdd = input[i]-partitions;
            if (toAdd<0)
            {
                toAdd = 0;
            }
            remaped.insert(remaped.end(), toAdd);
        }
        // dependings on the number input as the max for count 
        // number a lot of tests either fail or pass
        for (auto x : remaped)
        {
            //cout << x << ", ";
        }
        //cout <<endl;
        result *= countNumber(remaped, 1); 
    }
    return result;
}

bool checkrank (const vector<int> &input) // make sure ranks are distributed evenly
{
    bool result = true;
    for (int i=2; i<=8; i*=2) // check halves, fourths, eigths of input
    {
        result *= numberOfPartitions(input, i);
    }
    return result;
}

//*****************************************************************************
// Interface functions
// checking whether a given tournament draw is valid or not
// Input: two STL vectors: (i) vecPlayersRank[i]: rank (1 being highest) of the i-th player
//   in the draw, (ii) vecPlayersCountries[i]: country (coded as integers) of the i-th player in the darw
//   you can assume the two vectors are of the same length; you can also assume the number of players
//   (size of vectors) is a power of 2, and has at least 16 players
// Output: true if the draw is valid wrt a set of pre-defined rules, false otherwise
// Note: by default, all four rules are to checked, unless turned off by the caller
bool ECCheckTournamentDraw(const vector<int> &vecPlayersRank, const vector<int> &vecPlayersCountries)
{
    bool result = true;
    if (!allow2Plus) // this will be used to count number of people per countries
    {
        result *= countNumber(vecPlayersCountries, 2); // only 2 people per contry max
    }
    if (!dupRanks) // this will be used to make sure no duplicate rankings
    {
        result *= countNumber(vecPlayersRank, 1); // can only be one of each rank
    }
    if (!anyRound) // need to make sure players from the same contry do not play in the first 2 rounds 
    {
        result *= checkrounds(vecPlayersCountries);
    }
    if (!noSeedCheck) // need to make sure seed distribution is valid 
    {
        result *= checkrank(vecPlayersRank);
    }    
    return result;
}

// for the configuring function thinking that I will just make them change a global variable 
// that is used in the draw function then at the end of the draw function the global variables get reset
// configure checking: allow ties in ranking
void ECAllowDupRanks()
{
    dupRanks = true;
}
// configure checking: allow more than 2 players per country
void ECAllowMorePlayersPerCountry()
{
    allow2Plus = true;
}
// configure checking: allow players from the same country to play in any round
void ECNoCheckFirstTwoRounds()
{
    anyRound = true;
}
// configure checking: no checking of the distribution of seeded players
void ECNoSeedsCheck()
{
    noSeedCheck = true;
}