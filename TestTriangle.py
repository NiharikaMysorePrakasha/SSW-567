# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')
        print("3,4,5 is a Rightangle triangle")

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right')
        print("5,3,4 is a Rightangle triangle")

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
        print('1,1,1 should be equilateral')

    # Test for Isosceles triangles
    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(6,6,4), 'Isosceles')
        self.assertEqual(classifyTriangle(8,8,5), 'Isosceles', '7,7,5 should be isosceles')
        print('5,5,8 should be isosceles')

    # Test for scalene triangles
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(6,7,8), 'Scalene')
        self.assertEqual(classifyTriangle(5,6,7), 'Scalene', '5,6,7 should be scalene')
        print('6,7,8 should be scalene')

    # Test for invalid triangles with non-positive sides
    def testInvalidSides(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'InvalidInput')
        self.assertEqual(classifyTriangle(4, -2, 7), 'InvalidInput', "3,-1,5 should be invalid") 
        print("0,4,5 should be invalid")

    # Test for invalid triangles with triangle inequality rule
    def testInvalidTriangleInequality(self):
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle')
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', "1,1,3 should be invalid due to triangle inequality")
        print("1,10,12 should be invalid due to triangle inequality")

    # Test for floating point precision
    def testFloatingPointRightTriangle(self):
        self.assertEqual(classifyTriangle(1, 1, 1.41421), 'InvalidInput')
        print('1,1,1.41421 is invalid because it contains float value')


    # Edge cases for very large numbers
    def testLargeNumbers(self):
        self.assertEqual(classifyTriangle(6000000, 7000000, 5000000), 'InvalidInput')
        print('6000000, 7000000, 5000000 should be invalid triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
