//  ECTextDocument.cpp

#include "ECTextDocument.h"
#include <iostream>
#include <cctype>

using namespace std;

// **********************************************************
// Commands
// your code goes here 

// command implimentation needs to go here so it can have ectextdocument objects

// put functions
void put :: Execute()
{
  for (int i=0; i<toput.size(); i++)
  {
    doc.InsertCharAt(pos+i, toput[i]);
  }
}
void put :: UnExecute()
{
  for(int i=0; i<toput.size(); i++)
  {
    doc.RemoveCharAt(pos);
  }
}
// take functions 
void take :: Execute()
{
  for(int i=0; i<len; i++)
  {
    taken.push_back(doc.GetCharAt(pos)); // need this so we can undo it
    doc.RemoveCharAt(pos);
  }
}
void take :: UnExecute()
{
  for(int i=0; i<len; i++)
  {
    doc.InsertCharAt(pos+i, taken[i]);
  }
}
// cap functions 
void cap :: Execute()
{
  for (int i=0; i<len; i++)
  {
    doc.CapCharAt(pos+i);
  }
}
void cap :: UnExecute()
{
  for (int i=0; i<len; i++)
  {
    doc.LowerCharAt(pos+i);
  }
}
// low functions
void low :: Execute()
{
  for (int i=0; i<len; i++)
  {
    doc.LowerCharAt(pos+i);
  }
}
void low :: UnExecute()
{
  for (int i=0; i<len; i++)
  {
    doc.CapCharAt(pos+i);
  }
}

// **********************************************************
// Controller for text document

ECTextDocumentCtrl :: ECTextDocumentCtrl(ECTextDocument &docIn) : doc(docIn) {}

ECTextDocumentCtrl :: ~ECTextDocumentCtrl() {}

void ECTextDocumentCtrl :: InsertTextAt(int pos, const std::vector<char> &listCharsToIns)
{
  // your code
  put *action = new put(doc, pos, listCharsToIns);
  history.ExecuteCmd(action);
}

void ECTextDocumentCtrl :: RemoveTextAt(int pos, int lenToRemove)
{
  // your code
  take *action = new take(doc, pos, lenToRemove);
  history.ExecuteCmd(action);
}

void ECTextDocumentCtrl :: CapTextAt(int pos, int lenToCap)
{
  // your code
  cap *action = new cap(doc, pos, lenToCap);
  history.ExecuteCmd(action);
}

void ECTextDocumentCtrl :: LowerTextAt(int pos, int lenToLower)
{
  // your code
  low *action = new low(doc, pos, lenToLower);
  history.ExecuteCmd(action);
}

bool ECTextDocumentCtrl :: Undo()
{
  // your code
  return history.Undo();
}

bool ECTextDocumentCtrl :: Redo()
{
  // your code
  return history.Redo();
}

// **********************************************************
// Document for text document

ECTextDocument :: ECTextDocument() : docCtrl(new ECTextDocumentCtrl(*this)) {}

ECTextDocument :: ~ECTextDocument()
{
  delete docCtrl;
}

ECTextDocumentCtrl & ECTextDocument :: GetCtrl()
{
  return *docCtrl;
}

char ECTextDocument :: GetCharAt(int pos) const
{
  return listChars.at(pos);
}

void ECTextDocument :: InsertCharAt(int pos, char ch)
{
  // your code here
  listChars.insert(listChars.begin()+pos, ch); 
}

void ECTextDocument :: RemoveCharAt(int pos)
{
  // your code here
  listChars.erase(listChars.begin()+pos); 
}

void ECTextDocument :: CapCharAt(int pos)
{
  // your code here
  listChars[pos] = std::toupper(listChars[pos]); 
}

void ECTextDocument :: LowerCharAt(int pos)
{
  // your code here
  listChars[pos] = std::tolower(listChars[pos]); 
}
