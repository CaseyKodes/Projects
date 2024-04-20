# CW 1-26

def factorial(x):
    if not isinstance(x,int):
        raise TypeError(f"cannot calculate factorial of type {x.__class__}")
    product = 1 
    while x > 1:
        product *=x
        x -= 1
    return product

# Unit test 1 - expected input 
assert factorial(5) == 120
assert factorial(6) == 720

# edge case - 0
assert factorial(0) == 1

# edge case - unexpected types
# how do i catch an exception 
'''try :
    factorial (2.3)
    raise AssertionError("factorial of 2.3 did not raise a type error")
except TypeError:
    pass
'''

# use tdd to write funciton sum_k
# returns some of the first k possitive integers 

def sumK(x):
    if not isinstance(x,int):
        raise TypeError(f"cannot calculate sum of type {x.__class__}")
    tsum = 0
    while x > 0:
        tsum += x
        x -= 1
    return tsum

assert sumK(2) == 3 
assert sumK(4) == 10

