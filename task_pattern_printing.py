# print kunal nikam 7 times

for i in range(1,8):
    print("Kunal",end=" ")
    print("Nikam")
    print()

# print this pattern

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for i in range(1,8):
    for i in range(1,6):
        print("*",end=" ")
    print()

print("\n")   

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *

for row in range(1,7):
    for column in range(0,row):
        print("*",end=" ")
    print()


print("\n")  

for row in range(1,7):
    for column in range(7-row):
        print("*",end=" ")
    print()