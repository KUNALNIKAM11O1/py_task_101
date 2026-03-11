# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def show(self):
#         return self.name,self.marks

# s1 = Student("Kunal",22)
# print(s1.show())

# print("\n")

# # Eg.1

# class Std:
#     def __init__(self,name,phy,chem,math):
#         self.name = name
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#     def average(self):
#         self.avg = (self.phy + self.chem + self.math) / 3
#         print(f"Average of marks {self.name} is {self.avg}")

# m1 = Std("Kunal",30,20,40)
# m1.average()

# m1.name = "Rohit"  # we can change value of name from here also
# m1.average()


######################################

# Use of delete keyword in oops
# del : used to delete obj properties or obj itself

class Student:
    def __init__(self,name):
        self.name = name
    
s1 = Student("Kunal")
print(s1.name)

del s1
print(s1.name)
    
