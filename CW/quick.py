# quick
import random

def quicksort(L, left = 0, right = None): 
    print(L)

    if right is None: 
        right = len(L)
    if right - left <= 1:
        return None

    pivot = right-1
    print(L[pivot])
    i, j = left, right-2

    while i<j:
        while L[i] < L[pivot]:
            i+=1
        while L[j] >= L[pivot] and i<j:
            j-= 1
        if i<j:
            L[i], L[j] = L[j], L[i]
    if L[i] >= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    
    quicksort(L, left, pivot)
    quicksort (L, pivot+1, right)


if __name__ == '__main__':

    '''sorted = [1,2,3,4,5,6,7,8,9]
    quicksort(sorted)
    print('-'*40)
    backwards = [9,8,7,6,5,4,3,2,1]
    quicksort(backwards)
    print('-'*40)'''

    for i in range(3):
        print(i)
        print()
        ran = [random.randint(0, 100) for i in range(10)]
        quicksort(ran)
        print("-"*40)
