from MeetingRoom import *

class Person:
    inTheRoom = False
    room = MeetingRoom("Random room")

    def __init__(self, inTheRoom):
        self.inTheRoom = inTheRoom

    def entreTheRoom(self):
        if self.inTheRoom == True:
            print("The room is occupied, you cannot entre!")
        else:    
            inTheRoom = True
            room.isAvailable = False    

    def exitTheRoom(self):
        if self.inTheRoom == False:
            print("You cannot exit without entering")
        else:    
            inTheRoom = False
            room.isAvailable = True
