# coins 

def greedy_fewest_coins(amt, coins):
    coins.sort(reverse=True)
    numcoins = 0 
    for coin in coins:
        numcoins = amt//coin # floor division sign
        amt = amt%coin # removes second number from first number until it can not anymore
    return numcoins

    
'''
def fewcoin(amt,coins):
    if amt in coins:
        return 1
    mincoins = amt
    for coin in coins:
        if coin < amt:
            pathopt = 1+fewcoin(amt-coin,coins)
        if pathopt < mincoins:
            mincoins = pathopt
'''


print(greedy_fewest_coins(77, [1]))
print(greedy_fewest_coins(80, [1]))
print(greedy_fewest_coins(63,[1,21,25]))

'''
print(fewcoin(77, [1]))
print(fewcoin(80, [1]))
print(fewcoin(63,[1,21,25]))
'''


#TODO: add dictionary of solved subproblems to parameters
#TODO: update recrusive calls to pass that dictionary
#TODO: check against dictionary before making moves
#TODO: modify base case to use dictionary

def recr_fewest_coins(amt, coins, passed = None):
    # base case - amt is one of my coins
    if amt in passed: return passed[amt]

    # initalize dictionary 
    if passed == None:
        passed = {coin:1 for coin in coins}
        
    #  Initialize "worst case optimum"
    min_coins = amt 

    # Find all valid next steps
    valid_coins = [coin for coin in coins if coin<=amt]

    # explore all next steps, keeping tack of best solution
    for coin in valid_coins:
        if amt-coin not in passed:
            path_optimum = 1 + recr_fewest_coins(amt-coin, coins, passed)
        
            if path_optimum < min_coins:
                min_coins = path_optimum

    # AFTER the for loop, return the optimal solutio
    passed[amt] = min_coins
    return min_coins

print(recr_fewest_coins(77, [1]))
print(recr_fewest_coins(80, [1]))
print(recr_fewest_coins(63,[1,21,25]))


def dynamicfewcoins(amt, coins):
    solved = [None]*(amt+1)

    for prob in solved:
        solved[prob] = prob
        for coin in coins:
            if coins <= prob:
                potmin = 1 + solved[prob-coin]
                if potmin < solved[min]:
                    solved[min] = potmin
                    
    return solved[amt]
