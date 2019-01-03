"""
Count7
Given a non-negative int n, 
return the count of the occurrences of 7 as a digit, 
so for example 717 yields 2. (no loops). 
Note that mod (%) by 10 yields the rightmost digit 
(126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
"""

def count7(n):
    #base case
    if len(str(n)) <= 1:
        if n == 7 :
            return 1
        else:
            return 0
    if n % 10 == 7:
        return 1 + count7(int(n/10))
    else:
        return count7(int(n/10))

#helper function for testing only
def count7_solution(n):
    #utilizes loops to test random numbers and provide solution
    count = 0 
    my_list = list(str(n))
    for x in my_list:
        if x == "7":
            count +=1
    return count

import random
def random_number_generator(length):
    number = ""
    for x in range(length):
        number += str(random.randint(1,9))
    return int(number)

    

import unittest
class TestCount7(unittest.TestCase):
    def test_count7_solution(self):
        #Testing the solution function itself. 
        inputs = [879,1239457,7739561967,2345777,3246,2]
        answers = [1,1,3,3,0,0]
        for x in range(len(inputs)):
            self.assertEqual(count7_solution(inputs[x]),answers[x])
    
    def test_count7_hardCodedSolutions(self):
        #Testing count7 with the same inputs as the tester 
        inputs = [879,1239457,7739561967,2345777,3246,2]
        answers = [1,1,3,3,0,0]
        for x in range(len(inputs)):
            self.assertEqual(count7(inputs[x]),answers[x])

    
    def test_count7_small_numbers(self):
        #test numbers from 1-999
        for x in range(5):
            number =  random_number_generator(random.randint(1,3))
            c7 = count7(number)
            c7s = count7_solution(number)
            print("\nTesting",number,c7,c7s)
            self.assertEqual(c7,c7s) 
    
    def test_count7_large_numbers(self):
        #test numbers from 1,000,000 to 999,999,999,999,999
        for x in range(5):
            number =  random_number_generator(random.randint(7,15))
            c7 = count7(number)
            c7s = count7_solution(number)
            print("\nTesting",number,c7,c7s)
            self.assertEqual(c7,c7s) 
    