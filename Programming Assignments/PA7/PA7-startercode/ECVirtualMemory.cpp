//  ECVirtualMemory.cpp
//  Created by Yufeng Wu on 8/30/23.
//  Implement popular page replacement algorithms

#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <string>
#include "ECVirtualMemory.h"
using namespace std;


//*****************************************************************************
// Virtual memory: consists of memory pages and a main memory with limited capacity
// Page: represented by an integer; main memory can hold up to K pages
// Page replacement: when the main memory reaches its limit (i.e., having K pages) 
// and a new page (not currently in memory) is to be add, 
// then need to swap out one current page to make room for this new page
// This class: use OPT or LRU algorithm

// Your code here

