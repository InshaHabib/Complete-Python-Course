# Write a class train which has methods to book a ticket, get status (no to seats) and get fare information of train running under indian railways.

from random import randint

class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book_ticket(self, fromm, to):
        print(f"Ticket is booked in train Number = {self.trainNo} from {fromm} to {to}")
        
    def getstatus(self):
        print(f"Train number = {self.trainNo} is running on time.")
    
    def getfareinfo(self, fromm, to):
        print(f"Ticket fare in train Number = {self.trainNo} from {fromm} to {to} is {randint(222, 555)}")
    
t = train(int(input("Enter train number = ")))
t.book_ticket("Naushera", "Rawalpindi")
t.getstatus()
t.getfareinfo("Naushera", "Rawalpindi")

