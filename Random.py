import random

board_list = 4*[1,2,3,4,5,6,7,8,9,10,'J','Q','K']
#for seq in range(1,26):
#    choose = random.choice(board_list)
#    board_list.remove(choose)
#    print(board_list)
#    print(choose)



def draw_card(board_list):
    choose = random.choice(board_list)
    board_list.remove(choose)


draw_card(board_list)
print(board_list)