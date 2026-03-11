# 1. Create a program that takes the base and height of a triangle as input and calculates its area (½ * base * height)

# base = int(input("Enter the base of triangle :"))
# height = int(input("Enter the height of triangle :"))

# area = 1/2 * base * height

# print(f"Area of triangle of base {base} and height {height} is {area}")

# 2. Write a program that takes a number as input and prints its square and cube.

# num1 = int(input('Enter the number to get its square and cube :'))

# num1_square = num1 * num1

# num1_cube = num1 * num1 * num1

# print(f"Square and cube of number {num1} is {num1_square} and {num1_cube} resp")

# 3. Write a program that simulates a simple calculator. The program should take two numbers(user inputs)and an operator (+, -, *, /) as input and perform the corresponding operation, displaying the result.


num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))

operations = input("Enter operations(+ , - , * , /) :")

if operations == "+":
    print("Result :", num1 + num2)
elif operations == "-":
    print("Result :", num1 - num2)
elif operations == "*":
    print("Rseult :", num1 * num2)
elif operations == "/":
    if num2 != 0:
        print("Result :",num1 / num2)
    else : 
        print("Error : Divsion by zero is not allowed")

else :
    print("Invalid operator")