#Q1. Write a lambda function to sort a list of tuples based on the second element in descending order.
# Example:
# Input → [(1, 4), (3, 1), (5, 9), (2, 6)]
# Output → [(5, 9), (2, 6), (1, 4), (3, 1)]
# 
l = [(1, 4), (3, 1), (5, 9), (2, 6)]

result = sorted(l, key=lambda x: x[1],reverse=True) 
print(result)

print("\n")

#Q2. Write a lambda function to calculate the square of each number in a list.
# Example:
# Input → [2, 4, 6, 8]
# Output → [4, 16, 36, 64]

l = [2,4,6,8]

square = list(map(lambda x: x*x,l))
print(square)

print("\n")

#Q3. You have a list of dictionaries representing employees:

# employees = [ {'name': 'Amit', 'salary': 50000}, {'name': 'Riya', 'salary': 70000}, {'name': 'Karan', 'salary': 60000} ]

# Using lambda and max(), find the employee with the highest salary.
# Expected Output: {'name': 'Riya', 'salary': 70000}

employees = [ {'name': 'Amit', 'salary': 50000}, {'name': 'Riya', 'salary': 70000}, {'name': 'Karan', 'salary': 60000} ]

highest_salary = max(employees, key=lambda emp: emp["salary"])
print(highest_salary)

print("\n")

# Q4. Using a lambda expression with map(), convert a list of strings to title case (first letter capital).
# Example:
# Input → ["data science", "machine learning", "python"]
# Output → ["Data Science", "Machine Learning", "Python"]

l = ["data science", "machine learning", "python"]

captial = list(map(lambda x: x.title(),l))
print(captial)

print("\n")


# Q5.Write a recursive function to find the nth Fibonacci number.
# Example:
# Input → n = 7
# Output → 13

def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)


n = 7
print(fib(n))


print("\n")


# Q6.Write a recursive function to reverse a string.
# Example:
# Input → "hello"
# Output → "olleh"

def rev_str(s):
    if len(s)==0:
        return s
    return rev_str(s[1:]) + s[0]

str1 = "kunal"
print(rev_str(str1))


print("\n")


# Q7. Create a dictionary where keys are numbers from 1 to 5 and values are their cubes using dictionary comprehension.
# Expected Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

cubes = {k: k*k*k for k in range(1,6)}
print(cubes)


print("\n")


# Q8. Given a dictionary of students and marks, create a new dictionary with only those students who scored more than 50.
# Example:
# Input → {'Amit': 45, 'Riya': 78, 'Neha': 56, 'Sam': 32}
# Output → {'Riya': 78, 'Neha': 56}

student =  {'Amit': 45, 'Riya': 78, 'Neha': 56, 'Sam': 32}

result = {k:v for k,v in student.items() if v>50}
print(result)


print("\n")


# Q9. Write a recursive function to find the sum of digits of a number.
# Example:
# Input → 1234
# Output → 10

def sum_of_digits(n):
    if n == 0:              
        return 0
    return (n % 10) + sum_of_digits(n // 10)


print(sum_of_digits(456))


print("\n")


# Q10. Given a list of words, create a new list containing the lengths of each word.
# Example:
# Input → ["apple", "banana", "kiwi"]
# Output → [5, 6, 4]

def word_length(lst):
    lengths = []
    for w in lst:
        lengths.append(len(w))
    return lengths

lst = ["cricket","football","tennis"]
print(word_length(lst))


print("\n")


# Q11. Write a python class to enter the data of a 5 teaching faculty and display it. (Data of a Faculty: Name, Emp ID, Branch, Salary)


class faculty:
    def __init__(self,name,emp_id,branch,salary):
        self.name = name
        self.emp_id = emp_id
        self.branch = branch 
        self.salary = salary
    def showdata(self):
        print("\n Data of Faculty")
        print("Name",self.name)
        print("Emp ID",self.emp_id)
        print("Brnach",self.branch)
        print("Salary",self.salary)

faculties = []


for i in range(5):
    print(f"\n Enter the data of faculty {i+1}")
    name = input("Enter name :")
    emp_id = input("Enter Emp Id :")
    branch = input("Enter branch :")
    salary = input("Enter the salary")

    teacher = faculty(name,emp_id,branch,salary)
    faculties.append(teacher)

print("\n Faculty Details")
for teacher in faculties:
    teacher.showdata()


print("\n")   


# Q12.Write a python program to demonstrate the working of the banking system.
# a. Create account class with data members (Account No, Account holder name,
# Amount)
# b. Create constructor to initialize data members.
# c. Create member functions (Deposit, withdraw, check balance, and display account details)


class Bank:
    def __init__(self):
        self.account_no = input("Enter account no :")
        self.account_holder_name = input("Enter account holder's name :")
        self.amount = int(input("Enter the Initial Amount :"))

    def withdraw(self,amt):
        if amt > self.amount:
            print("Insufficent Balance")
        else:
            self.amount -= amt
            print(f"{amt} withdrawn successfully")

    def depoist(self,amt):
        self.amount += amt
        print(f"{amt} deposited successfully")

    def check_balance(self):
        print(f"{self.amount} is current balance")

    def display_acc_details(self):
        print("\n Account Number :",self.account_no)
        print("Account holder name :",self.account_holder_name)
        print("Balance",self.amount)

emp1 = Bank()
emp1.display_acc_details()
emp1.depoist(5000)
emp1.withdraw(2000)
emp1.check_balance()


print("\n")


# Q14.Create a class to store the details of two students: std1(Name= Rahul, Age =21, roll
# no=33),
# Std2( Name = Rohit, Age=22, Roll no = 74)
# Write a function to compare the age of both the students, print whether they are equal
# or not equal.

class Student:
    def __init__(self,name,age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no
    def compare(self,other):
        if self.age == other.age:
            print("Both students have equal age")
        else:
            print("Both Students have different age")

s1 = Student("Rahul",22,33)
s2 = Student("Rohit",22,74)

s1.compare(s2)

# Q.13 and 15 not solved






    