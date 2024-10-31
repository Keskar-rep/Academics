# N-Queens Problem

# Function to print the board

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Function to check if a queen can be placed on board[row][col]

def is_safe(board, row, col):
   
    # Check the column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if j < 0:
            break
        if board[i][j] == 'Q':
            return False

    # Check the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if j >= len(board):
            break
        if board[i][j] == 'Q':
            return False

    return True

# Function for backtracking to solve the N-Queens problem.

def solve_n_queens(board, row):
    
    if row >= len(board):
        print_board(board)  
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            
            # Place the queen
            board[row][col] = 'Q'  
            
            # Recur to place the next queen
            solve_n_queens(board, row + 1)  

            # Backtrack (remove the queen)
            board[row][col] = '.'  

# Function to implement N-Queens Problem

def n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]  # Create an N x N board
    solve_n_queens(board, 0)

if __name__ == "__main__":
    n = int(input("Enter the number of queens (N): "))
    n_queens(n)
