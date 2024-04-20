# puzzle 


def solve_puzzle(board, idx=0, visited = None):
    
    # initialzie visited 
    if visited == None:
        visited = set()

    # update visited 
    visited.add(idx)

    # base case
    if idx == len(board)-1:
        return True

    # find all valid moves
    idx_cw = (idx + board[idx]) % len(board)
    idx_ccw = (idx - board[idx]) % len(board)

    validMoves = [idx_cw, idx_ccw]

    # for each valid move 
    for move in validMoves:
        if move in visited: continue

        pathopt = solve_puzzle(board, move, visited)
        if pathopt: return True

    return False 
    #   find omptium result for move 
    #   if thats better than current best, update 

    # return best choice 