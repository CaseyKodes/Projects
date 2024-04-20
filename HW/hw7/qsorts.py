# first quicksort uses the last element as a pivot
def qsortLast(A, low, high):
    if (low < high):
        pivot = partition(A, low, high) # most of the work is done in here
        qsortLast(A, low, pivot-1)
        qsortLast(A, pivot+1, high)

# second qsort uses a random element as a pivot 
def qusortRandom(A, low, high):
    if (low < high):
        pivot = randpartition(A, low, high) # most of the work is done in here
        qusortRandom(A, low, pivot-1)
        qusortRandom(A, pivot+1, high)

def partition(L, i, j):
    pivot = j -1
    j = pivot -1
    while i < j : 
        #Pivot all items between left and right
        while L[i] < L[pivot]:
            i = i + 1
        while i<j and L[j] >= L[pivot]:
            j = j - 1
        if i < j:L[i], L[j] = L[j], L[i]
    #Swap pivot and i
    if L[i]>= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return pivot

def randpartition(A, low, high): 
    # works by just swaping a random element with the last element and then calling normal partition
    i = random.randint(low, high)
    temp = A[high]
    A[high] = A[i]
    A[i] = temp
    return partition(A, low, high)

# main 
if __name__ == "__main__":
    import time
    import random
    import sys
    sys.setrecursionlimit(10000)
    ranges = [100, 500, 1000, 1500, 2000]

    print("Sorted Tests time for quick sorts")
    for value in ranges:
        list1 = [i for i in range(value)] # use for first quick sort
        list2 = [j for j in range(value)] # use for second quick sort
        start = time.time()
        qsortLast(list1, 1, len(list1)-1)
        end = time.time()
        print(f"Pivot as the last element for size {value} total time was: {end-start}")
        start = time.time()
        qusortRandom(list2, 1, len(list2)-1)
        end = time.time()
        print(f"Pivot as a random element for size {value} total time was: {end-start}")
        
    print("\n\nReversed Tests time for quick sorts")
    for value in ranges:
        list1 = [i for i in range(value,0,-1)] # use for first quick sort
        list2 = [j for j in range(value,0,-1)] # use for second quick sort
        start = time.time()
        qsortLast(list1, 1, len(list1)-1)
        end = time.time()
        print(f"Pivot as the last element for size {value} total time was: {end-start}")
        start = time.time()
        qusortRandom(list2, 1, len(list2)-1)
        end = time.time()
        print(f"Pivot as a random element for size {value} total time was: {end-start}")

    print("\n\nUnsorted tests time for quick sorts")
    for value in ranges:
        list1 = random.sample(range(0, value), value)
        list2 = list1.copy() # list2 now has the same values as list1 but is an independent copy
        start = time.time()
        qsortLast(list1, 1, len(list1)-1)
        end = time.time()
        print(f"Pivot as the last element for size {value} total time was: {end-start}")
        start = time.time()
        qusortRandom(list2, 1, len(list2)-1)
        end = time.time()
        print(f"Pivot as a random element for size {value} total time was: {end-start}")
    