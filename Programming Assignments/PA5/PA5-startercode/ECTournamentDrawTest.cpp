// To build: g++ ECTournamentDrawTest.cpp -std=c++17 

#include "ECTournamentDraw.cpp"
using namespace std;

template <class T>
void EC_ASSERT_EQ(const T &vRes, const T &vExp)
{
  if( vRes == vExp )
  {
    cout << "Test passed\n";
  }
  else
  {
    cout << "Test FAILED: test result: " << vRes << ", expecting: " << vExp << endl;
  }
}

// test cases
static void Test1()
{
  // test to ensure all players are of distinct ranks
  cout << "Test1\n";
  vector<int> playerRanks1 = {1,9,5,10, 3,11,7,12, 2,13,6,14, 4,15,8,16};
  vector<int> playerRanks2 = {1,9,5,10,3,11,7,16,2,13,6,14,4,15,8,16};
  vector<int> playerCountries = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
  bool f1 = ECCheckTournamentDraw(playerRanks1, playerCountries);
  EC_ASSERT_EQ(f1, true);
  bool f2 = ECCheckTournamentDraw(playerRanks2, playerCountries);
  EC_ASSERT_EQ(f2, false);
  // now turn off distinct rank check
  ECAllowDupRanks();
  bool f3 = ECCheckTournamentDraw(playerRanks2, playerCountries);
  EC_ASSERT_EQ(f3, true);
}

static void Test2()
{
  // test to ensure no country has more than 2 players
  cout << "Test2\n";
  vector<int> playerRanks = {1,9,5,10,3,11,7,12,2,13,6,14,4,15,8,16};
  vector<int> playerCountries1 = {1,2,3,4,2,3,7,8,1,10,11,12,13,14,8,16};
  bool f1 = ECCheckTournamentDraw(playerRanks, playerCountries1);
  EC_ASSERT_EQ(f1, true);
  vector<int> playerCountries2 = {1,2,3,4,2,1,7,8,9,10,2,13,13,14,15,16};
  bool f2 = ECCheckTournamentDraw(playerRanks, playerCountries2);
  EC_ASSERT_EQ(f2, false);
  // now allow dup ranks, but this is still invalid
  ECAllowDupRanks();
  bool f3 = ECCheckTournamentDraw(playerRanks, playerCountries2);
  EC_ASSERT_EQ(f3, false);
  // now allow one country has more than 2 players
  ECAllowMorePlayersPerCountry();
  f3 = ECCheckTournamentDraw(playerRanks, playerCountries2);
  EC_ASSERT_EQ(f3, true);
}

static void Test3()
{
  // test to ensure no two players from the same country would play in the first two rounds
  cout << "Test3\n";
  vector<int> playerRanks = {1,9,5,10,3,11,7,12,2,13,6,14,4,15,8,16};
  vector<int> playerCountries1 = {1,2,3,4,2,3,7,8,1,10,11,12,13,14,8,16};
  bool f1 = ECCheckTournamentDraw(playerRanks, playerCountries1);
  EC_ASSERT_EQ(f1, true);
  vector<int> playerCountries2 = {1,2,3,4,2,1,7,8,9,10,11,9,13,14,15,16};
  bool f2 = ECCheckTournamentDraw(playerRanks, playerCountries2);
  EC_ASSERT_EQ(f2, false);
  // now allow playes from the same country with more players but this won't help
  ECAllowMorePlayersPerCountry();
  bool f3 = ECCheckTournamentDraw(playerRanks, playerCountries2);
  EC_ASSERT_EQ(f3, false);
  // now no checking of first two rounds
  ECNoCheckFirstTwoRounds();
  f3 = ECCheckTournamentDraw(playerRanks, playerCountries2);
  EC_ASSERT_EQ(f3, true);
}

static void Test4()
{
  // test to ensure seeds distribution is valid
  cout << "Test4\n";
  vector<int> playerRanks1 = {1,9,5,10, 3,11,7,12, 2,13,6,14, 4,15,8,16};
  vector<int> playerCountries = {1,2,3,4,2,3,7,8,1,10,11,12,13,14,8,16};
  bool f1 = ECCheckTournamentDraw(playerRanks1, playerCountries);
  EC_ASSERT_EQ(f1, true);
  vector<int> playerRanks2 = {1,9,5,10, 2,11,7,12, 3,13,6,14, 4,15,8,16};
  bool f2 = ECCheckTournamentDraw(playerRanks2, playerCountries);
  EC_ASSERT_EQ(f2, false);
  vector<int> playerRanks3 = {1,9,5,10,3,11,4,12,3,13,6,14,7,15,8,16};
  bool f3 = ECCheckTournamentDraw(playerRanks3, playerCountries);
  EC_ASSERT_EQ(f3, false);
  vector<int> playerRanks4 = {1,9,5,10, 3,11,4,12, 2,13,6,7, 14,15,8,16};
  bool f4 = ECCheckTournamentDraw(playerRanks4, playerCountries);
  EC_ASSERT_EQ(f4, false);
  // no seeds checking
  ECNoSeedsCheck();
  f4 = ECCheckTournamentDraw(playerRanks4, playerCountries);
  EC_ASSERT_EQ(f4, true);
}

int main()
{
  Test1();
  Test2();
  Test3();
  Test4();
}
