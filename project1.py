# Project 1: Smart Traffic Fine Management System
# Project Description:
# Build a Python program that helps a traffic police department automatically calculate fines for drivers 
# based on their speed, age, and seatbelt usage.
# Requirements:
# 1. Inputs:
# o Driver Name
# o Driver Age
# o Speed of the Vehicle (in km/h)
# o Whether the driver was wearing a seatbelt (yes or no)
# 2. Logic & Conditions:
# o Speed Limit: 60 km/h
# o Fine Rules:
# ▪ If speed > 60 and ≤ 80 → Fine ₹500
# ▪ If speed > 80 and ≤ 100 → Fine ₹1000
# ▪ If speed > 100 → Fine ₹2000
# o If no seatbelt → Add ₹500 to the fine.
# o If driver age < 18 → Display: "Underage driving is illegal. Report to higher authority."
# o If no fine → Display: "No fine. Drive safely!"
# 3. Output:
# o Driver name
# o Age
# o Speed
# o Seatbelt status
# o Fine amount (if applicable)
# o Final message


# 1. PROCEDURAL METHOD

# driver_name = input("Enter Driver's name: ")
# driver_age = int(input("Enter Driver's age: "))
# speed_of_vehicle = int(input("Enter speed of vehicle (km/h): "))
# seatbelt = input("Whether the driver was wearing a seatbelt (yes or no)?: ").lower()

# fine = 0

# print("\n----- Traffic Rule Report -----")
# print("Driver's name:", driver_name)
# print("Driver's age:", driver_age)
# print("Speed of vehicle:", speed_of_vehicle, "km/h")
# print("Seatbelt:", seatbelt)

# # Underage condition
# if driver_age < 18:
#     print("Message: Underage driving is illegal. Report to higher authority.")

# else:
#     # Speed fine rules
#     if speed_of_vehicle > 60 and speed_of_vehicle <= 80:
#         fine = 500
#     elif speed_of_vehicle > 80 and speed_of_vehicle <= 100:
#         fine = 1000
#     elif speed_of_vehicle > 100:
#         fine = 2000

#     # Seatbelt fine rule
#     if seatbelt == "no":
#         fine += 500
#         print("Message: No Seatbelt. Additional fine added.")

#     # Final output
#     if fine == 0:
#         print("Fine Amount: ₹0")
#         print("Message: No fine. Drive safely!")
#     else:
#         print("Fine Amount: ₹", fine)
#         print("Message: Please pay the fine and follow traffic rules.")


# 2.OOPs Method

class Traffic:
    def __init__(self, name, age, speed, seatbelt):
        self.name = name
        self.age = age
        self.speed = speed
        self.seatbelt = seatbelt.lower()
        self.fine = 0

    def cal_fine(self):
        # If underage, no fine calculation
        if self.age < 18:
            return

        # Speed fine rules
        if 60 < self.speed <= 80:
            self.fine = 500
        elif 80 < self.speed <= 100:
            self.fine = 1000
        elif self.speed > 100:
            self.fine = 2000

        # Seatbelt fine rule
        if self.seatbelt == "no":
            self.fine += 500

    def display_report(self):
        # Heading based on violation
        if self.age < 18 or self.fine > 0:
            print("\n----- Traffic Rule Violation Report -----")
        else:
            print("\n----- No Violation Report -----")

        print("Driver Name:", self.name)
        print("Driver Age:", self.age)
        print("Speed:", self.speed, "km/h")
        print("Seatbelt:", self.seatbelt)

        # Underage message
        if self.age < 18:
            print("Message: Underage driving is illegal. Report to higher authority.")
        else:
            print("Fine Amount: ₹", self.fine)

            if self.fine == 0:
                print("Message: No fine. Drive safely!")
            else:
                print("Message: Please pay the fine and follow traffic rules.")



name = input("Enter Driver Name: ")
age = int(input("Enter Driver Age: "))
speed = int(input("Enter Speed of Vehicle (km/h): "))
seatbelt = input("Was the driver wearing seatbelt? (yes/no): ")

driver = Traffic(name, age, speed, seatbelt)
driver.cal_fine()
driver.display_report()

                





    