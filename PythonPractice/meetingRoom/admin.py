from MeetingRoom import*

class Admin:
    room = MeetingRoom("Random room")
    meetingRooms = []

    def add(self, room):
        self.meetingRooms.append(room)

    def show(self, meetingRooms):
        for i in meetingRooms:
            print(i)
