"""
Writting functions for processing
"""
# function to calculate BMI Index
def BMI_Calculation(tall, weight):
    result_bmi = (weight/(tall**2))
    return result_bmi
# function to check BMI Status
def BMI_Check(result):
    final_result = ""
    if(result < 18.5):
        final_result = "C"
    elif(result >= 18.5 and result <= 24.9):
        final_result = "A"
    else:
        final_result = "B"
    return final_result

"""
Writting code
"""
# Introduce program name
print ("Welcome to Demo_BMI")
# Request enter input
print ("Your tall (m): ")
tall = float(input())
print ("Your weight (kg): ")
weight = float(input())
# Call processing function
result = BMI_Calculation(tall,weight)
final_result = BMI_Check(result)
# Export output
print ("Your BMI Index is: %s" % result)
print ("Your heathy status is: %s" % final_result)


