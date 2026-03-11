#Password Validation
#len()<=10
#first letter = uppercase
#last 3 letters : digits

#slicing : using index part of the string,list,tuple extract

#slicing :: varibalename[startvalue: stop value : step value]
#step value bydefault = 1
#startvalue bydefault = 0
#stopvalue bydefault = last index

password = input("Enter the password :")

if len(password) <= 10 :
    if password[0].isupper():
        if password[-3:].isdigit():
            print("Correct")
        else:
            print("Last three characters should be digits")
    else:
        print("First character should be upper")
else:
    print("Incorrect")
 
        