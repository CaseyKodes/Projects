# real world sorting

def is_sorted(L): return not any(L[i] > L[i+1] for i in range(len(L)-1))

def merge(L, Lleft, Lright):
    "Merges sorted lists Lleft and Lright into L"
    counter1 = 0
    counter2 = 0
    while counter1 < len(Lleft) and counter2 < len(Lright):
        if Lleft[counter1] < Lright[counter2]:
            L[counter1+counter2] = Lleft[counter1]
            counter1+=1
        else:
            L[counter1+counter2] = Lright[counter2]
            counter2+=1
    L[counter1+counter2:] = Lleft[counter1:] + Lright[counter2:] 

def merge_sort(L):
    "Sorts L in-place using mergesort"
    ### Base Case ###
    if len(L) <= 1:
        return L

    ### Divide ###
    median = len(L)//2
    # Recursively sort left
    Lleft = merge_sort(L[:median])
    # Recursively sort right
    Lright = merge_sort(L[median:])

    ### Conquer ###
    # merge left and right lists
    merge(L, Lleft, Lright)
    return L

def bubble(L):
    "Sorts L in-place using bubblesort"
    for i in range(len(L)-1):
        keepgoing = False
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j] # swap
                keepgoing = True            # list is *not* sorted

        # terminate early if list is sorted
        if not keepgoing: break
        
if __name__ == '__main__':
    ### Part 1 - merge ###
    n = 10
    import random

    # Construct sorted sublists L1 and L2
    L1 = [random.randint(0, n) for i in range(n)]
    L2 = [random.randint(0, n) for i in range(n)]
    L1.sort()
    L2.sort()

    # Create an empty list big enough for L1 + L2
    L3 = [None for i in range(len(L1) + len(L2))]

    # Verify L3 is the merger of L1 and L2
    merge(L3, L1, L2)
    assert is_sorted(L3)

    ### Part 2 - mergesort ###
    n = 1000
    L = [random.randint(0, n) for i in range(n)]
    merge_sort(L)
    assert is_sorted(L)

    