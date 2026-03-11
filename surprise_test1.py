#1. Type Conversion Twist:
# What will be the code if output if code is this ? Explain why.
a = "5"
b = 2
print(a * b + str(b)) 

# Answer - output is 552 becoz in python when you multiply string x integer it repeats the string so "5" * 2 ==> "55"
# and in str(b) it will convert int b i.e 2 to str b i.e "2" so in print after addition it will give final output "552".

print("\n")

#2. Mutable vs Immutable:
#Predict the output and explain the behavior.
x = [1, 2, 3]
y = x
y.append(4)
print(x)

# Answer - x and y refer to the same list object because y = x does not create a copy.
# Since lists are mutable, y.append(4) modifies the original list.
# So, print(x) outputs [1, 2, 3, 4].

print("\n")


# 3. String Operations:
# Write a program to count how many numbers are present in a given string without using any built-in count() 
# method. use user defined function

str1 = input("Enter a string :")


def count_num(s):
    count = 0
    for i in s:
        if i.isdigit():
            count +=1
    return count

result = count_num(str1)
print("Total numbers in string are :",result)

print("\n")

# 4. Dictionary Logic:
# Given a dictionary of student names and marks, find and print the student(s) with the second highest marks.

s = {"Kunal":44,"Aniket":54,"Jay":35,"Vishal":60}

marks = sorted(set(s.values()),reverse=True)
sec_highest = marks[1]

for name,mark in s.items():
    if mark == sec_highest:
        print(name,"=",mark)

print("\n")


# 5. Nested Loop Logic:
# Write a program that prints the following pattern using loops:
# 1 2
# 3 4 5
# 6 7 8 9
# 10 11 12 13

num = 1
row_counts = [2, 3, 4, 4]   # fixed numbers per row

for count in row_counts:
    for i in range(count):
        print(num, end=" ")
        num += 1
    print()

print("\n")


# 6. While Loop with Condition:
# Write a program using a while loop to find the sum of digits of a given integer

def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total           

print(sum_of_digits(3456))

print("\n")

# 7. Break and Continue Combo:
# Write a program that prints all numbers from 1 to 30 except multiples of 3.
# Stop the loop completely if a number is divisible by 13.


def func():
    for i in range(1,31):
        if i % 13 == 0:
            break

        if i % 3 !=0:
            print(i)

func()

print("\n")


# 8. For Loop Challenge:
# Using a for loop, calculate the sum of all prime numbers between 10 and 50.

# 9. Function Default Parameter Trap:
# Predict the output with explanation of code
def add_item(item, items=[]):
 items.append(item)
 return items
print(add_item(1))
print(add_item(2))


# Output [1]
#        [1,2]
# Answer items=[] is created only once when the function is defined.Since lists are mutable, the same list is reused in every function call.
# So first call returns [1], and second call appends to same list ==> [1, 2].

print("\n")

# 10. Using a List comprehension, print only the words longer than 4 letters from a given list.

l1 = ["Python","React","HTML","Javascript","CSS"]

result = [i for i in l1  if len(i)>4]
print(result)

print("\n")

# 11. Write a list comprehension that creates a list of squares of even numbers between 1 and 20, but only if the number is not divisible by 4.

squares = [i**2 for i in range(1,21) if i%2==0 and i%4!=0]
print(squares)

print("\n")

# 12 List Flattening Challenge:
# Given a nested list like [[1,2], [3,4,5], [6]], flatten it into a single list using list comprehension only. E.g. [1,2,3,4,5,6]

f = [[1,2], [3,4,5], [6]]

merge = [m for sub in f for m in sub]
print(merge)

print("\n")


# 13. Take a string input and count how many digits, alphabets, and special characters it contains.

str1 = "My password is kunal@123#"

def func(str1):
    count_digits = 0
    count_alphabets = 0
    count_special = 0
    
    for i in str1:
        if i.isdigit():
            count_digits += 1
        elif i.isalpha():
            count_alphabets += 1
        elif not i.isspace():   # ignore spaces
            count_special += 1
    
    return count_digits, count_alphabets, count_special

print(func(str1))

print("\n")

# 14. From a given list of integers, find the second largest element without using max() twice or sorting.

# 15.Remove duplicates from a list while maintaining order (no set()).

def remove_duplicates(lst):
    unique = []
    
    for item in lst:
        if item not in unique:
            unique.append(item)
    
    return unique

nums = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(nums))

print("\n")

# 16.Merge two dictionaries without using the update() method.

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = {**d1,**d2}
print(merged)

# 17 and 18 not solved



            

