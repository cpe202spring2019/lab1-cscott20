import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location("San Lui", 35, 20.7)
        self.assertEqual(repr(loc),"Location('San Lui', 35, 20.7)")
        self.assertNotEqual(repr(loc),"Location('San', 35, 20.7)")
        self.assertNotEqual(repr(loc),"Location('San Lui', 20, 20.7)")
        self.assertNotEqual(repr(loc),"Location('San Lui', 35, 20)")
        self.assertNotEqual(repr(loc),"Location('San', 3, 2)")
    

if __name__ == "__main__":
        unittest.main()
