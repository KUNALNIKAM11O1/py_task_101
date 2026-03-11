# 1.Write a program to input exactly 6 city names, store them in a list, and then print all city names in lowercase.


# city = []   

# for i in range(6):
#     names = input(f"Enter the city name :  ").lower()
#     city.append(names)

# print(city)


# 2.Convert a list of numbers into a set to remove duplicates, then convert it back into a sorted tuple.

# l1 = [1,2,3,3,3,4,5,6,6,7,8,9]

# l1_s = set(l1)

# s_t = tuple(l1_s)

# print(s_t)

# 3.Write a program to check whether a list contains any repeated values (return True/False).

# l1 = [1,2,3,4,5,6,7,8,9]

# if len(l1) != len(set(l1)):
#     print(True)
# else :
#     print(False)


# 4.Remove all digits (0–9) from every string in a list and print the updated list.  


# words = ["abc123", "he45llo", "99python"]

# result = []

# for w in words:
#     new_word = ""
#     for ch in w:
#         if not ch.isdigit():
#             new_word += ch
#     result.append(new_word)

# print(result)



# 5.Take the user’s marks as input and determine the grade using if-elif-else:  < 35 → "Fail" , 35–50 → "Pass" , 50–75 → "Good" , ≥ 75 → "Excellent"

# marks = int(input("Enter user's marks :"))

# if marks >= 75:
#     print("Excellent")
# elif  50 <= marks < 75:
#     print("Good")
# elif 35 <= marks < 50:
#     print("Pass")
# else :
#     print("Fail")

# 6.Ask the user for a number and check whether it is divisible by 2 and 7.


# num = int(input("Enter the number :"))

# if num%2 == 0 and num%7==0:
#     print(num,"is divisible by both 2 and 7")
# else:
#     print(num,"is not divisible by both 2 and 7")

# 7.Check whether a given number is a prime number or not.  

# num = int(input("Enter a number :"))

# if num <=1:
#     print("Not Prime")
# else:
#     for i in range(2,num):
#         if num % 2 == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime Number")


# 8.Read input from the user and print whether it is positive, negative, or zero.

# num2 = int(input("Enter the number :"))

# if num2 > 0:
#     print(num2,"is positive number")
# elif num2 < 0:
#     print(num2,"is negative number")
# else:
#     print("zero")

# 9.Convert a numeric string (e.g. "500") into an integer, multiply it by 5, and print the result.

# str = "500"

# str_int = int(str)*5

# print(str_int)

# 10.Swap the values of three variables (a, b, c) in cyclic order:  XXXX

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# a, b, c = b, c, a

# print("After swapping:")
# print("a =", a)
# print("b =", b)
# print("c =", c)


# 11.Determine whether a single input character is a digit or alphabet using if-else.

# ch = input("Enter the single input character :")

# if ch.isdigit():
#     print(ch,"is a digit")
# elif ch.isalpha():
#     print(ch,"is alphabet")
# else:
#     print("wrong input")

# 12.Read four numbers and use if-elif-else to print the smallest number.  XXXX

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if a <= b and a <= c and a <= d:
#     print("Smallest is:", a)
# elif b <= a and b <= c and b <= d:
#     print("Smallest is:", b)
# elif c <= a and c <= b and c <= d:
#     print("Smallest is:", c)
# else:
#     print("Smallest is:", d)

# 13.Check whether a given string is an anagram of another string.

s1 = input("Enter the first word :").lower()
s2 = input("Enter the second word :").lower()

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")





