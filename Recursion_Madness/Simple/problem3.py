"""
Problem 3
Sumdigits

Given a non-negative int n, 
return the sum of its digits recursively (no loops).
Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), 
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

Interesting this solution works however it is not consitent with numbers beyond 16 digits in length.
"""

def sumDigits(n):
    if len(str(n)) == 1:
        return n
    else:
        return (n % 10) + sumDigits(int(n/10))

#Helper functions needed for testing
import random 
def create_random_numbers(length):
    number = ""
    for x in range(length):
        number += str(random.randint(1,9))
    return int(number)

def tester_loop(n):
    #used for testing
    my_list = list(str(n))
    my_sum= 0
    for x in my_list:
        my_sum+= int(x)
    return my_sum

import unittest
class TestSumDigits(unittest.TestCase):

    def test_three_digits(self):
        for x in range(10):
            number = create_random_numbers(3)
            print("testing",number)
            self.assertEqual(sumDigits(number),tester_loop(number))
    
    def test_short_digits(self):
        for x in range(3):
            number = create_random_numbers(1)
            print("testing",number)
            self.assertEqual(sumDigits(number),tester_loop(number))
        
        for x in range(3):
            number = create_random_numbers(2)
            print("testing",number)
            self.assertEqual(sumDigits(number),tester_loop(number))
    
    def test_long_numbers(self):
        for x in range(4):
            number = create_random_numbers(16)
            print("testing",number)
            self.assertEqual(sumDigits(number),tester_loop(number))
