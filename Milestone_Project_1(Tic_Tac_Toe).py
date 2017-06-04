#Import module
#from IPython.display import clear_output
import os

def clear():
    os.system( 'cls' )

def game_mode():
    print('Welcome to Tic Tac Toe Game')
    print('Designed by BaoVHG')
    print('Please enter number of player: 1 or 2. Any answer different 1 or 2 is not accepted.')
    no_of_player = int(input())
    if(no_of_player == 1 or no_of_player == 2):
        print('Congratulation! The set up is completed. Let enjoy this game!!!')
        return no_of_player
    else:
        print('Your answer is wrong. The program is stopping.')
        no_of_player = 0
        return no_of_player


def draw_board(board):
    clear()
    link_line = '-----'
    for element in board:
        if(int(element) % 3 != 0):
            print(board[str(element)], end = '')
            print('|', end = '')
        else:
            print(board[str(element)])
            print(link_line)
    return board

def turn_board(num, current_board, signal):
    for element in current_board:
        try:
            check = current_board.keys()
            for detail in check:
                if(detail == str(num)):
                    current_board[detail] = signal
                    break
        except ValueError:
            continue
    return current_board

def turned(turn, own_turned):
    for element in own_turned:
        if(element == turn):
            return own_turned
        else:
            own_turned.append(turn)
            return own_turned


def check_winner(board):
    bool = False
    result_check = False
    set_x = ['X', 'X', 'X']
    set_o = ['O', 'O', 'O']
    set_win_key = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    temp_list = []
    for element in set_win_key:
        for detail in element:
            if(board[str(detail)] == 'X' or board[str(detail)] == 'O'):
                temp_list.append(board[str(detail)])
            else:
                continue
        if(temp_list == set_x):
            print('We have a winner player!!!Congratulation Player 1!!!')
            bool = True
            break
        elif(temp_list == set_o):
            print('We have a winner player!!!Congratulation Player 2!!!')
            bool = True
            break
        else:
            temp_list =[]
    return bool



def game_play_2_player(no_player, board):
    signal_player_1 = 'X'
    signal_player_2 = 'O'
    full_turn = 9
    current_turn = 1
    own_turn = [1,2,3,4,5,6,7,8,9]
    check = True
    while(current_turn <= 9):
        if(current_turn % 2 != 0):
            print('Now, turn of player 1: ')
            choose_player_1 = int(input())
            for element in own_turn:
                if(element == choose_player_1):
                    #Call method to write
                    current_board = turn_board(choose_player_1, board, signal_player_1)
                    own_turn[own_turn.index(element)] = 'Delete'
                    current_turn +=1
                    check_enter = True
                    check_result = check_winner(current_board)
                    break
                else:
                    check_enter = False
            if(check_enter == False):
                print('This position is not correct. Please choose again')
            elif(check_enter == True):
                draw_board(current_board)
                if(check_result == True):
                    print('This game is complete')
                    current_turn += 10
        else:
            print('Now, turn of player 2: ')
            choose_player_2 = int(input())
            for element in own_turn:
                if(element == choose_player_2):
                    #Call method to write
                    current_board = turn_board(choose_player_2, board, signal_player_2)
                    own_turn[own_turn.index(element)] = 'Delete'
                    current_turn +=1
                    check_enter = True
                    check_result = check_winner(current_board)
                    break
                else:
                    check_enter = False
            if(check_enter == False):
                print('This position is not correct. Please choose again')
            elif(check_enter == True):
                draw_board(current_board)
                if(check_result == True):
                    print('This game is complete')
                    current_turn += 10


#Main process
line_board = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
board = draw_board(line_board)
no_of_player = game_mode()
game_play_2_player(no_of_player, board)
