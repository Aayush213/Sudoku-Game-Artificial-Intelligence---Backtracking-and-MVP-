#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pygame
from sudoku import Sudoku


print("Welcome To sudoku")
print("Project by Pranjal, Ayush, Santosh, Shriya")


# In[3]:


WIDTH = 550
background_color = (251,247,245)
original_grid_element_color = (52, 31, 151)
buffer = 5


# In[ ]:





# In[ ]:


puzzle = Sudoku(3).difficulty(0.6)
board = puzzle.board
board
for row in range (0,9):    
        board[row] = [0 if val is None else val for val in board[row]]

# board = [[0, 9, 0, 1, 4, 0, 2, 0, 7],
#         [0, 5, 4, 0, 0, 8, 0, 0, 3],
#         [2, 6, 7, 3, 5, 9, 4, 1, 8],
#         [0, 4, 6, 0, 2, 7, 0, 3, 9],
#         [0, 0, 9, 0, 6, 3, 0, 2, 5],
#         [8, 0, 0, 0, 1, 5, 7, 0, 6],
#         [0, 0, 3, 7, 0, 1, 5, 6, 2],
#         [0, 2, 5, 0, 8, 0, 0, 0, 1],
#         [0, 7, 1, 0, 0, 0, 9, 8, 4]]


# In[54]:


# grid = response.json()['board']


# In[55]:


grid = board


# In[56]:


grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]


# In[57]:


def isEmpty(num):
    if num == 0:
        return True
    return False


# In[13]:


def isValid(position, num):
     #Check for Column, row and sub-grid
    
    #Checking row
    for i in range(0, len(grid[0])):
        if(grid[position[0]][i] == num):
            return False
    
    #Checking column
    for i in range(0, len(grid[0])):
        if(grid[i][position[1]] == num):
            return False
    
    #Check sub-grid  
    x = position[0]//3*3
    y = position[1]//3*3
    #Gives us the box number
    
    for i in range(0,3):
        for j in range(0,3):
            if(grid[x+i][y+j]== num):
                return False
    return True


# In[14]:
# Sudoku Solver With Back tracking will change name of functions later

solved = 0
def sudoku_solver(win):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 0:  # Find an empty cell
                for k in range(1, 10):  # Try all numbers from 1 to 9
                    if isValid((i, j), k):
                        grid[i][j] = k
                        draw_number(win, i, j, k, myfont)  # Draw the number on the grid
                        pygame.display.update()

                        if sudoku_solver(win):  # Continue with next empty cell
                            return True
                        grid[i][j] = 0  # Backtrack
                        erase_number(win, i, j, myfont)  # Erase the number from the grid
                return False  # Trigger backtracking if no number fits in this cell
    return True  # Puzzle solved

def draw_number(win, row, col, number, font):
    pygame.draw.rect(win, background_color, ((col + 1) * 50 + buffer, (row + 1) * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
    value = font.render(str(number), True, (0, 0, 0))
    win.blit(value, ((col + 1) * 50 + 15, (row + 1) * 50))

def erase_number(win, row, col, font):
    pygame.draw.rect(win, background_color, ((col + 1) * 50 + buffer, (row + 1) * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
    pygame.display.update()
    pygame.time.delay(20)



# In[58]:


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
            
    sudoku_solver(win)
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return



# In[60]:


main()


# In[53]:

### Can make it Multiple Boards with fixed complexity to check the performance
puzzle = Sudoku(3).difficulty(0.2)
board = puzzle.board
board
for row in range (0,9):    
        board[row] = [0 if val is None else val for val in board[row]]
