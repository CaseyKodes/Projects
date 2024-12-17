//  ECTournamentDraw.h
//  About tournament draw in sports

#ifndef ECTournamentDraw_h
#define ECTournamentDraw_h

#include <iostream>
#include <set>
#include <vector>
#include <map>

//*****************************************************************************
// Purpose of this assignment: get familiar with STL
// Containers: vector, set, map
// Algorithms: sort

//*****************************************************************************
// Interface functions

// checking whether a given tournament draw is valid or not
// Input: two STL vectors: (i) vecPlayersRank[i]: rank (1 being highest) of the i-th player
//   in the draw, (ii) vecPlayersCountries[i]: country (coded as integers) of the i-th player in the darw
//   you can assume the two vectors are of the same length; you can also assume the number of players
//   (size of vectors) is a power of 2, and has at least 16 players
// Output: true if the draw is valid wrt a set of pre-defined rules, false otherwise
// Note: by default, all four rules are to checked, unless turned off by the caller
bool ECCheckTournamentDraw(const std::vector<int> &vecPlayersRank, const std::vector<int> &vecPlayersCountries);

// configure checking: allow ties in ranking
void ECAllowDupRanks();

// configure checking: allow more than 2 players per country
void ECAllowMorePlayersPerCountry();

// configure checking: allow players from the same country to play in any round
void ECNoCheckFirstTwoRounds();

// configure checking: no checking of the distribution of seeded players
void ECNoSeedsCheck();

#endif /* ECTournamentDraw_h */
