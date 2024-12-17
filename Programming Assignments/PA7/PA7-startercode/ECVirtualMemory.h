//  ECVirtualMemory.h
//  Port the page replacement code to the ECVirtualMemory class 

#ifndef ECVirtualMemory_h
#define ECVirtualMemory_h

#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <deque>
#include <string>

void print(std::deque<int> q) // helper print function for deque
{
    for (auto x : q)
    {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    return;
}
void print(std::map<int,int> q) // helper print function for map
{
    for (auto x : q)
    {
        std::cout << "(" << x.first << ", " << x.second << ")";
    }
    std::cout << std::endl;
    return;
}
void print(std::vector<int> q) // helper print function for vector
{
    for (auto x : q)
    {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    return;
}

//*****************************************************************************
// Virtual memory: consists of memory pages and a main memory with limited capacity
// Page: represented by an integer; main memory can hold up to K pages
// Page replacement: when the main memory reaches its limit (i.e., having K pages) 
// and a new page (not currently in memory) is to be add, 
// then need to swap out one current page to make room for this new page
// This class: use LRU algorithm
class ECVirtualMemory
{
public:
    // Capacity: max # of pages in main memory 
    // we set faults to 0 initially 
    // should not need to do anything to memory
    ECVirtualMemory(int capacity) : cap(capacity), faults(0) {} 

    // Access a page in memory
    // here we want to check if the page is in memory
        // if it is in memory we can simply return the page
        // if it is not in memory 
            // first need to increase the fault number 
            // second need to check if memory is at capacity
                // if it is not we add the page to memory
                // if it is at capacity we need to remove the least recently used page then insert the page we are looking for
    void AccessPage(int page)
    {   
        //std::cout << "Page number: " << page << ", Current memory: "; print(LRUmem);
        requests.push_back(page); //add the page we want to access to the list of requests

        auto found = LRUmem.begin();
        for (auto x : LRUmem) // finding where page is in memory
        {
            if (x==page)
            {
                break;
            }
            found ++;
        }

        if (found != LRUmem.end()) // if page in memory just return page
        {
            LRUmem.erase(found); 
            LRUmem.push_back(page);
            return; 
        }
        else if (LRUmem.size() < cap) // put page to the end of memory if we have space
        {
            LRUmem.push_back(page); 
        }
        else if (LRUmem.size() == cap) // page not in mem and no space
        {
            // no space need to remove something from memory
            LRUmem.erase(LRUmem.begin());
            LRUmem.push_back(page);
        }
        faults++; // page was not in memory increase faults
    }

    // Return the number of page faults if optimal page replacement algorithm is run 
    // (for all the page requests that have been accessed so far)
    // Caution: this would erase previous run of LRU; you need to re-initialize to run
    // to get proper results
        // this is a very different function since it takes no params and returns the optimal number of faults
        // but how to impliment what it is suppose to do it very weird 
    // using the used vector we will calculate the number of pages faults with a different algorithm
        //this new algorithm relies on a 'hit' counter to tell you how often a page is used instead of hjow recently a page was used
    int RunOpt()
    {
        int min; 
        int minElement;
        int hitFaults=0;
        std::map<int,int>FutureCount;
        
        for (auto x:requests) {FutureCount[x]++;}
        // we are going to need a loop that goes through all the elements in requests
        for (int i=0; i<requests.size(); i++)
        {
            auto x = requests[i]; // now we can use i to easily index the vector
            FutureCount[x]--;
            min = 9999; // this is lazy way to set a min that will surely get overridden
            //std::cout << "Page number: " << x << ", Current memory: "; print(hitCountMem);
            if (hitCountMem.find(x) != hitCountMem.end()) // element is in mem
            {
                hitCountMem[x] = FutureCount[x];
                continue;
            }
            hitFaults++;
            if (hitCountMem.size() < cap) // element is not in mem but we have room
            {
                hitCountMem[x] = FutureCount[x];
            }
            else if (hitCountMem.size() == cap) // element is not in mem and we do not have room
            {
                // predictive way failing all tests
                int toremove = predict(requests, i+1);
                hitCountMem.erase(toremove);
                hitCountMem[x] = FutureCount[x];
                continue;

                // this does not really work but I want to keep it to not loose
                // we have to remove the least used in the future item
                // i think if every time we add something to memory we decrease the 
                // fullcount of that element we might get different behavior
                // for (auto y : hitCountMem)
                // {
                //     if (y.second <= min)
                //     {
                //         min = y.second;
                //         minElement = y.first;
                //     }
                // }
                // //if (FutureCount[x]!=0) // if this if is included we get less faults for 2 of the test cases but still fail three 
                // {
                //     hitCountMem.erase(minElement);
                //     hitCountMem[x] = FutureCount[x];
                // }
            }
            else // we should never get here
            {
                throw std::string ("SOMETHING WENT WRONG THIS SHOULD NEVER SHOW UP\n");
            }
        }
        return hitFaults;
    }

    // Return the number of pages in main memory
    // we can just reeturn the size of the map
    int GetNumPagesInMainMemory() const
    {
        return LRUmem.size(); // this should always be less or equal to capacity
    }

    // Return the number of page faults so far (for LRU algorithm)
    // a page fault is when we want to access a page but it is not in the virtual memory 
    // do we want to have the number of page faults as a private variable or should we recalculate it everytime?
    // probably faster to have it as a private variable
    int GetNumPageFaults() const 
    {
        return faults;
    }

private:
    // Implementation utilities
    // going to use some type of STL containter here to store the pages
    // for what containter type to use we can go a few ways 
        // we can use a map to which has as the pair <page id, some numer to represent the last time is was used>
            // for map when we access a page we would need to change the number that represents when it was access somehow
                // if we started all pages with the representation number as 0 as we access pages we just add 1 to the 
                // representation number
                // then to remove the least used page we remove the one with the lowest representation number 
                    // this might be faster than the vector version since we would only need to iterator over the map when we 
                    // need to remove pages not when we need to access them
            // to access a page we just need to say map[ id number ]
        // we can use a vector where the first or last element are the least recently used and then the middle elements 
        // are in order accordingly
            // for the vector version when we access a page we need to move its position 
            // to access a page we would need to search through the whole vector until the value matches the page id we want
        // we can also use a deque since removing and inserting for deques is fast at both ends
            // this is really efficient actually since it is so easy to remove and add to deques

    int predict(std::vector<int> &r, int curr)
    {
        // method to find what page is least used in the future
        // search in r from curr to end and if any elements currently in mem have 0
        // occureances return that element
        // if none have 0 occurances return first element
        int result = -1;
        int farthest = curr;
        int loopSpot;
        for (auto x:hitCountMem) {
            for (loopSpot = curr; loopSpot < r.size(); loopSpot++) {
                if (x.first == r[loopSpot]) {
                    if (loopSpot > farthest) {
                        farthest = loopSpot;
                        result = x.first;
                    }
                    break;
                }
            }
            // If a page is never referenced in future return it.
            if (loopSpot == r.size())
                return x.first;
        }
        // If all of the frames were not in future,
        // return the one that was farthest away
        return (result) == -1 ? hitCountMem.begin()->first : result;
    }

    std::deque <int> LRUmem; // the item at the begining of the deque will be the one least recently used 
    int faults;
    int cap;
    std::vector <int> requests; // this will be used in the runOPT funciton
    std::map<int, int> hitCountMem; // what track show often a page is used
};

#endif /* ECVirtualMemory_h */