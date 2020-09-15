'''
Adapt the code from one of the functions above to create a new function called 'multiplier'.
The user should be able to input two numbers that are stored in variables.
The function should multiply the two variables together and return the result to a variable in the main program.
The main program should output the variable containing the result returned from the function.
'''


def multiplier():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    return num1 * num2

output_num = multiplier()

print(output_num)