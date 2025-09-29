# Can you change the self-parameter inside a class to something else say ("Insha"). Try changing self to "slf" or "insha" and see the effects.
# Answer:- yes, we can change the self parameter to any other name, but it is a convention to use self. Here is an example with "slf" and "insha".

from random import randint
class train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    
    def book_ticket(insha, fromm, to):
        print(f"Ticket is booked in train Number = {insha.trainNo} from {fromm} to {to}")
        
    def getstatus(self):
        print(f"Train number = {self.trainNo} is running on time.")
    
    def getfareinfo(self, fromm, to):
        print(f"Ticket fare in train Number = {self.trainNo} from {fromm} to {to} is {randint(222, 555)}")
    
t = train(int(input("Enter train number = ")))
t.book_ticket("Naushera", "Rawalpindi")
t.getstatus()
t.getfareinfo("Naushera", "Rawalpindi")

