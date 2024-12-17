// top line comments to make it look betters

#include "SimpleObserver.h"
#include "ECElevatorSim.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

//************************************************************

ECSimpleGraphicObserver::ECSimpleGraphicObserver(ECGraphicViewImp& viewIn) : view(viewIn) {}

void drawreflines(ECGraphicViewImp& view)
{
    for (int i = 0; i < 1000; i += 100)
    {
        view.DrawLine(0, i, 900, i, 1, ECGV_RED);
        view.DrawLine(i, 0, i, 900, 1, ECGV_RED);
    }
}

using namespace std;
vector<int>spots;
vector<int>peopleattime;
vector<vector<int>>wants;
vector<vector<int>> waiting;
int TOTAL_FLOORS;

struct useables {
    int NFLOORS;
    int timeSim;
    std::vector<ECElevatorSimRequest> rs;
};

useables maketest(const std::string& filename)
{
    useables data;
    std::ifstream file(filename);

    if (!file.is_open()) {
        throw std::runtime_error("Could not open file");
    }

    std::string line;
    int line_number = 0;

    while (std::getline(file, line)) 
    {
        std::istringstream iss(line);

        if (!line.empty() && line[0] == '#') // if the line starts with and pound sign we want to skip it 
        {
            continue;
        }
        else if (line_number == 0) // first line is for numfloors and timesim
        {
            iss >> data.NFLOORS >> data.timeSim;
        }
        else // any other line is to create requests
        {
            std::vector<int> vec(3);
            for (int i = 0; i < 3; ++i) {
                if (!(iss >> vec[i])) {
                    throw std::runtime_error("Invalid input format in line: " + line);
                }
            }
            ECElevatorSimRequest r(vec[0], vec[1], vec[2]);
            data.rs.push_back(r);
        }
        ++line_number;
    }

    file.close();
    return data;
}
static void Test(int f, int t, vector<ECElevatorSimRequest>&rs)
{
    cout << "\n****** my own test\n";
    // test setup
    TOTAL_FLOORS = f;
    const int timeSim = t;
    vector <ECElevatorSimRequest> listRequests;
    for (auto &r : rs)
    {
        listRequests.push_back(r);
    }

    ECElevatorSim sim(TOTAL_FLOORS, listRequests);

    /* now simulate will be doing all the work for us but is has to return thge things we need to work with
    it will need to return the following 
            WORKING
        an array of length timeSim, with the elevator position at each time step
        an array of length timeSim, with the number of people on the elevator at a time
        an array telling us where the people want to go, this is a 2d array
            this will be used to print the number floor they want to go to on them
        an array telling us where the people who are waiting to be picked up are, this needs to be a 2d array
            this will show the people outside of the elevator before they get in
    */
    
    // we use a second simulate function to get around some problems 
    sim.Simulate2(timeSim, spots, peopleattime, wants, waiting);
}

