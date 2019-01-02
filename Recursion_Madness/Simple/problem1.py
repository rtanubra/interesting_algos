"""
We have bunnies standing in a line, numbered 1, 2, ... 
The odd bunnies (1, 3, ..) have the normal 2 ears. 
The even bunnies (2, 4, ..) we'll say have 3 ears, 
because they each have a raised foot. 
Recursively return the number of "ears" in the bunny line 1, 2, ... n 
(without loops or multiplication).
"""

def bunny_ears(n):
    if n == 0:
        return 0
    elif n < 0:
        return "FALSE INPUT"
    elif n == 1:
        return 2
    elif n == 2:
        return 5
    else:
        if n % 2 == 0 :
            return 3 + bunny_ears(n-1)
        else:
            return 2 + bunny_ears(n-1)

#Full test suite
import unittest

class TestBunny_ears(unittest.TestCase):

    def test_small_numbers(self):
        inputs = [0,1,2,3,4,5,10,11]
        results = [0,2,5,7,10,12,25,27]
        for x in range(len(inputs)):
            self.assertEqual(bunny_ears(inputs[x]),results[x])
        print("Completed tests with small numbers")

    def test_errors(self):
        inputs = [-1,-2,-10]
        for x in range(len(inputs)):
            self.assertEqual(bunny_ears(inputs[x]),"FALSE INPUT")
        print("Completed tests that should yield errors")