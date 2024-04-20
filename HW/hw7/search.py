def search(A, low, high):
    mid = (low+high)//2
    if (A[mid] == mid):
        return mid
    if (A[mid] < mid):
        # move left
        search(A, mid+1, high)
    if (A[mid] > mid):
        # move right 
        search(A, low, mid-1)


if __name__=="__main__":
    array = [-1,0,1,3,5,6,8]
    print(f"Actual output   = {search(array, 0, len(array))}")
    print(f"Expected output = 3")