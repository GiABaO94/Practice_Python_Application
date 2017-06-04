import random
#Problem 1
#Create a generator that generates the squares of numbers up to some number N.
def square(n):
    for element in range(n):
        yield element**2

print('Problem 1')
for i in square(3):
    print(i)

#Problem 2
#Create a generator that yields "n" random numbers between a low and high number (that are inputs). Note: Use the random library.
def random_high_low(high,low,n):
    if(high <= low):
        print('Error')
    else:
        for element in range(n):
            yield random.randint(low,high)

print('Problem 2')
for i in random_high_low(12,1,10):
    print(i)

#Problem 3
#Use the iter() function to convert the string below
print('Problem 3')
s = 'Vo Hoang Gia Bao'
s_iter = iter(s)
for i in range(len(s)):
    print(next(s_iter))

#Extra: Generator Comprehension
print('Extra')
my_list = [1,2,3,4,5,6,7]

my_gene = (item for item in my_list if item > 3)

for item in my_gene:
    print(item)