import random
print('Tic Tac Toe')
print("X => Player ; O => Computer")

board_game = [' ' for i in range(10)]

# print(board)
def winningBoard(brd , pce):
    return ((brd[1] == pce and brd[2] == pce and brd[3] == pce )or 
            (brd[4] == pce and brd[5] == pce and brd[6] == pce )or 
            (brd[7] == pce and brd[8] == pce and brd[9] == pce )or
            (brd[1] == pce and brd[5] == pce and brd[9] == pce )or
            (brd[3] == pce and brd[5] == pce and brd[7] == pce )or
            (brd[1] == pce and brd[4] == pce and brd[7] == pce )or
            (brd[2] == pce and brd[5] == pce and brd[8] == pce )or
            (brd[3] == pce and brd[6] == pce and brd[9] == pce )
            )


def draw_board(board):
    print('     |     |     ')
    print(' ',board[1],' | ',board[2],' | ',board[3],' ')
    print('     |     |     ')
    print('------------------')
    print('     |     |     ')
    print(' ',board[4],' | ',board[5],' | ',board[6],' ')
    print('     |     |     ')
    print('------------------')
    print('     |     |     ')
    print(' ',board[7],' | ',board[8],' | ',board[9],' ')
    print('     |     |     ')
    print()
    print('--------------------------------')

def check_fullBoard(board):
    count = 0
    for i in board:
        if i == ' ':
            count += count
    
    if count > 0:
        return True
    else:
        return False

    # pass

def get_user_input(board):
    # pass
    try:
        x = input('Where do you wanna play next:? (fill from 1 to 9 location):')
        x = abs(int(x))
    except:
        print('Try inputing ')

    if (0 < x < 10):
        # x = input('Position is already filled try again? (fill from 1 to 9 location):')
        if (board[x] != ' '):
            x = input('Position is already filled try again? (fill from 1 to 9 location):')
            
        else:
            print("Please input your move from 1 to 9:")
            board[x] = 'X'
            return x
    else:
        get_user_input(board)

def Comp_move():
    print('Computer moves now:')
    possible_move = [ x for x, letter in enumerate(board_game) if letter == ' ' and x!=0 ]
    move = 0
    # print(possible_move)
    for let in ['O', 'X']:
        for i in possible_move:
            # print(let)
            board_temp = board_game[:]
            board_temp[i] = let
            if winningBoard(board_temp, let):
                move = i
                return move
    
    corners = []
    for i in possible_move:
        if i in [1,3,7,9]:
            corners.append(i)
    
    if len(corners) > 0:
        move = generateRandom(corners)
        return move
    
    if 5 in possible_move:
        move = 5
        return move
    
    edges = []
    for i in possible_move:
        if i in [2,4,6,8]:
            edges.append(i)
    
    if len(edges) > 0:
        move = generateRandom(edges)
        return move
    
    return move
    
def generateRandom(pos_mov_list):
    ln_list = len(pos_mov_list)
    rand_no = random.randrange(0,ln_list)
    return pos_mov_list[rand_no]

def main():
    print('Welcome To Tic-Tac-Toe:  ')
    draw_board(board_game)
    # board_game[4] = 'X'
    # board_game[1] = 'X'
    # board_game[4] = 'X'
    # board_game[7] = 'X'
    x = check_fullBoard(board_game)
    
    while(check_fullBoard(board_game)!= True):
        # print(x)
        if not (winningBoard(board_game,'O') ):
            # board_game[4] = 'O'
            
            get_user_input(board_game)
            draw_board(board_game)
            
            
        else:
            print("Sorry 'O' Won")
            break
        if not (winningBoard(board_game,'X') ):
            move = Comp_move()
            if move == 0:
                print('Tie Game')
                break
            else:

                
                # board_game[4] = 'X'
                # Comp_move()
                board_game[move] = 'O'
                print("Computer Placed \'O\' in position ",move)
                draw_board(board_game)

        else:
            print("Congratulations 'X' Won")
            break

    if (check_fullBoard(board_game) == True):
        print('board is full')

        



    
   
    

main()