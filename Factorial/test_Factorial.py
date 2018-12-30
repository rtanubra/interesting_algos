import unittest
import Factorial

class TestFactorial(unittest.TestCase):
    
    def test_recurrsive_factorial(self):
        #Looping through some relatively low numbers to test sequential factorial
        inputs = [3,8,4,10,-1,1,0]
        results = [6,40320,24,3628800,"FAILED inappropriate input value",1,1]
        for x, my_inp in enumerate(inputs):
            self.assertEqual(Factorial.recurrsive_factorial(inputs[x]),results[x])
    
    def test_iterative_factorial(self):
        #Looping through some relatively low numbers to test sequential factorial
        inputs = [3,8,4,10,-1,1,0]
        results = [6,40320,24,3628800,"FAILED inappropriate input value",1,1]
        for x, my_inp in enumerate(inputs):
            self.assertEqual(Factorial.iterative_factorial(inputs[x]),results[x])

