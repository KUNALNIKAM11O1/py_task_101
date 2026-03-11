# single inheritance
# Eg 1

class user:
    def __init__(self):
        self.name = "Kunal"
        self.gender = "Male"

    def login(self):
        print("Login")

# child
# what gets inherited
# constructor,non private methods,non private variables

class student(user):
    def __init__(self):
        self.roll_no = 123
    def enroll(self):
        print("Enroll")

s1 = student()
s1.login()
s1.enroll()

print("\n")

# Eg 2

class Player:
    def __init__(self,name,id,age,loc):
        self.name = name
        self.id = id
        self._age = age
        self.__loc = loc

    def signin(self):
        print("Signin")

class Crickter(Player):
    def register(self):
        print("register")
        print(self.name)
        print(self.id)
        print(self._age)
      #  print(self.__loc)

p1 = Crickter("Raina",3,39,"UP")
p1.signin()
p1.register()

print("\n")

############################

# 2. Multilevel Inheritance
# super() is a built-in function used to access methods and constructors of the parent class in inheritance.

# Problem 1: Person → Employee → Manager
# Create a program where:
# Person class has method display_name()
# Employee class inherits Person and has method display_salary()
# Manager class inherits Employee and has method display_department()
# Create an object of Manager and display all details.

class Person:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print(self.name)

class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary

    def display_salary(self):
        print(self.salary)
      

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def display_department(self):
        print(self.department)
        

emp = Manager("Kunal",230000,"Hr")
emp.display_name()
emp.display_salary()
emp.display_department()

print("\n")

# class Parent:
#     def __init__(self):
#         print("Parent constructor executed")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child constructor executed")

# obj = Child()

# Problem 2: Animal → Dog → Puppy
# Create classes where:
# Animal class has method eat()
# Dog class inherits Animal and has method bark()
# Puppy class inherits Dog and has method weep()
# Create an object of Puppy and call all methods.

class Animal:     
    def __init__(self,eat):
        self.eat = eat

    def eating(self):
        print(self.eat)

class Dog(Animal):
    def __init__(self,eat,bark):
        super().__init__(eat)
        self.bark = bark

    def barking(self):
        print(self.bark)

class Puppy(Dog):
    def __init__(self, eat, bark,weep):
        super().__init__(eat,bark)
        self.weep = weep

    def weeping(self):
        print(self.weep)

sunny = Puppy("Sunny is eating","Sunny is barking","Sunny is weeping")
sunny.eating()
sunny.barking()
sunny.weeping()

print("\n")

# Problem 4: Student → CollegeStudent → GraduateStudent
# Create classes where:
# Student has method get_name()
# CollegeStudent inherits Student and has method get_course()
# GraduateStudent inherits CollegeStudent and has method get_research_topic()

class Student:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        print(self.name)

class CollegeStudent(Student):
    def __init__(self,name,course):
        super().__init__(name)
        self.course = course
    def get_course(self):
        print(self.course)

class GraduateStudent(CollegeStudent):
    def __init__(self, name, course,research_topic):
        super().__init__(name, course)
        self.research_topic = research_topic
    def get_reserach_topic(self):
        print(self.research_topic)

std = GraduateStudent("Kunal","BE","AIML")
std.get_name()
std.get_course()
std.get_reserach_topic()
    
        