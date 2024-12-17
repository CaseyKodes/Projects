//  ECTextDocument.h

#ifndef ECTextDocument_h
#define ECTextDocument_h

#include "ECCommand.cpp"
#include <vector>

class ECTextDocument;

// **********************************************************
// Implements Commands for editing 
// your code goes here
class put : public ECCommand
{
public:
    put(ECTextDocument &curr, int p, std::vector<char> toinsert) : pos(p), toput(toinsert), doc(curr) {}
    virtual void Execute() override;
    virtual void UnExecute() override;
private:
    int pos;
    std::vector<char> toput;
    ECTextDocument &doc;
};
class take : public ECCommand
{
public:
    take(ECTextDocument &curr, int p, int l) : pos(p), len(l), doc(curr) {}
    virtual void Execute() override;
    virtual void UnExecute() override;
private:
    int pos;
    int len;
    ECTextDocument &doc;
    std::vector<char> taken;
};
class cap : public ECCommand
{
public:
    cap(ECTextDocument &curr, int p, int l) : pos(p), len(l), doc(curr) {}
    virtual void Execute() override;
    virtual void UnExecute() override;
private:
    int pos;
    int len;
    ECTextDocument &doc;
};
class low : public ECCommand
{
public:
    low(ECTextDocument &curr, int p, int l) : pos(p), len(l), doc(curr) {}
    virtual void Execute() override;
    virtual void UnExecute() override;
private:
    int pos;
    int len;
    ECTextDocument &doc;
};

// **********************************************************
// Controller for text document

class ECTextDocumentCtrl
{
public:
    ECTextDocumentCtrl(ECTextDocument &docIn);                              // conroller constructor takes the document as input
    virtual ~ECTextDocumentCtrl();
    void InsertTextAt(int pos, const std::vector<char> &listCharsToIns);    // insert a list of characters starting at position
    void RemoveTextAt(int pos, int lenToRemove);                            // remove a segment of characters  of lenToRemove starting from pos
    void CapTextAt(int pos, int lenToCap);                                  // Capitalize the text of lenToCap long starting from pos
    void LowerTextAt(int pos, int lenToLower);                              // Lowercase the text of lenToLoer starting from pos
    bool Undo();                                                            // undo any change you did to the text
    bool Redo();                                                            // redo the change to the text
    
private:
    // your code
    ECTextDocument &doc; 
    ECCommandHistory history;
};

// **********************************************************
// Document for text document

class ECTextDocument
{
public:
    ECTextDocument();
    virtual ~ECTextDocument();
    ECTextDocumentCtrl &GetCtrl();          // return document controller
    int GetDocLen() const { return listChars.size(); }
    char GetCharAt(int pos) const;          // get char at current position
    void InsertCharAt(int pos, char ch);    // insert a single char at position
    void RemoveCharAt(int pos);             // erase a single char at position
    void CapCharAt(int pos);                // capitalize the char at position
    void LowerCharAt(int pos);              // lowercase the char at position
    
private:
    // your code
    std::vector<char> listChars;
    ECTextDocumentCtrl *docCtrl;
};

#endif /* ECTextDocument_h */
