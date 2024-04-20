# quicksort

import random, timeit, sys
def is_sorted(L): return not any(L[i] > L[i+1] for i in range(len(L)-1))

def quicksort(L, left = 0, right = None):
    "Sorts L in-place using quicksort"
    if right is None: 
        right = len(L)
    if right - left <= 1: 
        return
    median = partition (L, left, right)
    quicksort(L, left, median)
    quicksort(L, median+1, right)
    
def partition(L, left, right):
    """Partitions L[left:right] around L[right-1]
            Input
            -----
                L: list[int]
                    list of integers
                left: int
                    index of leftmost item to be considered
                right: int
                    index of rightmost item to be considered + 1
            Output
            ------
                pivot: int
                    index of the pivot element after partitioning (where L[right-1] ends up)
    """
    i = left 
    pivot = right -1
    j = right -2
    while  i < j:
        while L[i] < L[pivot]:
            i+=1
        while i < j and L[j] >= L[pivot]:
            j-=1
        if i < j:
            L[i], L[j] = L[j], L[i]
    if L[pivot] <= L[i]:
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i
    return pivot


def mergesort(L):
    "sorts L using mergesort"
    # base case
    if len(L) <= 1: return L
    
    # divide
    median = len(L) // 2
    Lleft = mergesort(L[:median])
    Lright = mergesort(L[median:])

    # conquer
    merge(L, Lleft, Lright)

    return L

def merge(L, Lleft, Lright):
    "merges sorted sublists Lleft and Lright into L"
    i, j = 0, 0
    while i < len(Lleft) and j < len(Lright):
        if Lleft[i] < Lright[j]:
            L[i+j] = Lleft[i]
            i += 1
        else:
            L[i+j] = Lright[j]
            j+=1

    L[i+j:] = Lleft[i:] + Lright[j:]
    
    return L

if __name__ == '__main__':
    # test our algs work
    n = 1000

    L = [random.randint(0, n) for i in range(n)]
    Lmerge = L[:]
    Lquick = L[:]

    mergesort(Lmerge)
    assert is_sorted(Lmerge)
    
    quicksort(Lquick)
    assert is_sorted(Lquick)
  
    """
    ### Times mergesort
    t_merge = 1000*timeit.timeit("mergesort(L)", setup=f"L={Lmerge}", globals=globals(), number=1) 
    print(f"t_merge: {t_merge:.3f} ms")
    print(f"max_depth = {max_depth}") 
    print()

    ### Times quicksort
    t_quick = 1000*timeit.timeit("quicksort(L)", setup=f"L={Lquick}", globals=globals(), number=1)
    print(f"t_quick: {t_quick:.3f} ms")
    print()
    """