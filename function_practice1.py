def absolute(n):
    s = str(n)
    if s[0] == "-":
        return int(s[1:])
    else:
        return n

print(absolute(-90))
print(absolute(89))

print("\n")

def minimum(s):
    m = s[0]
    for i in s:
        if i<m:
            m=i
    print(m)

minimum([8,6,4,5])

print("\n")

print(round(68.764))  # 69
print(round(24.33,0))  # 24.0
print(round(27.548,2))  # 27.55

print("\n")

def roundup(n):
    decimal_part = n - int(n)
    if decimal_part >= 0.5:
        return int(n) + 1
    else:
        return int(n)
    
print(roundup(22.51))

print("\n")

def factorial(f):
    fac = 1
    for i in range(1,f+1):
        fac = fac * i
    return fac
print(factorial(7))


print("\n")

# write a python program that takes a dict
# containing subject names and marks as input and return the total marks of students

data = {"maths":20,"science":55,"sst":60}

def marks(data):
    total = 0
    for key,value in data.items():
        total += value
    return total

print(marks(data))

print("\n")

# return highest marks and subject

m = {"hindi":40,"english":50,"maths":70}

def highest(m): 
    highest_subject = ""
    highest_marks = 0
    for key,value in m.items():
        if value > highest_marks:
            highest_marks = value
            highest_subject = key

    return highest_subject,highest_marks
print(highest(m))

print("\n")

# write a function to calculate average of three numbers

l1 = [4,5,6]

def average(l1):
    total = 0
    for i in l1:
        total += i
    avg = total / len(l1)
    return avg

print(average(l1))

# To check palindrome

def palindrome(s):
    for i in s:
        if s == s[::-1]:
            return True
        else :
            return False
        
print(palindrome("pop"))

print("\n")

# Filter numbers greater than 20 

l2 = [4,14,21,44,3,53,12,43]

def greater(l2):
    result = []
    for i in l2:
        if i > 20:
            result.append(i)
    return result
print(greater(l2))
        
