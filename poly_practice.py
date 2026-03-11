# Polymorphism

# 1.Animal Sound

# Create a parent class Animal with a method sound().
# Create two child classes Dog and Cat that override the sound() method to print their own sounds.

class Animal:
    def intro(self):
        print("There are many types of animals")

    def sound(self):
        print("Different animals make different sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a1 = Animal()
a1.intro()
a1.sound()

a2 = Dog()
a2.sound()

a3 = Cat()
a3.sound()

print("\n")

# 5. Bank Interest
# Create a parent class Bank with a method interest_rate().
# Create child classes SBI, HDFC, and ICICI that override the method and display different interest rates.

class Bank:
    def interest_rate(self):
        print("The bank has interest rate of 8%")

class SBI(Bank):
    def interest_rate(self):
        print("SBI has interest rate of 6%")

class HDFC(Bank):
    def interest_rate(self):
        print("HDFC has interest rate of 9%")

class ICICI(Bank):
    def interest_rate(self):
        print("ICICI has interest rate of 11%")

banks = [Bank(), SBI(), HDFC(), ICICI()]

for b in banks:
    b.interest_rate()