'''
Collaborators: Adrian, Jack, and I were conversing about each other's code, trying to figure out why certain lines were working and such.
'''

def add_math(num1, num2):
   return num1 + num2

def subtract_math(num1, num2):
   return num1 - num2

def multiply_math(num1, num2):
    return num1 * num2

def divide_math(num1, num2):
   return num1 / num2

print("Choose the operation to perform: ")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")
print("\n")

option = int(input("Choose 1, 2, 3, or 4: "))
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if option == 1:
    print(add_math(num1, num2))

elif option == 2:
    print(subtract_math(num1, num2))

elif option == 3:
    print(multiply_math(num1, num2))

elif option == 4:
    print(divide_math(num1, num2))

else:
    print("Please pick 1, 2, 3, or 4.")






'''
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

'''
