import unittest
import Factorial

class TestFactorial(unittest.TestCase):
    
    def test_sequential_factorial(self):
        #Looping through some relatively low numbers to test sequential factorial
        inputs = [3,8,4,10,-1]
        results = [6,40320,24,3628800,"FAILED inappropriate input value"]
        for x, my_inp in enumerate(inputs):
            self.assertEqual(Factorial.sequential_factorial(inputs[x]),results[x])

