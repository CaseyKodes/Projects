# quick select 


def quickselect(L,k):
    '''
    finds the kth biggest item in an unsorted list L
    '''

    # find first biggest item 
    maxitem = L[0]
    penitem = min(L[0], L[1])
    for i in range (2,len(L)):
        if L[i] > maxitem:
            penitem = maxitem
            maxitem = L[i]
        elif L[i] > penitem:
            penitem = L[i]

    return maxitem
