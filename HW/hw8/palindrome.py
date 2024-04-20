def PSL(input):
    n = len(input)
    Rinput = input[::-1]   
    table = [[0]*(n+1)]*(n+1)

    for i in range(1,n+1):
        for j in range(1,n+1):
            if(input[i-1] == Rinput[j-1]):
                table[i][j] = table[i-1][j-1]+1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    
    return table [n][n]

if __name__ == "__main__":
    toinput = 'character'
    print(PSL(toinput))
