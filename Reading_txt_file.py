# Import libraries
from os.path import exists
import os
import os.path

#Method to check answer of customer
#-----***-----
def Check_Answer(your_answer):
    file_name = ""
    if(your_answer[0] == "y"):
        print("Please enter the name of file you want to read: ")
        file_name = input()
    else:
        print("The program will stop now. Thanks!!!")
    return file_name
#-----***-----

#Method to check file
#-----***-----
def Check_File(file_name):
    result = False
    if(os.path.exists(file_name) == True):
        result = True
    else:
        result = False
    return result
#-----***-----

#Method to check read file
#-----***-----
def Read_File(file_name):
    txt = open(file_name, 'r')
    txt_content = txt.read()
    txt.close()
    print (txt_content)
#-----***-----

#Main_process
print("Do you want to read a txt file???")
your_answer = input()
your_answer = your_answer.lower()
file_name = Check_Answer(your_answer)
result = Check_File(file_name)
if(result == True):
    Read_File(file_name)
else:
    print("Nothing!!!")




        