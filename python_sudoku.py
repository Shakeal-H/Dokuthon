from dokusan import generators, renderers, solvers
import random
import numpy as np

# A sodoku generator and solver using dokusan and np, inspired by techwithtim

# Dokusan sodoku solver
alt_board = generators.random_sudoku(avg_rank=random.randint(150,450))

def print_fancier_board(sudoku):
    return print(renderers.colorful(sudoku))

def solve_sudoku(some_board):
    solution = solvers.backtrack(some_board)
    return print(renderers.colorful(solution))


# Create a sudoku board of random levels as an array of ints
board = np.array(list(str(generators.random_sudoku(avg_rank=random.randint(150,450)))))
board = [int(i) for i in board]
board = np.array(board)
board = board.reshape(9,9)



# Print the sudoku board from my array using dash(-) and pipe(|)
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

def valid(board, number, position):
    # Check the row of board
    for i in range(len(board[0])):
        if (board[position[0]][i] == number) and (position[1] != i):
            return False

    # Check the column of board
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check the box of board
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


# print_fancier_board(alt_board)
solve_sudoku(alt_board)

