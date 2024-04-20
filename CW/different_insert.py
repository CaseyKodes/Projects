# different_insert


def insertionsortLast(L): # sorts the last objects first 
    n = len(L)
    for i in range(n):
        j = n - i - 1
        while j < n - 1 and L[j]>L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            j+=1
        print(L)

def insertionFirst(L): # sorts the first objects first
    n = len(L)
    k = 0
    for i in range(n):
        for j in range(0, k):
            if L[j]>L[k]:
                L[j], L[k] = L[k], L[j]
        print(L)
        k+=1

if __name__ == '__main__':
    print()
    test = [4,2,76,2,998,3,5,76,78,0,2,1,7,34]
    print(test)
    print()
    insertionFirst(test)
    print()
    print("-"*40)
    test = [4,2,76,2,998,3,5,76,78,0,2,1,7,34]
    print(test)
    print()
    insertionsortLast(test)