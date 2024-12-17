#include "ECReverseLinkedList.h"
#include <stdio.h>
#include <stdlib.h>

/* Reverse the given linked list */
/* pHead: head node pointer to the linked list */
/* return the head of the reversed linked list */
/* note: don't allocate any new space using malloc; you should be able to reverse the linked list by just changing the pointers */
struct ECLinkedListNode* ECReverseLinkedList( struct ECLinkedListNode *pHead )
{
  /* Your code goes here */
  struct ECLinkedListNode *cur = pHead;
  struct ECLinkedListNode *next = NULL;
  struct ECLinkedListNode *prev = NULL;
  while (cur != NULL)
  {
    next = cur->pNext;
    cur->pNext = prev;
    prev = cur;
    cur = next;
  }
  return prev;
}