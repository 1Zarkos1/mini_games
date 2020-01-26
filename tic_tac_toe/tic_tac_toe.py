import random
import logging

logging.basicConfig(level='DEBUG')

def play_game():

    board = [' '] * 9
    player_turn = 1
    end = ''
    available_boxes = [i for i, k in enumerate(board) if k == " "]

    while available_boxes and not end:
        
        if player_turn:
            choice = input('Your sign is "x". Choose a number from 1 to 9. (For ' \
                'example 2 represents 1st row 2nd column box.)\n')
            
            #check if it number and its in within right range
            try:
                if (1 > int(choice) or 9 < int(choice) or 
                    int(choice)-1 not in available_boxes):
                    print('Input correct number! (1 to 9 that is not occupied)')
                    continue
                board[int(choice)-1] = 'x'
                player_turn = 0
            except ValueError:
                print('You need to provide a number within range 1-9!')       
        
        #computer turn (random)
        else:
            print("Computer's turn")
            board[random.choice(available_boxes)] = 'o'
            player_turn = 1
        
        #print board
        for i, item in enumerate(board, start=1):
            if i % 3 == 0:
                print(item)
            else:
                print(item, end=' | ')  
        
        #recalculate available boxes
        available_boxes = [i for i, k in enumerate(board) if k == " "]

        #check if someone has won. Set end to winner
        win_lines = [board[0:3], board[0::3], board[0::4], board[1::3], 
                    board[2:8:2], board[2::3], board[3:6], board[6:9]]
        for line in win_lines:
            unique = set(line)
            sign = unique.pop()
            if not unique:
                if sign == 'x':
                    end = 'player'
                elif sign == 'o':
                    end = 'comp'
                else:
                    continue
    #check end variable and print results
    if end == 'player':
        print('Gratz! You won!')
    elif end == 'comp':
        print('Sorry! You lost!')
    else:
        print("It's a draw!")

while True:
    play = input('Do you want to play? (y/n)')
    if play == 'y':
        play_game()
    elif play == 'n':
        break
    else:
        print('Please provide correct answer!')