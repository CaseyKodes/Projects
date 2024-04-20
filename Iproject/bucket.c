#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

int Max(int list[], int length)
{
  int maximum = list[0];
  for (int i = 1; i < length; i++)
    if (list[i] > maximum)
      maximum = list[i];
  return maximum;
}

void display_Array(int list[], int length)
{
  for (int i = 0; i < length; ++i)
  {
    printf("%d ", list[i]);
  }
  printf("\n");
}

void bucketSortAlgorithm(int list[], int length)
{
  const int maximum = Max(list, length);
  int bucket[maximum];
  for (int i = 0; i <= maximum; i++)
  {
    bucket[i] = 0;
  }
  for (int i = 0; i < length; i++)
  {
    int toadd = list[i];
    bucket[toadd]++;
  }
  for (int i = 0, j = 0; i <= maximum; i++)
  {
    while (bucket[i] > 0)
    {
      list[j] = i;
      bucket[i]--;
      j++;
    }
  }
}

int main()
{
  int elements[] = {3,2,9,5,5,6};
  printf("Before sorting in ascending order: \n");
  int length = sizeof(elements) / sizeof(elements[0]);
  display_Array(elements, length);
  bucketSortAlgorithm(elements, length);
  printf("\nAfter sorting in ascending order: \n");
  display_Array(elements, length);
}