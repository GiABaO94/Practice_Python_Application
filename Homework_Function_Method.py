#Write a function that checks whether a number is in a given range (Inclusive of high and low)

#The first way: Normal
def ran_check(num, low, high):
    if(num >= low and num <= high):
        return True
    else:
        return False

print(ran_check(2,2,3))

#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33
def calc_upper_lower(content):
    txt_content = content.split()
    count_upper = 0
    count_lower = 0
    for element in txt_content:
        for detail in element:
            if(detail.isupper() == True):
                count_upper = count_upper + 1
            elif(detail.islower() == True):
                count_lower = count_lower + 1
    print("The string is: " + content)
    print("No. of uppper is: " + str(count_upper))
    print("No. of lower is: " + str(count_lower))

test_content = "Vo Hoang Gia Bao"
calc_upper_lower(test_content)


#Write a Python function that takes a list and returns a new list with unique elements of the first list.

#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
def unique_list(list):
    list = set(list)
    my_list = []
    for element in list:
        my_list.append(element)
    return my_list

sample_list = [1,1,1,1,2,2,3,3,3,3,4,5]
unique_list = unique_list(sample_list)
print(unique_list)


#Write a Python function to multiply all the numbers in a list.

#Sample List : [1, 2, 3, -4]
#Expected Output : -24
def multupy(list):
    result = 1
    if(len(list) != 0):
        for element in list:
            result = result * element
    else:
        result = 0
    return result

computer_list = [7,10,13]
result = multupy(computer_list)
print(result)


#Write a Python function that checks whether a passed string is palindrome or not.

#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def palindrome(sample):
    before = sample
    after = ""
    lengh_value = len(before)
    while(lengh_value > 0):
        after = after + before[lengh_value - 1]
        lengh_value = lengh_value - 1
    if(before == after):
        return True
    else:
        return False

value = "AbobA"
print(palindrome(value))


#Hard:

#Write a Python function to check whether a string is pangram or not.

#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"
def ispangram(str1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    check = True
    for element in alphabet:
        if(str1.find(element) == -1):
            check = False
            break
    return check

my_string = "The quick brown fox jumps over the lazy dog"
print(ispangram(my_string))