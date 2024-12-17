/* to build: gcc ECReverseLinkedList.cpp ECReverseLinkedListTest.cpp -o test  */
#include "ECReverseLinkedList.h"
#include <stdio.h>
#include <stdlib.h>

/* Test: get length of linked list */
void Test1()
{
  printf("**** Test1\n");
  struct ECLinkedListNode *p1, *p2, *p3, *ph;
  p1 = (struct ECLinkedListNode *)malloc(sizeof(struct ECLinkedListNode) );
  p2 = (struct ECLinkedListNode *)malloc(sizeof(struct ECLinkedListNode) );
  p3 = (struct ECLinkedListNode *)malloc(sizeof(struct ECLinkedListNode) );
  p1->value = 1;
  p1->pNext = p2;
  p2->value = 2;
  p2->pNext = p3;
  p3->value = 3;
  p3->pNext = NULL;

  /* Reverse */
  ph = ECReverseLinkedList(p1);

  /* should be 3 */
  printf("Head: %d\n", ph->value  );
  /* should be 2 */
  ph = ph->pNext;
  printf("Middle: %d\n", ph->value  );
  /* should be 1 */
  ph = ph->pNext;
  printf("Last: %d\n", ph->value  );
}

void Test2()
{
  printf("**** Test2\n");
  struct ECLinkedListNode *p1, *ph;
  p1 = (struct ECLinkedListNode *)malloc(sizeof(struct ECLinkedListNode) );
  p1->value = 1;
  p1->pNext = NULL;

  /* Reverse */
  ph = ECReverseLinkedList(p1);

  /* should be 1 */
  printf("Head: %d\n", ph->value  );
}

int main()
{
  Test1();
  Test2();
}


