# # 1.Write a function sum_of_digits(n) that takes an integer and returns the sum of its digits.
# # Example: sum_of_digits(1234) → 10

# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total = total + digit
#         n = n // 10
#     return total           

# print(sum_of_digits(3456))



# # 2.Write a function count_vowels(s) that counts the number of vowels in a string using a loop.
# # Example: count_vowels("hello world") → 3

# s = "My Name is Kunal Nikam"
# vowels = "aeiouAEIOU"

# def count_vowels(s):
#     count = 0
#     for i in s:
#         if i in vowels:
#             count = count + 1
#     return count
# print(count_vowels(s))


# # 3.Factorial using Loop
# # Write a function factorial(n) that calculates factorial using a for loop.
# # Example: factorial(5) → 120


# def factorial(n):
#     n = int(input("Enter the number :"))
#     fac = 1
#     for i in range(1,n+1):
#         fac = fac*i
#     return fac
# print(factorial(5))

# # 4.Prime Check
# # Write a function is_prime(n) that returns True if n is prime, otherwise False.
# # Example: is_prime(11) → True

# def is_prime(n):
#     n = int(input("Enter the number :"))
#     if n == 1:
#         return False
#     for i in range(2,n):
#         if n%2==0:
#             return False
#         else:
#             return True
# print(is_prime(7))

# 5.Reverse a String
# Write a function reverse_string(s) that reverses a string using a loop.
# Example: reverse_string("python") → "nohtyp"


# 1st method
# def reverse_string(str1):
#    return str1[::-1]
# print(reverse_string("python"))

# 2nd method
# def rev_string(s):
#    return "".join(reversed(s))
# print(rev_string("react"))



#  6 .Library Management – Book Borrow System
# A library keeps track of books and their availability.
# You need to write functions to manage the borrowing system.
# display_books(library) → prints all books with their status (Available or Issued)
# borrow_book(library, book_name) →
# If the book is available → mark it as "Issued" and print "Book issued successfully"
# If not available → print "Sorry, book not available"
# return_book(library, book_name) → marks the book back as "Available"
# # Example:
# library = {
# "Python Basics": "Available",
#  "Data Science": "Issued",
#   "Machine Learning": "Available"
# }

# display_books(library)
# borrow_book(library, "Python Basics")
# return_book(library, "Data Science")
# display_books(library)

# # Expected Output:
# Books in Library:
# Python Basics - Available
# Data Science - Issued
# Machine Learning - Available
# Book issued successfully
# Book returned successfully

# # Books in Library:
# Python Basics - Issued
# Data Science - Available
# Machine Learning - Available








# # # 7.Fibonacci Series
# # Write a function fibonacci(n) that prints the first n numbers of the Fibonacci sequence.
# # Example: fibonacci(5) → [0, 1, 1, 2, 3]

# def fibonacci(n):
#     fib = [0,1]
#     for i in range(2,6):
#         next_term = fib[-1] + fib[-2]
#         fib.append(next_term)
#     return fib
# print(fibonacci(5))

# # 8.Even Numbers from List
# # Write a function get_even_numbers(lst) that returns a list of even numbers from the given list.
# # Example: get_even_numbers([1,2,3,4,5,6]) → [2,4,6]

# def get_even_numbers(lst):
#      even = []
#      for i in lst:
#           if i%2==0:
#                even.append(i)
#      return even
# print(get_even_numbers([1,2,3,4,5,6]))

# # 9..Find Maximum in List
# # Write a function find_max(lst) that returns the maximum number from a list without using max() function.

# def find_max(lst):
#     max_num = lst[0]
#     for i in lst:
#        if i > max_num:
#            max_num = i
#     return max_num
# print(find_max([3,1,4,5,7,11,9]))

# # 10.You are given a list of student marks.
# # Write a function grade_report(marks) that:
# # Prints each student’s mark.
# # Counts how many students passed (marks ≥ 40).
# # Find the highest and lowest marks.

# def grade_report(marks):
#     passed_std = 0
#     highest = marks[0]
#     lowest = marks[0]

#     for p in marks:
#         print("Mark:", p)

#         if p >= 40:
#             passed_std += 1

#         if p > highest:
#             highest = p

#         if p < lowest:
#             lowest = p

#     print("Passed students:", passed_std)
#     print("Highest marks:", highest)
#     print("Lowest marks:", lowest)

# grade_report([20,50,65,70,22,49])

# # 11.Sum of Even Numbers up to N
# # Write a function sum_even(n) that returns the sum of all even numbers from 1 to n.
# # Example: sum_even(10) → 30 (2+4+6+8+10)

# def sum_even(n):
#    total = 0
#    for i in range(1,n+1):
#       if i%2==0:
#          total = total + i
#    return total
# print(sum_even(8))

# # 12.Count Words in String
# # Write a function count_words(sentence) that counts how many words are in a given string (don’t use .split()).
# # Example: count_words("I love Python") → 3

# def count_words(s):
#     count = 0
#     in_word = False

#     for i in s:
#         if i!=" " and in_word == False:
#             count += 1
#             in_word = True
#         elif i == " ":
#             in_word = False

#     return count
# print(count_words("My name is Kunal Nikam"))

# # 13.Number Pattern
# # Write a function number_pattern(n) that prints the following pattern using loops:
# # For n=5

#  1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5

# def number_pattern(n):
#     for row in range(1,n+1):
#        for column in range(1,row+1):
#             print(column,end=" ")
#        print()

# number_pattern(5)

# # 14.Find Common Elements
# # Write a function common_elements(list1, list2) that returns the common elements of two lists using loops.
# # Example: common_elements([1,2,3,4], [3,4,5,6]) → [3,4]

# def common_elements(list1,list2):
#     common = []

#     for i in list1:
#         for j in list2:
#             if  i == j:
#              common.append(i)
#     return common

#  l5.Armstrong Number Check
# Write a function is_armstrong(n) that checks whether a number is an Armstrong number.
# Example: is_armstrong(153) → True
# (Since 1³ + 5³ + 3³ = 153)

def is_armstrong(n):
   for i in n:
      if n*n*n == n:
         True
      else:
          False
      return n
      
print(is_armstrong(153))

   





 
        
               
    

    
            

  

          
          