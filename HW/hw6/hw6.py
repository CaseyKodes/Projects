# TODO: implement the 4 functions (as always, include docstrings & comments)

def find_zero(L, mid = None): 
    n = len(L)
    for i in range(n):
        if L[i] == 0:
            return i
    raise TypeError("There is no 0 in this list")
    
# do not know why or how to use left and rigth values for sorts
# they might need to be used as where the sort fucntions iterate through each list
def bubble(L, left, right): 
    '''
    compares to adjacent items in a list to each other and switches their position if the bigger item comes at an erlier index
    sorts the largest item to the correct spot with each iteration through the list
    it is possible to jump out of the sort early if the list is already sorted by checking if a pair was never switched
    '''
    n = right-left
    for i in range(n+1):
        switches = 0 # variable to see if list is already sorted, can also be considered the adaptive variable
        for j in range(left,right-1):
            if L[j] > L[j+1]: 
                L[j], L[j+1] = L[j+1], L[j]
                switches += 1
        if switches == 0:
            return

def selection(L, left, right): 
    '''
    finds the index of the largest object then when at the end of the list switches the item at the end of the list with the largest object 
    not possible to jump out of sort if the list is already sorted 
    '''
    count = 0 # made so that when testing the positive half of the list once the biggest value is put into place oyu do not check the sorted indexes anymore
    for i in range(left, right):
        maxidx = left
        if left == 0: # sorts the negative half of the list works 
            for j in range (left, right-i+1):
                if L[maxidx] < L[j]:
                    maxidx = j 
            L[j], L[maxidx] = L[maxidx], L[j]
        else: # sorts the positive half of the list 
            for k in range (left, right-count):
                if L[maxidx] < L[k]:
                    maxidx = k 
            L[k], L[maxidx] = L[maxidx], L[k]
        count += 1

def insertion(L, left, right): 
    '''
    instead of sorting the largest objects frist it sorts the latest objects first 
    almost like creating a sorted list at the end of the full list as it iterates through
    '''
    n = right
    for i in range(n+1):
        j = n - i
        while j < n - 1 and L[j] > L[j+1]: # only runs if items are out of order therefor it is adaptive 
            L[j], L[j+1] = L[j+1], L[j]
            j += 1

def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, bubble)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''

    idx_zero = find_zero(L)     # find the 0 index 
    sort(L, 0, idx_zero)        # sort left half
    sort(L, idx_zero+1, len(L)) # sort right half