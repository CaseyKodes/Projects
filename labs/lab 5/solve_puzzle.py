# solve_puzzle

def solve_puzzle(board, i = 0, visited = None): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    if visited == None:
        visited = set()
    
    # Base case: have you found a valid solution?
    if i == len(board)-1:
        return True
    # have we visited a position before
    elif i in visited:
        return False
    
    visited.add(i)
    
    # compute next moves
    move = board[i]
    lmove = (i-move)%len(board)
    rmove = (i+move)%len(board)

    # Recursively explore next-steps, returning True if any valid solution is found
    lresult = solve_puzzle(board, lmove, visited)
    rresult = solve_puzzle(board, rmove, visited)

    return lresult or rresult

if __name__ == '__main__':
    print(solve_puzzle([3,6,4,1,3,4,2,0]))
    print(solve_puzzle([3,4,1,2,0]))
    

    '''
    moves foward/back the number of indexes at the idex equal
    to the vlaue in the first item in the list 
    repeats until at index -1
    '''