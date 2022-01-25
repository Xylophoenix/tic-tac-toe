
from operator import truediv
from tkinter.tix import FileSelectBox
import random

user_input = input("Enter x or o :- ")


board = ["","","","","","","","",""]
print('   |   |')
print(' ' + board[0] + '  | ' + board[1] + '  | ' + board[2])
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + board[3] + '  | ' + board[4] + '  | ' + board[5])
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + board[6] + '  | ' + board[7] + '  | ' + board[8])
print('   |   |')
def lets_play(user_input): 
    global user_playing
    user_playing = True
    first = str(input("Do you want to play first :- "))
    def user_play():
        global player_input
        player_input = int(input(f"Where you want to place {user_input}\n"
        "(1,2,3,4,5,6,7,8,9) :- "))
        global user_playing 
        user_playing = True
        if player_input == 1:
            board[0] = user_input
            print('   |   |')
            print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
            print('   |   |')
        elif player_input == 2:
            board[1] = user_input
            print('   |   |')
            print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
            print('   |   |')
        elif player_input == 3:
            board[2] = user_input
            print('   |   |')
            print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
            print('   |   |')
        elif player_input == 4:
            board[3] = user_input
            print('   |   |')
            print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
            print('   |   |')
        elif player_input == 5:
            board[4] = user_input
            print('   |   |')
            print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
            print('   |   |')
        elif player_input == 6:
            board[5] = user_input
            print('   |   |')
            print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
            print('   |   |')
        elif player_input == 7:
            board[6] = user_input
            print('   |   |')
            print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
            print('   |   |')
        elif player_input == 8:
            board[7] = user_input
            print('   |   |')
            print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
            print('   |   |')
        elif player_input == 9:
            board[8] = user_input
            print('   |   |')
            print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
            print('   |   |')
        if board[0] == user_input and board[1] == user_input and board[2] == user_input or board[3] == user_input and board[4] == user_input and board[5] == user_input or board[6] == user_input and board[7] == user_input and board[8] == user_input or board[0] == user_input and board[4] == user_input and board[8] == user_input or board[2] == user_input and board[4] == user_input and board[6] == user_input or board[0] == user_input and board[3] == user_input and board[6] == user_input or board[1] == user_input and board[4] == user_input and board[7] == user_input or board[2] == user_input and board[5] == user_input and board[8] == user_input:
            print("You have won")   
            user_playing = False
    def computer_play():
        global user_playing 
        user_playing = True
        if user_input == "x":
            computer_input = "o"
        if user_input == "o":
            computer_input = "x"
        computer_random = random.randint(0,8)
        board[computer_random] = computer_input
        if board[computer_random] == user_input:
            board[computer_random + 1] = computer_input
        if computer_random == 8:
            computer_random = 0
        print('   |   |')
        print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
        print('   |   |')
    while user_playing:
        if first == "yes" or "YES" or "Yes":
            user_play()
        computer_play()
lets_play(user_input)


