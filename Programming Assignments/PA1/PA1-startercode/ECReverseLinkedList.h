#ifndef EC_REVERSE_LINKEDLIST_H
#define EC_REVERSE_LINKEDLIST_H

/* Define a (single) linked list node, which stores an integer */
struct ECLinkedListNode
{
  int value;                /* value held by the linked list */
  struct ECLinkedListNode *pNext;    /* pointer to the next node */ 
};

/* Reverse the given linked list */
/* pHead: head node pointer to the linked list */
/* return the head of the reversed linked list */
/* note: don't allocate any new space using malloc; you should be able to reverse the linked list by just changing the pointers */
struct ECLinkedListNode* ECReverseLinkedList( struct ECLinkedListNode *pHead );

#endif
