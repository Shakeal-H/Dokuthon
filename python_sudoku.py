from dokusan import generators, renderers, solvers
import random
import numpy as np

# A sodoku generator and solver using dokusan and np, inspired by techwithtim

board = np.array(list(str(generators.random_sudoku(avg_rank=random.randint(150,450)))))
board = board.reshape(9,9)

alt_board = generators.random_sudoku(avg_rank=random.randint(150,450))

def print_fancier_board(sudoku):
    return print(renderers.colorful(sudoku))

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

print_board(board)
print_fancier_board(alt_board)