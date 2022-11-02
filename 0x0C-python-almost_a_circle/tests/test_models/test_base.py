#!/usr/bin/python3
""" A test class for base.py """


import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    """ Tests all the functionalities of the base.py function """

    #def setUp(self):
        #""" Setups the instances of the base class to avoid repetition """
        #self.base2 = Base(123)
        #self.base4 = Base(float('inf'))

    def test_id_argument(self):
        """ Tests if given the id argument the instance will store the id"""
        base1 = Base(123)
        self.assertEqual(base1.id, 123)

    def test_increment_of_nb_objects(self):
        """Tests if __nb_objects is incremented when an instance of the class is created """

        base2 = Base()
        base3 = Base(None)
        self.assertEqual(base2.id, 1)
        self.assertEqual(base3.id, 2)

if __name__ == '__main__':
    unittest.main()
