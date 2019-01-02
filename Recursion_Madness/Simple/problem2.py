
"""
Problem2  - Triangle 
We have triangle made of blocks. 
The topmost row has 1 block, the next row down has 2 blocks, 
the next row has 3 blocks, and so on. 
Compute recursively (no loops or multiplication) 
the total number of blocks in such a triangle with 
the given number of rows.
"""

def triangle(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + triangle(n-1)

import unittest
#Full test suite

class TestTriangle(unittest.TestCase):
    
    def test_simple_numbers(self):
        inputs = [0,1,2,3,4,5,8,10]
        results = [0,1,3,6,10,15,36,55]
        for x in range(len(inputs)):
            self.assertEqual(triangle(inputs[x]),results[x])
        print("Passed Simple Tests!\n")

