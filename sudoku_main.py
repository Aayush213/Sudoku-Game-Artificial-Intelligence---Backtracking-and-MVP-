#!/usr/bin/env python
# coding: utf-8
#### imports for the game
import pygame
from sudoku import Sudoku
import time

print("Welcome To sudoku")
print("Project by Pranjal, Ayush, Santosh, Shriya")

#### Setting up parameters for board
WIDTH = 550
background_color = (251,247,245)
original_grid_element_color = (52, 31, 151)
buffer = 5

#### Board Generation 
puzzle = Sudoku(3).difficulty(0.9)
board = puzzle.board
board
for row in range (0,9):    
        board[row] = [0 if val is None else val for val in board[row]]
print(board)
# In[54]:
# easy_board = [[0, 0, 6, 0, 0, 0, 3, 0, 0], 
#          [2, 0, 8, 0, 0, 6, 0, 9, 0], 
#          [0, 0, 5, 0, 0, 0, 4, 0, 7], 
#          [0, 7, 0, 6, 3, 0, 0, 5, 9], 
#          [0, 6, 0, 0, 0, 0, 2, 0, 3], 
#          [8, 1, 0, 0, 9, 0, 0, 0, 4], 
#          [9, 5, 0, 0, 2, 0, 8, 1, 0], 
#          [0, 0, 0, 8, 6, 0, 0, 0, 5], 
#          [6, 0, 0, 9, 1, 0, 0, 0, 2]]

difficult_board = [[0, 0, 0, 0, 0, 0, 0, 0, 8], 
                   [0, 4, 0, 0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 3, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 2], 
                   [0, 0, 0, 0, 0, 0, 6, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 1, 0], 
                   [6, 0, 0, 1, 0, 5, 0, 0, 0]]

board = difficult_board
grid = board
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
def isEmpty(num):
    if num == 0:
        return True
    return False

def isValid(position, num):         
    for i in range(0, len(grid[0])):
        if(grid[position[0]][i] == num):
            return False
    
    for i in range(0, len(grid[0])):
        if(grid[i][position[1]] == num):
            return False
    
    x = position[0]//3*3
    y = position[1]//3*3
    
    for i in range(0,3):
        for j in range(0,3):
            if(grid[x+i][y+j]== num):
                return False
    return True

solved = 0
def sudoku_solver_backtracking(win):
    global solved, iterations, start_time
    if 'start_time' not in globals():
        start_time = time.time()
    if 'iterations' not in globals():
        iterations = 0

    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if isEmpty(grid[i][j]): 
                for k in range(1, 10):
                    if isValid((i, j), k):
                        grid[i][j] = k
                        iterations += 1
                        pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer, 50 - 2*buffer, 50 - 2*buffer))
                        value = myfont.render(str(k), True, (0,0,0))
                        win.blit(value, ((j+1)*50 + 15, (i+1)*50))
                        pygame.display.update()
                        pygame.time.delay(25)
                        
                        sudoku_solver_backtracking(win)
                        
                        if solved == 1:
                            return

                        grid[i][j] = 0
                        pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer, 50 - 2*buffer, 50 - 2*buffer))
                        pygame.display.update()
                return
    solved = 1
    print("Time taken:", time.time() - start_time, "seconds")
    print("Iterations (memory footprint):", iterations)


def sudoku_solver_bruteforce(win):
    global iterations, start_time
    if 'start_time' not in globals():
        start_time = time.time()
    if 'iterations' not in globals():
        iterations = 0

    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if isEmpty(grid[i][j]):
                for k in range(1, 10):
                    if isValid((i, j), k):
                        grid[i][j] = k
                        iterations += 1
                        pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer, 50 - 2*buffer, 50 - 2*buffer))
                        value = myfont.render(str(k), True, (0, 0, 0))
                        win.blit(value, ((j+1)*50 + 15, (i+1)*50))
                        pygame.display.update()
                        pygame.time.delay(25)

                        if sudoku_solver_bruteforce(win):
                            return True

                        grid[i][j] = 0
                        pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer, 50 - 2*buffer, 50 - 2*buffer))
                        pygame.display.update()
                return False
    
    print("Time taken:", time.time() - start_time, "seconds")
    print("Iterations (memory footprint):", iterations)
    return True

def find_mrv_cell(grid):
    min_options = 10 
    mrv_cell = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if isEmpty(grid[i][j]):
                num_options = 0
                for num in range(1, 10):
                    if isValid((i, j), num):
                        num_options += 1
                if num_options < min_options:
                    min_options = num_options
                    mrv_cell = (i, j)
    return mrv_cell


def sudoku_solver_mrv(win):
    global solved, iterations, start_time
    if 'start_time' not in globals():
        start_time = time.time()
    if 'iterations' not in globals():
        iterations = 0

    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    mrv_cell = find_mrv_cell(grid)
    if mrv_cell is None:
        solved = 1
        print("Time taken:", time.time() - start_time, "seconds")
        print("Iterations (memory footprint):", iterations)
        return True

    i, j = mrv_cell
    for k in range(1, 10):
        if isValid((i, j), k):
            grid[i][j] = k
            iterations += 1
            pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer, 50 - 2*buffer, 50 - 2*buffer))
            value = myfont.render(str(k), True, (0, 0, 0))
            win.blit(value, ((j+1)*50 + 15, (i+1)*50))
            pygame.display.update()
            pygame.time.delay(25)

            if sudoku_solver_mrv(win):
                return True

            grid[i][j] = 0
            pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer, 50 - 2*buffer, 50 - 2*buffer))
            pygame.display.update()

    return False

def main():    
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    
    for i in range(0,10):
        if(i%3 == 0):
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()
    
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()
    algo = int(input("which algorithm you want to run/n 1. Backtracking /n 2.Bruteforce /n 3. MRV ") )       
    if(algo == 1):
        sudoku_solver_backtracking(win)
    elif (algo == 2):
        sudoku_solver_bruteforce(win)
    elif (algo == 3):
        sudoku_solver_mrv(win)


    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()
