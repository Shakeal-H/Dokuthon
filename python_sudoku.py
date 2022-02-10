from dokusan import generators, renderers, solvers
import random
import numpy as np
from pyrsistent import b

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


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------------------------")

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
                # Row and column of empty cell
                return (i, j)  

    return None

def valid_num(board, position, num):
    row = position[0]
    col = position[1]

    for j in range(0, 9):
        if board[row][j] == num:
            return False

    for i in range(0, 9):
        if board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid_num(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False