#write a program usin for loop that allows user 3 attempts to enter the correct password
#if the pass is correct display "Login Successful" and stop using break
#if the password is incorrect,directly display "Wrong Password"

#using for loop

# password = "sal123"

# for i in range(1,4):
#    p1 = input("Enter the password")
#    if p1 == password:
#       print("Login Successful")
#       break
#    else:
#       print("Incorrect password")


# using while

# i=1
# while i < 4:
#    p1 = input("Enter the password")
#    if password == p1:
#       print("Login Successful")
#       break
#    else:
#       print("Incorrect password")
#       i = i + 1

#print numbers from 1 to 10 using while loop
#skip number 4: continue
#stop loop at 7 : break

# i = 1
# while i < 10:
#     if i == 4:
#         i = i + 1
#         continue
#     if i == 7:
#         break
#     print(i)
#     i = i + 1


# check if given number is prime or not

num = int(input("Enter the number :"))
if num==1:
    print("Not a prime number")
else:
    for i in range(2,num):
      if num%2==0:
            print("Not prime")
            break
    else:
        print("Prime number")
    
