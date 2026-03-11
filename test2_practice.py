# 1.Write a function is_palindrome(n) that checks whether a number is palindrome.
# Example: is_palindrome(121) → True

# def is_palindrome(n):
#     s = str(n)
#     for i in s:
#         if s == s[::-1]:
#             return True
#         else:
#             return False
        
# print(is_palindrome(1010))
    

# 2.Palindrome String Check
# Write a function is_palindrome_string(s) that checks whether a string is palindrome.
# Example: is_palindrome_string("madam") → True

# def is_palindrome_string(s):
#     for i in s:
#         if s == s[::-1]:
#             return True
#         else :
#             return False
        
# print(is_palindrome_string("DaaD"))

# 3.Write a function count_digits(n) that returns how many digits are in a number.
# Example: count_digits(12345) → 5

# def count_digits(n):
#     s = str(n)
#     return len(s)
# print(count_digits(1234))

# # using loop

# def count_digit(n):
#     count = 0
#     for digit in str(n):
#         count += 1
#     return count
# print(count_digit(123))

# 4.Write a function sum_odd(n) that returns sum of odd numbers from 1 to n.
# Example: sum_odd(10) → 25

# def sum_odd(n):
#     sum = 0
#     for i in range(1,n+1):
#         if i%2!=0:
#             sum = sum + i
#     return sum
# print(sum_odd(12))

# 5.Find Minimum in List
# Write a function find_min(lst) that returns the minimum number without using min().

# def fin_min(lst):
#     min_num = lst[0]
#     for i in lst:
#         if i < min_num:
#             min_num = i
#     return min_num
# print(fin_min([6,4,8,2,9]))

# 6.Count Even and Odd
# Write a function count_even_odd(lst) that returns count of even and odd numbers.
# Example: count_even_odd([1,2,3,4]) → even=2 odd=2

# def count_even_odd(lst):
#     even = 0
#     odd = 0
#     for i in lst:
#         if i%2==0:
#             even += 1
#         else:
#             odd += 1
#     return f"even={even} odd={odd} "

# print(count_even_odd([1,2,3,4,5,7]))

# 7.Multiplication Table
# Write a function print_table(n) that prints table of n up to 10.
# # Example: print_table(5)

# def print_table(n):
#    for i in range(1,11):
#       print(n,"x",i,"=",n*i)
   
# print(print_table(6))

# 8.Sum of List Elements
# Write a function sum_list(lst) that returns sum of all elements without using sum().

# def sum_list(lst):
#     summ = 0
#     for i in lst:
#         summ = summ + i
#     return summ
# print(sum_list([1,2,3,4,5]))

# 9.Remove Duplicates
# Write a function remove_duplicates(lst) that returns a list without duplicates.
# Example: remove_duplicates([1,2,2,3,3]) → [1,2,3]

# def remove_duplicates(lst):
#     unq = []
#     for i in lst:
#         if i not in unq:
#             unq.append(i)
#     return unq
# print(remove_duplicates([1,2,3,3,2,4,5,6]))

# 10.Count Frequency of Character
# Write a function char_frequency(s, ch) that counts how many times character appears.
# Example: char_frequency("banana",'a') → 3

# def char_freq(s,ch):
#      count = 0
#      for i in s:
#           if i == ch:
#                count += 1
#      return count
# print(char_freq("Manasi","a"))

# 11.Count Uppercase and Lowercase
# Write a function count_case(s) that counts uppercase and lowercase letters.
# Example: count_case("PyTHon") → upper=3 lower=3

# def count_case(s):
#     lower = 0
#     upper = 0
#     for i in s:
#        if i.islower():
#         lower += 1
#        elif i.isupper():
#           upper += 1
#     return f"upper={upper} lower={lower}" 
# print(count_case("Kunal Nikam"))
        
# 12.Find Factors of a Number
# Write a function factors(n) that returns all factors of n.
# Example: factors(12) → [1,2,3,4,6,12]

# def factors(n):
#     fac = []
#     for i in range(1,n+1):
#        if n % i == 0:
#          fac.append(i)
#     return fac
# print(factors(12))

# 13.Count Consonants
#Write a function count_consonants(s) that counts consonants.
#Example: count_consonants("hello") → 3

# def count_consonants(s):
#     vowels = "aeiouAEIOU"
#     consononats = 0
#     for i in s:
#         if i.isalpha() and i not in vowels:
#          consononats += 1
#     return consononats
# print(count_consonants("Hello"))

# 14.Reverse Number
# Write a function reverse_number(n) that returns reverse of number.
# Example: reverse_number(1234) → 4321

# def reverse_number(n):
#     s = str(n)
#     return int(s[::-1])
# print(reverse_number(321))

# 15.Sum of Prime Numbers up to N
# Write a function sum_primes(n) that returns sum of all prime numbers between 1 and n.

# def sum_primes(n):
#      total = 0
#      for num in range(2,n+1):
#           is_prime = True

#           for i in range(2,num):
#                if num%i==0:
#                     is_prime = False
#                     break

#           if is_prime:
#                total+=num

#      return total
# print(sum_primes(10))

# 16.Check Anagram
# # Write a function is_anagram(s1, s2) that checks if both strings are anagrams.
# # Example: is_anagram("listen","silent") → True

# def is_anagram(s1,s2):
#      return sorted(s1) == sorted(s2)
       
    
# print(is_anagram("listen","silnnet"))

# 17.ind Second Largest Number
# Write a function second_largest(lst) that returns second largest element.

def second_largest(lst):
     first_larg = lst[0]
     sec_larg = lst[0]
     for i in lst:
          if i > first_larg:
               sec_larg = first_larg
               first_larg = i
          elif i > sec_larg and i!= first_larg:
               sec_larg = i

     return sec_larg
print(second_largest([2,4,5,6,7]))

          


            
            
                
     






        

