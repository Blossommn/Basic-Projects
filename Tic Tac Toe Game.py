#!/usr/bin/env python
# coding: utf-8

# In[1]:


player1 = input("Please pick a marker 'X' or 'O'")


# In[2]:


position = int(input('Please enter a number'))


# In[3]:


from IPython.display import clear_output
clear_output()


# In[4]:


print('\n' * 100)


# In[67]:


from IPython.display import clear_output

def display_board(board):
    
    
    print("   |   |")
    print(" " + board[1]+ " | "+board[2]+" | "+board[3])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4]+ " | "+board[5]+" | "+board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[7]+ " | "+board[8]+" | "+board[9])
    print("   |   |")    


# In[68]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[69]:


def player_input():
    marker = ''
    
    while not (marker =='X' or marker == 'O'):
        marker = input('Plater 1: Do you want to be X or O? ').upper()
        
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


# In[70]:


player_input()


# In[71]:


def place_marker(board, marker, position):

    board[position] = marker


# In[74]:


place_marker(test_board,'$',2)
display_board(test_board)


# In[75]:


def win_check(board, mark):
    return (
        #Horizontal Line
        (board[1]== mark and board [2] == mark and board[3] == mark) or
        (board[4]== mark and board [5] == mark and board[6] == mark) or
        (board[7]== mark and board [8] == mark and board[9] == mark) or
        #Vertical
        (board[1]== mark and board [4] == mark and board[7] == mark) or
        (board[2]== mark and board [5] == mark and board[8] == mark) or
        (board[3]== mark and board [6] == mark and board[9] == mark) or
        # Diagonal
        (board[1]== mark and board [5] == mark and board[9] == mark) or
        (board[3]== mark and board [5] == mark and board[7] == mark) 
    )


# In[78]:


win_check(test_board,"O")


# In[85]:


import random

def choose_first():
    
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[86]:


def space_check(board,position):
    
    return board[position] == ' '


# In[87]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[88]:


def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[89]:


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[90]:


print("Welcome to Tic Tac Toe!")

while True:
    #Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            #Player 1's turn
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            #Player 2's turn
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
                    
    if not replay():
        break


# In[ ]:




