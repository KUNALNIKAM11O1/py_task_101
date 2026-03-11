from abc import ABC,abstractclassmethod

class BankApp(ABC):
    def database(self):
        print("Connceted to database")

    @abstractclassmethod
    def security(self):
        pass

    @abstractclassmethod
    def display(self):
        pass

class MobileApp(BankApp):
    def mobile_login(self):
        print("Login into mobile")
        super().database()
        #

    def security(self):
        print("Mobile Security")

    def display(self):
        print("Display")

o1 = MobileApp()
o1.mobile_login()
o1.security()

#o2 = BankApp()