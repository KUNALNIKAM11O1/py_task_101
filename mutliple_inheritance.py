# Mutliple Inheritance

# Problem 1: Father and Mother → Child
# Create classes:
# Father with method skills_father()
# Mother with method skills_mother()
# Child inherits from both and has method skills_child()
# Create object of Child and call all methods.

class Father():
    def __init__(self,skill_father):
        self.skill_father = skill_father

    def skills_father(self):
        print(self.skill_father)

class Mother():
    def __init__(self,skill_mother):
        self.skill_mother = skill_mother
    
    def skills_mother(self):
        print(self.skill_mother)

class Child(Father,Mother):
    def __init__(self, skill_father,skill_mother):
        Father.__init__(self, skill_father)
        Mother.__init__(self, skill_mother)

    def child_skills(self):
        print("Fast")
       
        
     

child1 = Child("Tall","Fair")
child1.skills_father()
child1.skills_mother()
child1.child_skills()

print("\n")

# Problem 3: Camera + Phone → SmartPhone
# Create classes:
# Camera with method take_photo()
# Phone with method make_call()
# SmartPhone inherits both and has method browse_internet()

class Camera():
    def __init__(self,photo):
        self.photo = photo

    def take_photo(self):
        print(self.photo)

class Phone():
    def __init__(self,call):
        self.call = call

    def make_call(self):
        print(self.call)

class SmartPhone(Camera,Phone):
    def __init__(self,photo,call):
        Camera.__init__(self,photo)
        Phone.__init__(self,call)

    def browse_Internet(self):
        print("Browsing Internet")

samsung = SmartPhone("Clicks Photo","Makes call")
samsung.take_photo()
samsung.make_call()
samsung.browse_Internet()

print("\n")

# Problem: Writer + Speaker → AuthorSpeaker
# Create the following classes:
# 1️⃣ Writer class
# Constructor should take book_name
# Method write_book() should print the book name.
# 2️⃣ Speaker class
# Constructor should take topic
# Method give_speech() should print the speech topic.
# 3️⃣ AuthorSpeaker class
# Inherits from both Writer and Speaker
# Constructor should initialize both parent classes.
# Method motivate_people() should print a motivational message using the book and topic.
# 4️⃣ Create an object and call all methods.

class Writer():
    def __init__(self,book_name):
        self.book_name = book_name

    def write_book(self):
        print(self.book_name)

class Speaker():
    def __init__(self,topic):
        self.topic = topic

    def give_speech(self):
        print(self.topic)

class AuthorSpeaker(Writer,Speaker):
    def __init__(self, book_name,topic):
       Writer.__init__(self,book_name)
       Speaker.__init__(self,topic)

    def motivate_people(self):
        print("Your day will come")

rabi = AuthorSpeaker("Ryzen","Express")
rabi.write_book()
rabi.give_speech()
rabi.motivate_people()