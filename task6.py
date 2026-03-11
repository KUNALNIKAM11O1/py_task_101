# driving license verification
#age>20 ad has_license="yes"

# age = int(input("Enter your age :"))

# if age >20 :
#     license = input("Do you have license(Yes/No) :").capitalize()
#     if license == "Yes":
#         print("You can drive")
#     else :
#         print("Bring your license")
# else :
#     print("You are not eligible for driving")

# bank loan approval

# salary = float(input("Enter your salary :"))

# if salary >=30000 :
#     credit_score = int(input("Enter your credit score :"))
#     if credit_score >=700:
#      home_owner = input("Are you home owner(Yes/No) :").lower()
#      if home_owner == "yes":
#         print("Your loan is approved")
#      else :
#         print("you should be owner of home")
#     else :
#        print("Your credit score must be 700 or above")
# else :
#     print("Your home loan is not approved")


# Employee bonus calculation

# exp = int(input("Enter your years of experince :"))

# if exp >= 10 :
#    bonus = int(20000)
# elif exp >=5 :
#    bonus = int(10000)
# elif exp >=2:
#    bonus = int(5000)
# else :
#    bonus = 0

# print("You have received bonus :",bonus)

# Online shopping system

price = int(input("Enter your product's price :"))

if price >= 30000 :
    offer = price * 0.5
elif price >=20000:
    offer = price * 0.3
elif price >=10000:
    offer = price * 0.1
elif price >=5000:
    offer = price * 0.05
else :
    offer = 0

print("Final amount ", price - offer)



      
        


