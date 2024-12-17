#pragma once
//  ECElevatorSim.h
//  Created by Yufeng Wu on 6/27/23.
//  Elevator simulation

#ifndef ECElevatorSim_h
#define ECElevatorSim_h

#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cmath>

//*****************************************************************************
// DON'T CHANGE THIS CLASS
// 
// Elevator simulation request: 
// (i) time: when the request is made
// (ii) floorSrc: which floor the user is at at present
// (iii) floorDest floor: where the user wants to go; we assume floorDest != floorSrc
// 
// Note: a request is in three stages:
// (i) floor request: the passenger is waiting at floorSrc; once the elevator arrived 
// at the floor (and in the right direction), move to the next stage
// (ii) inside request: passenger now requests to go to a specific floor once inside the elevator
// (iii) Once the passenger arrives at the floor, this request is considered to be "serviced"
//
// two sspecial requests:
// (a) maintenance start: floorSrc=floorDest=-1; put elevator into maintenance 
// starting at the specified time; elevator starts at the current floor
// (b) maintenance end: floorSrc=floorDest=0; put elevator back to operation (from the current floor)
class ECElevatorSimRequest
{
public:
    ECElevatorSimRequest(int timeIn, int floorSrcIn, int floorDestIn) : time(timeIn), floorSrc(floorSrcIn),
        floorDest(floorDestIn), fFloorReqDone(false), fServiced(false), timeArrive(-1) {
    }
    ECElevatorSimRequest(const ECElevatorSimRequest& rhs) : time(rhs.time), floorSrc(rhs.floorSrc),
        floorDest(rhs.floorDest), fFloorReqDone(rhs.fFloorReqDone), fServiced(rhs.fServiced), timeArrive(rhs.timeArrive) {
    }
    int GetTime() const { return time; }
    int GetFloorSrc() const { return floorSrc; }
    int GetFloorDest() const { return floorDest; }
    bool IsGoingUp() const { return floorDest >= floorSrc; }

    // Is this passenger in the elevator or not
    bool IsFloorRequestDone() const { return fFloorReqDone; }
    void SetFloorRequestDone(bool f) { fFloorReqDone = f; }

    // Is this event serviced (i.e., the passenger has arrived at the desstination)?
    bool IsServiced() const { return fServiced; }
    void SetServiced(bool f) { fServiced = f; }

    // Get the floor to service
    // If this is in stage (i): waiting at a floor, return that floor waiting at
    // If this is in stage (ii): inside an elevator, return the floor going to
    // Otherwise, return -1
    int GetRequestedFloor() const {
        if (IsServiced()) {
            return -1;
        }
        else if (IsFloorRequestDone()) {
            return GetFloorDest();
        }
        else {
            return GetFloorSrc();
        }
    }

    // Wait time: get/set. Note: you need to maintain the wait time yourself!
    int GetArriveTime() const { return timeArrive; }
    void SetArriveTime(int t) { timeArrive = t; }

    // Check if this is the special maintenance start request
    bool IsMaintenanceStart() const { return floorSrc == -1 && floorDest == -1; }
    bool IsMaintenanceEnd() const { return floorSrc == 0 && floorDest == 0; }

private:
    int time;           // time of request made
    int floorSrc;       // which floor the request is made
    int floorDest;      // which floor is going

    // saying we have picked up the passenger
    bool fFloorReqDone; // is this passenger passing stage one (no longer waiting at the floor) or not

    bool fServiced;     // is this request serviced already?
    int timeArrive;     // when the user gets to the desitnation floor
};

//*****************************************************************************
// Elevator moving direction

typedef enum
{
    EC_ELEVATOR_STOPPED = 0,    // not moving
    EC_ELEVATOR_UP = 1,         // moving up
    EC_ELEVATOR_DOWN = -1       // moving down
} EC_ELEVATOR_DIR;

//*****************************************************************************
// Add your own classes here...
/*

might want to make a class that has a *check request function*
should this go into the ECElevatorSim class?
    this function would take a request and see if it has been made yet (time on request <= time on sim)
        if so we need to see if there are any current requests being proccessed
            if there are and we wait to either pass the floor of the new request or until no more requests are being made
            if there are not we go directly to the new request
i think i will need two extra functions, 1 to check if we are on the floor that a request needs to be dropped off on
and one to check if we are on the floors for a request to be picked up on
might be able to combine them but the functino would be too long
both of these would need to take a request, a time, and a floor
    i do not think it would need to take a direction

to use inheritacne we can have a general class called "requestcheck"
then two subclasses requestcheckpickup and requestcheckdrop off
one would deal with when we arrive on the final destination floor
and one would deal with when we arrice on the original source floor

*/

class requestCheck
{
public:
    requestCheck(ECElevatorSimRequest& r, int& t, int f)
        : request(r), time(t), floor(f)
    {}

    // here would be the function to check if we can load or unload a passenger at the current time
    // not sure what i would want the return type to be for not void 
    // general structure of this function, implimentation will change in subclasses
        // check if the request has been serviced i.e. - is the request done
            // if serviced we are done so break out of function
        // check if request has been started yet i.e. the passenger has been picked up 
            // if picked up we can break out of the pick up funciton but need to continue in the drop off function
            // if not picked up we can break out of the drop off function but need to continue in the pick up function 
        // check if the current time is >= request time on the request
            // if not we can break out of the function
        // check if floor number is == request floor number 
            // if yes we can either drop off or pick up the passenger and change the coorosponding bool in the request object
    virtual bool check() = 0;
    int getTime() { return time; }
    int getFloor() { return floor; }
    ECElevatorSimRequest getr() { return request; }

protected:
    ECElevatorSimRequest& request;
    int time;
    int floor;
};

