# 1.Write a program that takes an integer as input and converts it into a string. Then, concatenate it with another string and print the result.

#num = int(input("Enter the integer :"))
#num_str = str(num)

#print(num_str)
#print(type(num_str))

#result = num_str + " " + "is my fav num"
#print(result)

# 2.Write a program that takes a numerical string as input and converts it into an integer. Perform arithmetic operations on the integer and print the results.

#str1 = str(input("Enter the numerical string :"))
#str1_num = int(str1)

#print("Addition : ",str1_num + 10)
#print("Sub :", str1_num - 4)
#print("Multi : ", str1_num * 10)
#print("Div : ",str1_num / 2)

# 3.Write a program that takes a float number as input, converts it into an integer, and then prints the integer.

#num1 = float(input("Enter the float number :"))
#num1_int1 = int(num1)

#print(num1_int1)

# 4. Write a program that takes two integers as input, divides them using the integer division operator (//), converts the result into a float, and prints the float.

#num2 = int(input("Enter first number :"))
#num3 = int(input("Enter second number : "))

#divsion = num2 // num3

#divsion_flo = float(divsion)

#print(divsion_flo)

# 5. Write a program that takes a comma-separated string of numbers as input, converts it into a list of integers, and then calculates and prints the sum of the list.

#num4 = str(input("Enter the string of numbers :"))
#num4_list = list(map(int,num4.split(",")))

#total = sum(num4_list)

#print(total)

# 6. Write a program that takes a list of strings as input, converts the list into a single string by concatenating the elements with a space, and then prints the resulting string

#str1 = input("Enter the list of string :").split()
#result = "".join(str1)

#print(str1)

# 7. Write a program that takes a string ("True" or "False") as input, converts it into a boolean value, and then prints whether it's True or False.


# word = input("Enter the value true or false :")

# if word == "true":
#     result = True
# elif word == "false":
#     result = False
# else :
#     result = None

# if result is not None:
#     print("Boolean value : ",result)
# else :
#      print("Invalid Input")


# 8.Write a program that takes a float number as input, converts it into a string with exactly two decimal places, and then prints the resulting string.

# number2 = float(input("Enter the number :"))
# result = "{:.2f}".format(number2)
# print(result)

# 9.Write a program that takes an integer as input, converts it into a float, performs some arithmetic operations involving both integers and floats, and prints the results.

int1 = int(input("Enter the number :"))
int1_flo = float(int1)

print("Addition :",int1 + int1_flo)
print("Sub :", int1 - int1_flo)



