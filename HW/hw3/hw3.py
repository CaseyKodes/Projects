# hw 3

import time 


'''
takes in a list of integers and a traget value, 
itterates thorugh the list and finds integer pairs that equal target value
'''
def findPairNaive(first, target):

    pairs = set()                                       # 1

    for num1 in first:                                  # n*

        for num2 in first:                              #   n*  

            if (num1+num2==target) and (num1<num2):     #       1x/2x/3x/4x     can be 1-4 calls depending on hardware
                pairs.add((num1,num2))                  #                       2

    return pairs                                        # 1
                                                        #______________________________
                                                        # 1+n*n*2*2+1 = 4n^2+2 = O(n^2)
                                                        # this function takes an exponetially more amount of time as n increases


'''
same purpose as findPairNaive 
but faster
'''
def findPairOptimize(first, target): 
    # creates a set of the list input 
    # to eliminate similar values
    firstset = set(first)                                           # 1
    pairs = set()                                                   # 1
                                            
    for num1 in range(len(firstset)):                               # n*

        if ((target-num1) in firstset) and (num1<target-num1):      #   1x/2x/3x/4x/5x*     can 1-5 call depending on hardware
            pairs.add((num1,target-num1))                           #                   1x/2x   can be 1 or 2 calls depending on hardware

    return pairs                                                    # 1
                                                                    # ___________________________
                                                                    # 1+1+n(2(2))+1 = 10n+3 = O(n)
                                                                    # this function takes a linearly more amount of time as n increases


'''
measures the time needed to run 10 tests of both:
findPairNaive and findPairOptimize
uses a format string as output 
inputs a function and the arguments for that function
'''
def measureMinTime(fn, arg1):

    n = 10 # number of times that the function is tested
    mintime = float('inf')

    for i in range (n):

        start = time.time() 
        hold = fn(*arg1)
        end = time.time()  

        if end-start < mintime:
            mintime = end-start

    return mintime


# prints table of run times
if __name__ == '__main__':

    holder = "" # needed to make string formatting work
    print(f"{holder:<7}Time to run in ms")
    print(f" n{holder:<9}naive{holder:<8}optimize")
    print('='*33)

    for n in [10,50,100,250,500,1000,2500,5000]: # you can not see how long find pair optimzie is unless you run much larger values

        printlist = [i for i in range (n)]
        printtarget = n/2
        time_naive = 1000*measureMinTime(findPairNaive, (printlist,printtarget))
        time_optimize = 1000*measureMinTime(findPairOptimize, (printlist,printtarget))
        print (f" {n:<10}{time_naive:<13.4f}{time_optimize:.4f}")

    print ("-"*33)
    print ()
    print ("larger values of 'n' to show that")
    print ("findPairsOptimize is extremly fast")
    print ("findPairsNaive would take to long to run")
    print ()
    print(f" n{holder:<9}-----{holder:<8}optimize")
    print ('='*33)

    for n in [10000,20000,50000,100000,200000,500000]: 
        printlist = [i for i in range (n)]
        printtarget = n/2
        time_optimize = 1000*measureMinTime(findPairOptimize, (printlist,printtarget))
        print (f" {n:<10}--------{holder:<5}{time_optimize:.4f}")
    print('-'*33)
