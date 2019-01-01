import unittest
import prime_fact

class TestPrimeFact(unittest.TestCase):
    
    def test_prime_fact_iter_small_numbers(self):
        #test small numbers
        inputs = [100,88,72,10,46,39]
        results = [97,83,71,7,43,37]
        for x, curr_inp in enumerate(inputs):
            self.assertEqual(iter_prime_fact(curr_inp),results[x])