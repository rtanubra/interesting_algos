import unittest
import ncr

class TestnCr(unittest.TestCase):
    
    def test_nCr_factorial(self):
        inputs = [[20,12],[8,2],[15,5],[3,2],[4,2],[4,3]]
        results = [125970,28,3003,3,6,4]
        for x, my_inp in enumerate(inputs):
            self.assertEqual(Factorial.recurrsive_factorial(inputs[x]),results[x])
    
    def test_iterative_factorial(self):
        #nCr_factorial depends on this test.
        inputs = [3,8,4,10,-1,1,0]
        results = [6,40320,24,3628800,"FAILED inappropriate input value",1,1]
        for x, my_inp in enumerate(inputs):
            self.assertEqual(Factorial.iterative_factorial(inputs[x]),results[x])

   