# print numbers between 50 to 200

# start = 50
# while start <= 200:
#     print(start)
#     start = start + 1

# 1.1) Sum of numbers until user enters 0
# Take numbers from user repeatedly and add them until user enters 0.

# num = int(input("Enter your first number :"))
# total = num
# while num!=0:
#     num = int(input("Enter your next number :"))
#     total = total + num
# print(total)

# 2) Count positive and negative numbers until user enters 0
# Ask user for numbers repeatedly.
# Count how many are positive and how many are negative. Stop when user enters 0.

num1 = int(input("Enter the number :"))

cnt_positive = 0
cnt_negative = 0

while num1 != 0:
    if num1 > 0:
        cnt_positive += 1
    else:
        cnt_negative += 1

    num1 = int(input("Enter the number :"))

print("Postive numbers are :",cnt_positive)
print("Negative numbers are :",cnt_negative)


