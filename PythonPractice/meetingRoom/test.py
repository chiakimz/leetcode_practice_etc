import unittest
from main import *

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def check_availability(self):
        room = MeetingRoom()
        self.assertTrue(room.checkAvailability())


if __name__ == '__main__':
    unittest.main()
    