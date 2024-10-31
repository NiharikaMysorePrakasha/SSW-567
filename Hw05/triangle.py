# -*- coding: utf-8 -*-
"""
This module classifies triangles based on side lengths.

Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple python program to classify triangles.
@author: jrr
@author: rk
"""
def classify_triangle(a, b, c):
    """
    Classifies the type of triangle based on the lengths of its sides.

    Args:
        a (int): Length of side a.
        b (int): Length of side b.
        c (int): Length of side c.

    Returns:
        str: A string indicating the type of triangle. Possible values are:
             'InvalidInput' if any input is out of range or non-integer,
             'NotATriangle' if the sides do not satisfy the triangle inequality,
             'Equilateral' if all sides are equal,
             'Right' if it is a right triangle,
             'Scalene' if all sides are different,
             'Isosceles' if two sides are equal.
    """
    # Check for invalid inputs
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput' 
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    # Validate triangle inequality theorem
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'
    # Determine the type of triangle
    if a == b == c:
        triangle_type = 'Equilateral'
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        triangle_type = 'Right'
    elif len({a, b, c}) == 3:
        triangle_type = 'Scalene'
    else:
        triangle_type = 'Isosceles'
    return triangle_type
