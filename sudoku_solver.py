import numpy as np

# Sample board
# This board can be taken as input
# Enter 0 for empty cells
board = np.array([
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]

])

print("The unsolved board:\n")
print(board)
print("\n")

def find_empty(board):
    
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return [i,j]
    return None
            
def valid(board,num,pos):
    
    # checking Row
    for i in range(9):
        if board[pos[0]][i]==num and i!=pos[1]:
            return False
        
    # checking Column
    for i in range(9):
        if board[i][pos[1]]==num and i!=pos[0]:
            return False
        
    # Checking boxes
    x_box = pos[1]//3
    y_box= pos[0]//3
    
    for i in range(y_box*3, y_box*3+3):
        for j in range(x_box*3, x_box*3+3):
            if board[i][j]==num and [i,j]!=pos:
                return False      
            
    return True

def solve(board):
    
    find = find_empty(board)
    
    if not find:
        return True
    
    else:     
        row ,col =  find  
    
    for m in range(1,10):
        
        if valid(board,m, [row,col]):
            board[row][col]=m
            
            if solve(board):
                return True
            board[row][col]=0
            
    return False

solve(board)

print("The solved board:\n")
print(board)
