#!/usr/bin/python3
""" A test class for base.py """


import unittest
from models.base import Base

class BaseTestCase(unittest.TestCase):
    """ Tests all the functionalities of the base.py function """

    def setUp(self):
        """ Setups the instances of the base class to avoid repetition """
        self.base1 = base.Base()
        self.base2 = base.Base(123)
        self.base3 = base.Base(None)

    def test_private_nb_objects(self):
        """ Tests if __nb_objects can be accessed """
        with self.assertRaises(AttributeError) as cm:
            self.assertEqual(cm, self.base1.__nb_objects)



if __name__ == '__main__':
    unittest.main()
