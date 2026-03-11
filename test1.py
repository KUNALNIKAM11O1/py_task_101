# 1  Write a program to input exactly five student names, store them in a list, and then print the names in uppercase. 

student = []

for i in range(5):
    name = input(f"Enter name of student {i+1} :")
    student.append(name)

print("Students name in upper case")

for name in student:
     print(name)


# # 2.Convert a list of integers to a set to remove duplicates, then convert it back to a sorted list. 

# l1 = [1,2,4,6,6,8,9,9,11]

# l1_s = set(l1)

# print(l1_s)

# sorted_list = sorted(l1_s)
# print("The sorted list is",sorted_list)

# # 3. Write a program to check whether a list contains any duplicate elements (return True/False).

# l1 = [1,2,4,6,6,8,9,9,11]

# for i in l1:
#    if l1.count(i) > 1:
#       print("True")
#    else:
#       print("False")

# # 4. Remove all vowels (a, e, i, o, u) from every string in a list and print the resulting list.

# l1 = ["HTML","CSS","Bootstrap","Tailwind","React","Backend"]

# vowels = "aeiou"

# result = []

# for word in l1:
#     new = ""
#     for ch in word:
#         if ch not in vowels:
#             new += ch
#     result.append(new)

# print(result)

# # 5. Take a user’s age as input and determine the movie‑ticket price using if‑elif‑else logic:

# # < 5 → “Free”, 5–18 → “₹50”, 18–60 → “₹100”, ≥ 60 → “₹70”.


# user_age = int(input("Enter the user's age :"))

# if user_age >= 60 :
#     print("Ticket is ₹70")
# elif user_age >=18 and user_age <60:
#     print("Ticket is ₹100")
# elif user_age >=5 and user_age <18:
#     print("Ticket is ₹50")
# else:
#     print("Ticket is free")


# # 6. Ask the user for a number and check whether it is divisible by both 3 and 5.

# num1 = int(input("Enter the number :"))

# if num1%3==0 and num1%5==0:
#     print(num1,"is divisible by both 3 and 5")
# else :
#     print(num1,"is not divisible by both 3 and 5")

# # 7. Check if a given year is a leap year using the standard Gregorian rules


# year = int(input("Enter the year :"))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(year,"is a leap Year")
# else:
#     print(year,"is not a leap year")

# # 8.  Read input from the user and print its data type (int, float, or str) 

# d1 = input(("Enter the input to check data type :"))

# print("data type is ",type(d1))


# # 9. Convert a numeric string (e.g., "1234") to an integer, add 10 to it, and print the result.

# str1 = "1234"

# str1_int = int(str1)

# result = str1_int + 10


# print("Result :",result)

# # 10.Swap the values of two variables without using a third variable and print the swapped values.

# a = int(input("Enter the value of a :"))
# b = int(input("Enter the value of b :"))

# a,b = b,a

# print("After swapping","a=",a,"b=",b)

# # 11.  Determine whether a single input character is a vowel or consonant with an if‑else statement.

# character = input("Enter the aplhabet :")

# vowel = "aeiouAEIOU"
  
# if character in vowel:
#     print(character,"is a vowel")
# else:
#     print(character,"is a consonant")

# # 12.   Read three numbers and use if‑elif‑else to print the largest of the three.

# num1 = int(input("Enter first number :"))
# num2 = int(input("Enter first number :"))
# num3 = int(input("Enter first number :"))

# if num1 >= num2 and num1 >= num3:
#     print("greatest number is",num1)
# elif num2 >= num1 and num2 >= num3:
#      print("greatest number is",num2)
# else:
#       print("greatest number is",num3)


# # 13.  Check whether a given string is a palindrome (reads the same forward and backward) by using slicing).

# str1 = input("Enter the string :")

# if str1 == str1[::-1]:
#     print(str1,"is a palindrome")
# else :
#     print(str1,"is not a palindrome")

# # 14. Ask the user to choose either Celsius→Fahrenheit or Fahrenheit→Celsius conversion (if‑elif). Perform the chosen conversion and display the result.

# # Not able to solve