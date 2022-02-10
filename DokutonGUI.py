# pyGUI.py
import pygame
from dokusan import generators
import random
import numpy as np
from python_sudoku import valid_num
pygame.font.init()
import time


board = np.array(list(str(generators.random_sudoku(avg_rank=random.randint(150,450)))))
board = [int(i) for i in board]
board = np.array(board)
board = board.reshape(9,9)
comp_board = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
solved = 0

WIDTH = 550
background_color = (251, 247, 245)
og_element_color = (0,0,0)
buffer = 5

def isEmpty(val):
    if (val == 0):
        return True
    return False

def sudoku_solver(win):
    
    bo_font = pygame.font.SysFont('Verdana', 35)
    for i in range(0, len(board[0])):
        for j in range(0, len(board[0])):
            if (isEmpty(board[i][j])):
                for k in range(1, 10):
                    if valid_num(board, (i, j), k):
                        board[i][j] = k
                        value = bo_font.render(str(k), True, (47, 97, 61))
                        win.blit(value, (((j + 1)* 50 + 15, (i + 1)* 50)))
                        pygame.display.update()
                        pygame.time.delay(2)

                        sudoku_solver(win)
                        global solved
                        if(solved == 1):
                            return
                        
                        board[i][j] = 0
                        pygame.draw.rect(win, background_color, ((j+1)* 50 + buffer, (i + 1)* 50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                        pygame.display.update() 

                return
    solved = 1



def insert_num(win, position):
    x,y = position[1], position[0]
    bo_font = pygame.font.SysFont('Verdana', 35)
    print("Input")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if(comp_board[x - 1][y - 1] != 0):
                    return
                if(event.key == 48): # 48 is 0 in ASCII
                    board[x -1][y - 1] = event.key - 48
                    # 5 is the buffer to prevent board discoloration
                    pygame.draw.rect(win, background_color, (position[0]* 50 + buffer, position[1]* 50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    pygame.display.update()

                if(0 < event.key - 48 < 10): # Checking for valid input
                    pygame.draw.rect(win, background_color, (position[0]* 50 + buffer, position[1]* 50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    value = bo_font.render(str(event.key - 48), True, (50, 168, 82))
                    win.blit(value, (position[0]* 50 + 15, position[1]* 50))
                    board[x - 1][y - 1] = event.key - 48
                    pygame.display.update()
                    return
                return 
            
def format_time(secs):
    sec = secs % 60
    minute = secs//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku with Backtracking Algorithm")
    win.fill(background_color)
    bo_font = pygame.font.SysFont('Verdana', 35)
    
    for i in range(0, 10):
        if (i % 3 == 0):
            pygame.draw.line(win, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        
        pygame.draw.line(win, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    
    pygame.display.update()

    for i in range(0, len(board[0])):
        for j in range(0, len(board[0])):
            if(0 < board[i][j] < 10):
                value = bo_font.render(str(board[i][j]), True, og_element_color)
                # j traverses the inner array of our sudoku board
                # j is horizontal, i is vertical
                win.blit(value,((j + 1)* 50 + 15, (i + 1)* 50))

    pygame.display.update()
    sudoku_solver(win)
    while True:
        for event in pygame.event.get():
            # Uncomment ths for insert functionality

            # if event.type == pygame.MOUSEBUTTONUP and (event.button == 1):
            #     pos = pygame.mouse.get_pos()
            #     insert_num(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return

start_time = time.time()
main()
print("Elapsed Time in seconds: ", round(time.time() - start_time))