void ECSimpleGraphicObserver::Update()
{
    // here is my idea

    /*  
        what if we first simulate the logic and state of the elevator at all times
            this would include how many people are on it what floor it is at 
        then we annimate based of off that
        so i can use a key to say go to the next timestep which would show us the update

        also need to figure out how to what people are waiting outside of the elevator at what time
            might be able to use the fact that each persons requested floor is differnet 
            depending on if they are in the elevator or not
        think maybe i just input another vector to fill into Simulate2

    */
    if (print)
    {
        spots.clear();
        peopleattime.clear();
        wants.clear();

        // this working in openeing a file and then makeing the test from that file 
        useables touse = maketest("paxton.txt"); // this is where you put the file you want to make a simulation from
        Test(touse.NFLOORS, touse.timeSim, touse.rs);
        
        print = false;
        spots.push_back(spots[spots.size() - 1]);
        peopleattime.push_back(peopleattime[peopleattime.size()-1] - 1);
    }
    

    ECGVEventType evt = view.GetCurrEvent();
    if (evt == ECGV_EV_KEY_UP_SPACE)
    {
        fIsSpaceBarPressed = true;

        if (started)
        {
            if (pause)
            {
                pause = false;
            }
            else if (!pause)
            {
                pause = true;
            }
        }

        view.SetRedraw(true);
    }
    if (evt == ECGV_EV_KEY_UP_G)
    {
        // we should also use this event to start the timer 
        started = true;
        view.SetRedraw(true);
    }
    if (evt == ECGV_EV_KEY_UP_RIGHT)
    {
        time++;
        if (time == spots.size()-1)
        {
            time--;
            cout << "end of runtime\n";
        }
        else
        {
            cout << time << " - time, floor - " << spots[time] << endl;
        }
    }
    if (evt == ECGV_EV_KEY_UP_LEFT)
    {
        time--;
        if (time < 0)
        {
            time++;
            cout << "time less than 0\n";
        }
        else
        {
            cout << time << " - time, floor - " << spots[time] << endl;
        }
    }

    // if this is the timer event
    // we need to draw things here so they can stay on the screen since the timer constantly runs 
    if (evt == ECGV_EV_TIMER)
    {
        // if space bar already pressed, draw a winidow
        // Note: you need to draw this in the timer event; otherwise you won't see the rectangle
        if (fIsSpaceBarPressed)
        {
            // drawing the original background for the whole thing
            view.DrawFilledRectangle(0, 0, 900, 900, ECGV_BLACK); // main background 

            // to see lines that tell us where the 100s are 
            //drawreflines(view);

            // draw the representaion of floors 
                // TOTAL_FLOORS is only temperary
            for (int i = TOTAL_FLOORS; i > 0; i--)
            {
                ECGVColor color = static_cast<ECGVColor>(1);
                // boxes representing each floor
                view.DrawRectangle(xstart, ystart - ysize * i, xstart + xsize, ystart - ysize * i - ysize, 5, color);
                // buttons for each floor 
                view.DrawCircle(xstart + xsize + r + 7, ystart - ysize * i - ysize + r + off2 - 20, r, 3, ECGV_BLUE); 
            }
            timer++;
            view.SetRedraw(true); 

        }
        if (started)
        {
            // draws the time 
            if (time < spots.size() - 2)
            {
                view.DrawFilledRectangle(600, 800, 900, 900, ECGV_WHITE);
                char timeLine[] = "Time - ";
                view.DrawText(700, 825, timeLine, ECGV_BLACK);
                string t = to_string(time);
                char const* t_char = t.c_str();
                view.DrawText(825, 825, t_char, ECGV_BLACK);
            }
            else
            {
                view.DrawFilledRectangle(600, 800, 900, 900, ECGV_GREEN);
                view.DrawText(750, 825, "Sim Done", ECGV_BLACK);
            }

            // draws the pause text 
            if (pause)
            {
                view.DrawFilledRectangle(600, 700, 900, 800, ECGV_RED);
                view.DrawText(750, 725, "Paused", ECGV_BLACK);
            }

            // decides how fast we move times, larger the number after % the longer a time step is
            if (timer % 40 == 0 && !pause)
            {
                time++;
                if (time == spots.size() - 1)
                {
                    time--;
                }
            }


            // change how we are caulculateing ey1 and ey2 so it changed based on the floor from spots
            // this works to move the elevator cabin and people get on and off 
            position = spots[time];
            peopleinElevator = peopleattime[time];

            //  position holds the floor we want to be on 
            //  this calculation turns a floor number into a pixel number for the box to be drawn at
            newey1 = 900 - position * 100;

            // this animates the elevator
            if (ey1 != newey1)
            {
                if (ey1 < newey1)
                {
                    ey1 += 5;
                    ey2 += 5;
                }
                if (ey1 > newey1)
                {
                    ey1 -= 5;
                    ey2 -= 5;
                }
            }

            //show the elevator 
            view.DrawFilledRectangle(ex1, ey1, ex2, ey2, ECGV_BLUE);
            int spacing = 40;
            int start = 20;
            // draw the people in the elevator
            for (int i = 0; i < peopleinElevator; i++)
            {
                view.DrawFilledCircle(start + spacing * i, ey2 - 35, 15, ECGV_WHITE);
                view.DrawLine(start + spacing * i, ey2 - 30, start + spacing * i, ey2, 15, ECGV_WHITE);
                view.DrawLine(start + spacing * i, ey2 - 20, start + spacing * i - 15, ey2 - 10, 6, ECGV_WHITE);
                view.DrawLine(start + spacing * i, ey2 - 20, start + spacing * i + 15, ey2 - 10, 6, ECGV_WHITE);
                view.DrawLine(start + spacing * i, ey2 - 7, start + spacing * i, ey2, 3, ECGV_BLACK);

                // this will print the floor number a passenger wants to go to on that passenger
                string istr = to_string(wants[time][i]);
                char const* ichar = istr.c_str();
                view.DrawText(start + spacing * i, ey2 - 50, ichar);
            }
            // draw the people that are wating outside of the elevator
            for (int i=0; i<waiting[time].size(); i++)
            {
                int y = 1000 - waiting[time][i] * 100;
                view.DrawFilledCircle(417, y - 55, r, ECGV_BLUE);

                view.DrawFilledCircle(450 + i * 40, y - 35, 15, ECGV_WHITE);
                view.DrawLine(450 + i * 40, y - 30, 450 + i * 40, y, 15, ECGV_WHITE);
                view.DrawLine(450 + i * 40, y - 20, 450 - 15 + i * 40, y - 10, 6, ECGV_WHITE);
                view.DrawLine(450 + i * 40, y - 20, 450 + 15 + i * 40, y - 10, 6, ECGV_WHITE);
                view.DrawLine(450 + i * 40, y - 7, 450 + i * 40, y, 3, ECGV_BLACK);
            }
        }
    }
}

