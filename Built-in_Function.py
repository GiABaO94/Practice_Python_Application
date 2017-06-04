#Import Module
import functools

#Map
celius = [30, 60, 90, 100]
fahrenheit = list(map(lambda x: (5.0/9)*(x-32), celius))
print(fahrenheit)

list_a = [1,2,3]
list_b = [4,5,6]
list_c = [7,8,9]
total = list(map(lambda x, y, z: (x + y + z), list_a, list_b, list_c))
print(total)
#Reduce
number_array = [1,2,3,4,5,6,7,8,9,10]
add_array = lambda x, y: x if (x > y) else y
total_array = list(functools.reduce(add_array,number_array))
print(total_array)


#Filter (return True or False)
old_even_array = [1,2,3,4,5,6,7,8,9,10]
even_list = list(filter(lambda x: (x % 2 == 0), old_even_array))
print(even_list)
