import time

def time_function(func, arg, runNum = 10):
    """
    inputs a function and a argument to be used in that fuciont
    and returns the time that funciton takes to run
    """
    mintime = float('inf')

    for i in range(runNum):
        start = time.time()
        func(arg)
        end = time.time()
        runtime = end-start
        mintime = min(runtime, mintime)
        
    return mintime
    
def time_function_flexible(func, *arg, runNum = 10):
    """inputs tuple of multiple tests"""
    mintime = float('inf')

    for i in range(runNum):
        start = time.time()
        func(*arg)
        end = time.time()
        runtime = end-start
        mintime = min(runtime, mintime)
        
    return mintime

if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    L3 = (i for i in range(10**5))
    t3 = time_function_flexible(test_func, L3)

    L4 = (i for i in range(10**6)) # should be 10x slower to operate on every item
    t4 = time_function_flexible(test_func, L4)

    print("t(L1) = {:.3e} ms".format(t1*1000))
    print("t(L2) = {:.3e} ms".format(t2*1000))
    print("t(L3) = {:.3e} ms".format(t3*1000))
    print("t(L4) = {:.3e} ms".format(t4*1000))