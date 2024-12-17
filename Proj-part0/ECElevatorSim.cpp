//  ECElevatorSim.cpp
//  Created by Yufeng Wu on 6/27/23.
//  Elevator simulation

#include "ECElevatorSim.h"
#include <iostream>
using namespace std;

// prints for testing function
void printRs(vector<ECElevatorSimRequest>& toprint, int time)
{
    for (auto& x : toprint)
    {
        if (time == x.GetTime())
        {
            cout << "REQUEST MADE at time - " << x.GetTime();
            cout << ", from floor - " << x.GetFloorSrc();
            cout << ", to floor - " << x.GetFloorDest() << endl;
        }
    }
}
void whereat(int currFloor, int time, EC_ELEVATOR_DIR direction)
{
    if (direction != EC_ELEVATOR_STOPPED)
    {
        cout << "at time - " << time <<
            ", at floor - " << currFloor <<
            ", with direction - " << direction << endl;
    }
}
void printworking(vector <int> work)
{
    if (!work.empty())
    {
        cout << "list of request number indicies - ";
        for (auto x : work)
        {
            cout << x << " ";
        }
        cout << endl;
    }
}

// Simulate by going through all requests up to certain period of time (as specified in lenSim)
    // starting from time 0. For example, if lenSim = 10, simulation stops at time 10 (i.e., time 0 to 9)
    // Caution: the list of requests contain all requests made at different time;
    // at a specific time of simulation, some events may be made in the future 
    // (which you shouldn't consider these future requests)
void ECElevatorSim::Simulate(int lenSim)
{
    // vector of indices of which requests to edit
    vector <int> workingNums;
    bool picked, dropped;
    int numpeople = 0;

    // elevatore starts on floor 1 and stays there not moving until there is a request
    // this loop will be used because we can check if we are on the floor of a request 
    // and if we are we set the arrival time of that request to the current time
    // and set the fservised to true 
    for (int time = 0; time < lenSim; time++)
    {
        picked = false;
        dropped = false;

        // print for testing 
        //whereat(currFloor, time, direction);
        //printRs(requests, time);
        // printworking(workingNums);

        // requests are made sequencially, but multiple can be made at the same time
        // the classes and function I am making are going to be helpful 
        // in this function itself is where we will need to decide what direction to move the elevator
        workingNums = calculatework(time);
        for (auto x : workingNums)
        {
            // for checking if we can pick up or drop of a passenger
            pickup* pcheck = new pickup(requests[x], time, currFloor);
            picked += pcheck->check();
            delete pcheck;

            dropoff* dcheck = new dropoff(requests[x], time, currFloor);
            dropped += dcheck->check();
            delete dcheck;
        }
        workingNums = calculatework(time);

        // need a way to decide what direction the elevator will move
            // this depends on the resustes we have in working
            // we want to move to the closest request
                // if we are on floor 4 and there is a request on floor 2 and on floor 5 we go yo floor 5 
            // but if we are moving in a direction already we do not want to change based on the requests
            // the way i am calculateing direction is wrong
        SetCurrDir(calculateDirection(workingNums));
        SetCurrFloor(GetCurrFloor() + GetCurrDir());
        if (currFloor < 1 || currFloor>numFloors)
        {
            throw runtime_error("OUTSIDE OF THE RANGE OF FLOORS");
        }

        // there is a problem with dropped and picked not being 1 when they should be sometimes 
        // but other times when they should be 1 they are 
        if (dropped || picked)
        {
            time += 1;

            // since we skip over a time step when we pick someone up 
            // if there is a request in that skipped time step we will not be heading in the
            // right direction at the next time
            // so we need some sort of check if we skip a time so see if there is a request at the time we skip 
            for (auto& x : requests)
            {
                if (x.GetTime() == time && direction == EC_ELEVATOR_STOPPED)
                {
                    time -= 1; // this will pass the one test we dont like but it fails other tests
                    break;
                }
            }
        }
    }
}
void ECElevatorSim::Simulate2(int lenSim, vector<int>& spots, vector<int>& people, vector<vector<int>> &wants, vector<vector<int>> &waiting)
{
    // vector of indices of which requests to edit
    vector <int> workingNums;
    bool picked, dropped;
    int numpeople = 0;
    vector<int> temp;
    vector<int>waitingtime;

    // elevatore starts on floor 1 and stays there not moving until there is a request
    // this loop will be used because we can check if we are on the floor of a request 
    // and if we are we set the arrival time of that request to the current time
    // and set the fservised to true 
    for (int time = 0; time < lenSim; time++)
    {
        spots.push_back(currFloor);
        people.push_back(numpeople);
        picked = false;
        dropped = false;

        // print for testing 
        // whereat(currFloor, time, direction);
        // printRs(requests, time);
        // printworking(workingNums);

        // requests are made sequencially, but multiple can be made at the same time
        // the classes and function I am making are going to be helpful 
        // in this function itself is where we will need to decide what direction to move the elevator
        bool tempP, tempD;
        int pickedNum=0, droppedNum=0;
        workingNums = calculatework(time);

        pushes(temp, waitingtime, workingNums);
        wants.push_back(temp);
        waiting.push_back(waitingtime);
        

        for (auto x : workingNums)
        {
            // for checking if we can pick up or drop of a passenger
            pickup* pcheck = new pickup(requests[x], time, currFloor);
            tempP = pcheck->check();
            picked += tempP;
            if (tempP)
            {
                pickedNum++;
            }
            delete pcheck;

            dropoff* dcheck = new dropoff(requests[x], time, currFloor);
            tempD = dcheck->check();
            dropped += tempD;
            if (tempD)
            {
                droppedNum++;
            }
            delete dcheck;
        }

        // here we want to calculate where the waiting people are and then put them into the waiting people 2d array

        workingNums = calculatework(time);
        numpeople = numpeople + (pickedNum-droppedNum);

        // need a way to decide what direction the elevator will move
            // this depends on the resustes we have in working
            // we want to move to the closest request
                // if we are on floor 4 and there is a request on floor 2 and on floor 5 we go yo floor 5 
            // but if we are moving in a direction already we do not want to change based on the requests
            // the way i am calculateing direction is wrong
        SetCurrDir(calculateDirection(workingNums));
        SetCurrFloor(GetCurrFloor() + GetCurrDir());
        if (currFloor < 1 || currFloor>numFloors)
        {
            throw runtime_error("OUTSIDE OF THE RANGE OF FLOORS");
        }

        // there is a problem with dropped and picked not being 1 when they should be sometimes 
        // but other times when they should be 1 they are 
        if (dropped || picked)
        {
            time += 1;
            spots.push_back(currFloor - GetCurrDir());
            people.push_back(numpeople);
            wants.push_back(temp);
            waiting.push_back(waitingtime);

            // since we skip over a time step when we pick someone up 
            // if there is a request in that skipped time step we will not be heading in the
            // right direction at the next time
            // so we need some sort of check if we skip a time so see if there is a request at the time we skip 
            for (auto& x : requests)
            {
                if (x.GetTime() == time && direction == EC_ELEVATOR_STOPPED)
                {
                    time -= 1; // this will pass the one test we dont like but it fails other tests
                    spots.pop_back();
                    people.pop_back();
                    wants.pop_back();
                    waiting.pop_back();
                    break;
                }
            }
        }
    }
}