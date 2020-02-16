global N 
N = 4 
def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print board[i][j], 
        print
def isSafe(board, row, col): 
    for i in range(col): 
        if board[row][i] == 1: 
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True