class pickup : public requestCheck
{
public:
    pickup(ECElevatorSimRequest& r, int t, int f) : requestCheck(r, t, f) {}
    virtual bool check() override
    {
        // for pick up we need the request to 
            // 1 not be finished 
            // 2 not be started yet 
        if (!request.IsFloorRequestDone() && !request.IsServiced())
        {
            if (getFloor() == request.GetRequestedFloor())
            {
                std::cout << "--pickup at time " << time << std::endl;
                request.SetFloorRequestDone(true);
                return true;
            }
        }
        return false;
    }
};

class dropoff : public requestCheck
{
public:
    dropoff(ECElevatorSimRequest& r, int t, int f) : requestCheck(r, t, f) {}
    virtual bool check() override
    {
        // for drop we need the request to 
            // 1 not be finished 
            // 2 be started  
        if (request.IsFloorRequestDone() && !request.IsServiced())
        {
            if (getFloor() == request.GetRequestedFloor() && request.IsFloorRequestDone())
            {
                std::cout << "--dropoff at time " << time << std::endl;
                request.SetServiced(true);
                request.SetArriveTime(time);
                return true;
            }
        }
        return false;
    }
};

//*****************************************************************************
// Simulation of elevator

class ECElevatorSim
{
public:
    // numFloors: number of floors serviced (floors numbers from 1 to numFloors)
    ECElevatorSim(int numFloors, std::vector<ECElevatorSimRequest>& listRequests)
        : numFloors(numFloors), requests(listRequests), currFloor(1),
        direction(EC_ELEVATOR_STOPPED)
    {
    }

    // free buffer
    ~ECElevatorSim()
    {
        // destructor 
    }

    // Simulate by going through all requests up to certain period of time (as specified in lenSim)
    // starting from time 0. For example, if lenSim = 10, simulation stops at time 10 (i.e., time 0 to 9)
    // Caution: the list of requests contain all requests made at different time;
    // at a specific time of simulation, some events may be made in the future (which you shouldn't consider these future requests)
        // make in .cpp file
    void Simulate(int lenSim);
    void Simulate2(int lenSim, std::vector<int>& spots, std::vector<int>& people, std::vector<std::vector<int>>& wants, std::vector<std::vector<int>>& waiting);

    // The following methods are about querying/setting states of the elevator
    // which include (i) number of floors of the elevator, 
    // (ii) the current floor: which is the elevator at right now (at the time of this querying). 
    // Note: we don't model the tranisent states like when the elevator is between two floors
    // (iii) the direction of the elevator: up/down/not moving

    // Get num of floors
    int GetNumFloors() const { return numFloors; }

    // Get current floor
    int GetCurrFloor() const { return currFloor; }

    // Set current floor
    void SetCurrFloor(int f) { currFloor = f; }

    // Get current direction
    EC_ELEVATOR_DIR GetCurrDir() const { return direction; }

    // Set current direction
    void SetCurrDir(EC_ELEVATOR_DIR dir) { direction = dir; }

    // funciton to calculate what request we are working on
    std::vector<int> calculatework(int time)
    {
        std::vector<int> workingNums;
        for (int i = 0; i < requests.size(); i++)
        {
            if (time >= requests[i].GetTime() && !requests[i].IsServiced())
            {
                workingNums.push_back(i);
            }
        }
        return workingNums;
    }

    void pushes(std::vector<int>& temp, std::vector<int>& waitingtime, std::vector<int>& workingNums)
    {
        temp.clear();
        waitingtime.clear();
        for (auto x : workingNums)
        {
            temp.push_back(requests[x].GetFloorDest());
            if (requests[x].GetRequestedFloor() != requests[x].GetFloorDest())
            {
                waitingtime.push_back(requests[x].GetRequestedFloor());
            }
        }
    }

    // might not be right for multiple requests 
    // this does not work if we have a new request at a floor close to the elevator 
    // but in the opposite direction of a request we are currently proccessing
    EC_ELEVATOR_DIR calculateDirection(std::vector <int> rNums)
    {
        // elevator is initiallized at stopped state so if statements that need it to not be in stopped state will never work
        // to see if we want to go up we need to check if there are any requests that want to go up vis versa for down 
        // we know which requests we need to handle based on the input array
        // we can split this input array into two arrays one is requests to go down floors one is requests to go up floors
        // from those two array we can find which request is the closest and move towards that request 
            // if we are in stopped state
            // if we are in a moving state we want to keep moving in that direction until there are no requests in that direction
        std::vector<int> upR;
        std::vector<int> downR;
        for (auto x : rNums)
        {

            // since we are using desitnation floor if we at some point have a reqwuest that 
            // needs to be picked up from a lower floor and one that needs to be brought to a lower floor 

            if (requests[x].GetRequestedFloor() > currFloor)
            {
                upR.push_back(x);
            }
            else
            {
                downR.push_back(x);
            }
        }
        if (direction != EC_ELEVATOR_STOPPED)
        {
            if (!upR.empty() && direction == EC_ELEVATOR_UP)
            {
                return EC_ELEVATOR_UP;
            }
            if (!downR.empty() && direction == EC_ELEVATOR_DOWN)
            {
                return EC_ELEVATOR_DOWN;
            }
        }
        if (!upR.empty())
        {
            return EC_ELEVATOR_UP;
        }
        if (!downR.empty())
        {
            return EC_ELEVATOR_DOWN;
        }
        return EC_ELEVATOR_STOPPED;
    }

private:
    // Your code here
    int numFloors;
    int currFloor;
    EC_ELEVATOR_DIR direction;
    std::vector<ECElevatorSimRequest>& requests;
};

#endif /* ECElevatorSim_h */