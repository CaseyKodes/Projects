import math

# list to think about for each method
# sorted: [0,1,2,3,4,5,6,7]
# reversed: [8,7,6,5,4,3,2,1,0]
# random: [3,7,2,6,5,9,8,5,6]

def linear_scan(L): 
    n = len(L)
    unsortedcounter = 0 
    sortedcounter = 0
    for i in range(n-1):
        if L[i] >= L[i+1]: # updates counter if objects are in the wrong order or equal
            unsortedcounter += 1 
        if L[i] <= L[i+1]: # updates counter if objects are in the right order or equal
            sortedcounter += 1

# there are n-1 comparasions for a list of length n
    if sortedcounter == len(L)-1:
        # if this counter = len(list)-1 then every object is in place or equal to the object next to it therefor the list is sorted
        return "list is sorted"
    if unsortedcounter == len(L)-1: 
        # if this counter = len(list)-1 then every object is out of place or equal to the object next to it therefor the list is reversed 
        return "list is reversed"
    if unsortedcounter <= 5:
        # if this counter is <5 then insertion sort does the best job or sorting the list
        return "unsorted use insertion"
    if unsortedcounter > 5:
        # if this counter is >5 then quicksort does the best job of sorting the list
        return "unsorted use quicksort"

def reverse_list(L): 
    for i in range(len(L)//2):
        L[i] , L[-1-i] = L[-1-i], L[i] # switches the first and last objects that are out of order 

def insertionsort(L, left = 0, right = None): 
    # atribute to tell magic when this functions runs
    insertionsort.hasbeencalled = True 

    if right is None:
        right = len(L)

    n = right
    for i in range(left, n+1):
        j = n - i
        while j < n - 1 and L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            j += 1

def quicksort(L, left = 0, right = None, depth = 0, maxdepth = None): 
    # atribute to tell magic when this functions runs
    quicksort.hasbeencalled = True
    
    # if the max depth gets to big then the pivots were not effective
    if maxdepth is None:
        maxdepth = 2*(math.log2(len(L))+1)
    
    if depth > maxdepth:
        mergesort(L)
        return L

    if right is None: 
        right = len(L)
    if right - left <= 1:
        return None
    
    # if length of section to be sorted is <=16 then sorts list using insertionsort
    if right-left <= 16:
        insertionsort(L, left, right)
        #print (L) # to see what is going on 

    pivot = right-1
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
    
    #print (depth)
    quicksort(L, left, pivot, depth+1, maxdepth)
    quicksort (L, pivot+1, right, depth+1, maxdepth)
    
def mergesort(L): 
    # atribute to tell magic when this functions runs
    mergesort.hasbeencalled = True

    if len(L) <= 1:
        return L
    
    # if length of section to be sorted is <=16 then sorts list using insertionsort
    # i think this one works for using insertion within merge 
    if len(L) <= 16:
        # do not need to make a left and right parameter here becasue merge sort creates smaller lists by default
        insertionsort(L)
        return L

    median = len(L)//2
    left = L[:median]
    right = L[median:]
    left = mergesort(left)
    right = mergesort(right)

    i, j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i+j] = left[i]
            i +=1
        else:
            L[i+j] = right[j]
            j+=1
    L[i+j:] = left[i:] + right[j:]

    return L

def magic_sort(L): 
    actions = ["list is sorted","list is reversed","unsorted use insertion","unsorted use quicksort"]
    whattodo = linear_scan(L)

    # set all values that tell magic if the functions were run to false to make sure they have some value
    insertionsort.hasbeencalled = False
    quicksort.hasbeencalled = False
    mergesort.hasbeencalled = False

    # some simple base cases that are easy to deal with 
    if whattodo == actions[0]:
        return {}
    elif whattodo == actions[1]:
        reverse_list(L)
        return {'reverse_list'}
    elif whattodo == actions[2]:
        insertionsort(L)
        return {'insertionsort'}
    
    # main oart of magic sort uses quick sort and then if other functions are called from quick sort
    # the "hasbeencalled" varible changes for that function 
    else:
        quicksort(L)
        called = set()
        if insertionsort.hasbeencalled:
            called.add('insertionsort')
        if quicksort.hasbeencalled:
            called.add('quicksort')
        if mergesort.hasbeencalled:
            called.add('mergesort')
        return called
