# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Test for right triangles
    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right Scalene triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,12,13),'Right','5,12,13 is a Right Scalene triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classify_triangle(8,15,17),'Right','8,15,17 is a Right Scalene triangle')

    # Test for equilateral triangles
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    # Test for isosceles triangles
    def testIsoscelesTriangles(self):
        self.assertEqual(classify_triangle(5,5,8), 'Isosceles', '5,5,8 should be isosceles')
        self.assertEqual(classify_triangle(7,7,5), 'Isosceles', '7,7,5 should be isosceles')
        self.assertEqual(classify_triangle(10,10,14), 'Isosceles', '10,10,14 should be isosceles')

    # Test for scalene triangles
    def testScaleneTriangles(self):
        self.assertEqual(classify_triangle(6,7,8), 'Scalene', '6,7,8 should be scalene')
        self.assertEqual(classify_triangle(5,6,7), 'Scalene', '5,6,7 should be scalene')

    # Test for invalid triangles with non-positive sides
    def testInvalidSides(self):
        self.assertEqual(classify_triangle(0, 4, 5), "InvalidInput", "0,4,5 should be invalid")
        self.assertEqual(classify_triangle(-1, 4, 5), "InvalidInput", "-1,4,5 should be invalid")
        self.assertEqual(classify_triangle(3, -1, 5), "InvalidInput", "3,-1,5 should be invalid")
        self.assertEqual(classify_triangle(3, 4, -1), "InvalidInput", "3,4,-1 should be invalid")

    # Test for invalid triangles with triangle inequality rule
    def testInvalidTriangleInequality(self):
        self.assertEqual(classify_triangle(1, 10, 12), "NotATriangle", "1,10,12 should be invalid due to triangle inequality")
        self.assertEqual(classify_triangle(1, 1, 3), "NotATriangle", "1,1,3 should be invalid due to triangle inequality")
        self.assertEqual(classify_triangle(2, 2, 5), "NotATriangle", "2,2,5 should be invalid due to triangle inequality")

    # Test for floating point precision
    def testFloatingPointRightTriangle(self):
        self.assertEqual(classify_triangle(1, 1, 1.41421), "Isosceles", "1,1,1.41421 should be a right isosceles triangle")

    # Edge cases for very large numbers
    def testLargeNumbers(self):
        self.assertEqual(classify_triangle(3000000, 4000000, 5000000), 'InvalidInput', '3000000, 4000000, 5000000 should be a Right Scalene triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
