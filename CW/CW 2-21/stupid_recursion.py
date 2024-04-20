# stupid recursion 

def sumk(k):
    tempsum = 0
    for i in range (1,k+1):
        tempsum+=k

    return tempsum

# sum(k) = k+k-1+k-2...+1
# sum(k) = k+sum(k-1)...+sum(1)

def sumkbad(k):
    if k == 1 or k == 0:
        return k
    else:
        return k+sum(k-1)

assert sumk(1)==1
assert sumk(0)==0
assert sumk(4)==10
assert sumkbad(1)==1
assert sumkbad(0)==0
assert sumkbad(4)==10

def fac(k):
    if k in {0,1}:
        return 1
    else:
        return k*fac(k-1)

assert fac(0)==1
assert fac(1)==1
assert fac(5)==125

def fib(k):
    if k in {1,2}:
        return 1
    else:
        return fib(k-1) + fib(k-2)

assert fib(1)==1
assert fib(2)==1
assert fib(3)==2
assert fib(4)==3
assert fib(5)==5
assert fib(6)==8

def fibsol(k, solved=None):
    if solved is None:
        solved = dict()
        solved[1]=1
        solved[2]=1
    if k in {1,2}:
        return 1
    if k in solved:
        return solved[k]
    solved[k]=fibsol(k-1, solved) + fib(k-2, solved)

assert fibsol(1)==1
assert fibsol(2)==1
assert fibsol(3)==2
assert fibsol(4)==3
assert fibsol(5)==5
assert fibsol(6)==8