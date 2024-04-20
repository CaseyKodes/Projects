def numCombos(target, values):
    table = [0 for i in range(target+1)]
    table[0] = 1
    for move in values:
        for i in range(move, target+1):
            table[i] += table[i-move]
    return table[target]

if __name__ == "__main__":
    moves = [3,5,10]
    target = 20
    index = [i for i in range(target+1)]
    #print(index)
    print(numCombos(target, moves))