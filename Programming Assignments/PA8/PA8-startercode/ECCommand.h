//  ECCommand.h

#ifndef ECCommand_h
#define ECCommand_h

#include <vector>
#include <iostream>

// ******************************************************
// Implement command design pattern

class ECCommand
{
public:
    virtual ~ECCommand() {}
    virtual void Execute() = 0;
    virtual void UnExecute() = 0;
};

// ******************************************************
// Implement command history

class ECCommandHistory
{
public:
    ECCommandHistory()
    {
        undoNumber = 0;
        commandNum = 0;
    }
    virtual ~ECCommandHistory()
    {
        for (auto x: listCommands)
        {
            delete x;
        }
    }
    bool Undo()
    {
        std::cout << "\nwe got to inside the undo\n";
        if (commandNum>0)
        {
            std::cout << "\nwe got to inside the undo if\n";
            listCommands.at(listCommands.size()-undoNumber-1)->UnExecute();
            undoNumber++;
            return true;
        }
        return false;
    }
    bool Redo()
    {
        std::cout << "\nwe got to inside the redo\n";
        if (undoNumber>0)
        {
            std::cout << "\nwe got to inside the redo if\n";
            listCommands.at(listCommands.size()-undoNumber)->Execute();
            undoNumber--;
            return true;
        }
        return false;
    }
    void ExecuteCmd( ECCommand *pCmd )
    {
        pCmd->Execute();
        listCommands.push_back(pCmd);
        commandNum++;
    }
    
private:
    // your code goes here
    int undoNumber;
    int commandNum;
    std::vector<ECCommand*> listCommands;
};

#endif /* ECCommand_h */
