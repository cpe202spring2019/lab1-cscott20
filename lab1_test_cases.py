import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1,2,3,4,5,6]), 6)
        self.assertEqual(max_list_iter([8,2,3,4,5,6]), 8)
        self.assertEqual(max_list_iter([8,2,3,8,5,6]), 8)
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([8]), 8)


    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,3]),[3,1])
        self.assertEqual(reverse_rec([3]),[3])
        self.assertEqual(reverse_rec([]),[])

    def test_bin_search(self):
        low = 0
        # val somewhere 3/4 of the way through the list
        list_val =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.assertEqual(bin_search(13, 0, len(list_val)-1, list_val), 13 )
        # val somewhere 1/4 of the way through the list
        list_val =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), 3 )
        # val somewhere 1/2 of the way through the list
        list_val =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 10 )
        # val ALMOST at the end of the list
        list_val =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.assertEqual(bin_search(14, 0, len(list_val)-1, list_val), 14 )
        # val at the very beginning of the list
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )
        # val at the very end of the list
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8 )
        # val somewhere 1/2 of the way through the list
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 5 )
        # what if there's just one element in the list?
        list_val =[5]
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), 0 )
        # what if there are duplicates?
        list_val =[1, 1, 1, 1, 1]
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 2 )
        # what if the list is empty?
        list_val =[]
        self.assertEqual(bin_search(1, 0, -1, list_val), None )
        # What if the list is none?
        list_val = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(1, 0, 0, list_val)


if __name__ == "__main__":
        unittest.main()

    
