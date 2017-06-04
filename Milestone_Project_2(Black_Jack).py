#Import module
import random
import os

#Define Function
def clear():
    os.system( 'cls' )

#Define Objects
def ask_info():
    print('Welcome to BlackJack World')
    print('Are you ready??? (Y/N)')
    your_answer_01 = str(input())
    if(your_answer_01[0].upper() == 'Y'):
        print('Please enter your name: ')
        your_name = str(input())
        print('Please enter your amount: ')
        while True:
            try:
                your_amount = int(input())
            except TypeError:
                print('Please enter your amount again (just accept number): ')
                continue
            else:
                break
            finally:
                pass
        return (str(your_name) + ' ' + str(your_amount))
    else:
        return ('')

def draw_card(board_list):
    choose = random.choice(board_list)
    board_list.remove(choose)
    return choose

def compare_mark(own_mark,player_mark):
    if(own_mark <= player_mark):
        print('Own mark is: %s' % (own_mark))
        print('Congratulation!!! You won!!!')
    else:
        print('Own mark is: %s' % (own_mark))
        print('You lose!!!')


#Create System Object
class Own(object):
    def __init__(self):
        self.name = 'System'
        self.hand = 0
        self.onhand = []
        self.total_mark = 0

    def check_mark(self):
        self.total_mark = 0
        for element in self.onhand:
            if(self.total_mark > 11 and self.total_mark <= 21):
                if(element in ['J','Q','K']):
                    self.total_mark = self.total_mark + 10
                elif(element == 1):
                    self.total_mark = self.total_mark + 1
                else:
                    self.total_mark = self.total_mark + element
            elif(self.total_mark > 21):
                print('Own mark is: %s' % (self.total_mark))
                print('Own lose!!!')
                break
            else:
                if(element in ['J','Q','K']):
                    self.total_mark = self.total_mark + 10
                elif(element == 1):
                    self.total_mark = self.total_mark + 11
                else:
                    self.total_mark = self.total_mark + element
        return self.total_mark

    def take_card(self,status,board_list):
        if(status == 1):
            self.onhand.append(draw_card(board_list))
            self.onhand.append(draw_card(board_list))
            self.hand = 2
            #print('The cards on own hand are: %s' % (self.onhand))
        else:
            self.onhand.append(draw_card(board_list))
            self.hand = self.hand + 1
            #print('The cards on own hand are: %s' % (self.onhand))

#Create Player Object:
class Player(object):
    def __init__(self,name,total_money):
        self.name = name
        self.total_money = total_money
        self.hand = 0
        self.onhand = []
        self.total_mark = 0
        self.gamble_money = 0
    
    def check_mark(self):
        self.total_mark = 0
        for element in self.onhand:
            if(self.total_mark > 11 and self.total_mark <= 21):
                if(element in ['J','Q','K']):
                    self.total_mark = self.total_mark + 10
                elif(element == 1):
                    self.total_mark = self.total_mark + 1
                else:
                    self.total_mark = self.total_mark + element
            elif(self.total_mark > 21):
                print('You lose!!!')
                break
            else:
                if(element in ['J','Q','K']):
                    self.total_mark = self.total_mark + 10
                elif(element == 1):
                    self.total_mark = self.total_mark + 11
                else:
                    self.total_mark = self.total_mark + element
        return self.total_mark

    def take_card(self,status,board_list):
        if(status == 1):
            self.onhand.append(draw_card(board_list))
            self.onhand.append(draw_card(board_list))
            self.hand = 2
            self.gamble_money = 50
            self.total_money = self.total_money - 50
            print('The cards on your hand are: %s' % (self.onhand))
            print('Total money now: %s' % (self.total_money))
        else:
            self.onhand.append(draw_card(board_list))
            self.hand = self.hand + 1
            self.total_money = self.total_money - self.gamble_money
            print('The cards on your hand are: %s' % (self.onhand))
            print('Total money now: %s' % (self.total_money))
    
    def stop_card(self):
        print('Your mark total is: %s' % (self.total_mark))

    def add_money(self,gamble):
        self.gamble_money = 0
        if(self.total_money < gamble):
            return False
        else:
            self.gamble_money = self.gamble_money + gamble
            return True

    #def stop_game(self):


#Main processing
str_info = ask_info()
if(len(str_info) > 0):
    list_info = str_info.split()
    board_list = 4*[1,2,3,4,5,6,7,8,9,10,'J','Q','K']
    o = Own()
    p = Player(name = str(list_info[0]),total_money = int(list_info[1]))
    print("Player's name is: " + p.name.upper())
    print("Total money is currently: " + str(p.total_money))
    p.take_card(1,board_list)
    check_mark_info_player = p.check_mark()
    print('Mark now: ' + str(check_mark_info_player))
    o.take_card(1,board_list)
    check_mark_info_own = o.check_mark()
    i = 2
    while (i < 5):
        if(check_mark_info_player < 21 and len(p.onhand) < 5):
            print('Do you want to draw card(Y/n): ')
            while True:
                try:
                    draw_card_info = str(input())
                except TypeError:
                    continue
                else:
                    break
                finally:
                    pass
            if(draw_card_info[0].upper() == 'Y'):
                while True:
                    print('Please add money: ')
                    try:
                        adding_money = int(input())
                    except TypeError:
                        continue
                    else:
                        break
                    finally:
                        pass
                check_mark_info_own = o.check_mark()
                if(adding_money > p.total_money or adding_money == 0):
                    continue
                else:    
                    p.add_money(adding_money)
                    p.take_card(i,board_list)
                    check_mark_info_player = p.check_mark()
                    print('Mark now: ' + str(check_mark_info_player))
                    if(check_mark_info_own == 17):
                        pass
                    elif(check_mark_info_own < check_mark_info_player and check_mark_info_own <= 21):
                        o.take_card(i,board_list)
                        check_mark_info_own = o.check_mark()
                    else:
                        pass
                    i = i + 1
            else:
                p.stop_card()
                compare_mark(check_mark_info_own,check_mark_info_player)
                break

        elif(check_mark_info_player == 21):
            print('The cards on own hand are: %s' % (o.onhand))
            print('Own mark is: %s' % (o.total_mark))
            print('You won!!!')
            break
        else:
            print('The cards on own hand are: %s' % (o.onhand))
            print('Own mark is: %s' % (o.total_mark))
            print('You lose!!!')
            break
else:
    print('The game will be ended')