# Project 2:Movie Ticket Pricing System
# Description:
# Create a system to calculate movie ticket price based on age and time of show.
# Rules:
# • Age < 5: Free
# • Age 5–12: ₹100
# • Age 13–60: ₹200
# • Age > 60: ₹120
# • If showtime is before 12 PM, apply 20% discount on price

class movie:
    def __init__(self,age,showtime):
        self.age = age
        self.ticket = 0
        self.showtime = showtime
        self.discount = 1
    def ticket_price(self):
            if self.age > 60:
                self.ticket = 120
            elif self.age >= 13 and self.age <= 60:
                self.ticket = 200
            elif self.age >= 5 and self.age <= 12:
                self.ticket = 100
            elif self.age < 5:
                self.ticket = 0


            if self.showtime < 12 and self.ticket_price != 0:
                 self.ticket = self.ticket - (self.ticket * 0.20)
                 
            if self.ticket == 0:
                 print("Ticket price Free")
            else:
                 print("Ticket price :",int(self.ticket))


film = movie(62,9)
film.ticket_price()

