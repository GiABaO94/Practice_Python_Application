#Exercise 1
try:
    for i in ['a','b','c']:
        print(i ** 2)
except TypeError:
    print("Error!!!")

#Exercise 2
try:
    x = 5
    y = 0
    print(x/y)
except ZeroDivisionError:
    print('Type Error!!!')
finally:
    print('All Done')

#Exercise 3
def askint():
    while True:
        try:
            print('Enter an interger: ')
            var_enter = int(input())
            result = var_enter * var_enter
            print('Square: %s' % (result))
        except ValueError:
            print("You didn't enter the right interger. Please try again")
            continue
        else:
            break
        finally:
            print("Completed")

askint()