"""
Problem 7 powerN
Given base and n that are both 1 or more, 
compute recursively (no loops) the value 
of base to the n power, so powerN(3, 2) is 9 (3 squared).

There is a deliberate built in method but the main function 
below will take the recursivce approach.

"""
import unittest
import random

def powerN(base,power):
    if power <= 1: 
        return base
    else:
        return base * powerN(base,power-1)

class TestPowerN(unittest.TestCase):

    #helper functions
    def built_function(self,base,power):
        return base ** power 
    
    def random_number_generator(self,length):
        my_number = ""
        for x in range(length):
            my_number += str(random.randint(1,9))
        return int(my_number)
    
    #unittests:
    def test_powerN_power1(self):
        inputs = [[3,1],[8,1],[2,1],[11,1],[3,1]]
        outputs = [3,8,2,11,3]
        for x in range(len(inputs)):
            self.assertEqual(powerN(inputs[x][0],inputs[x][1]), outputs[x])

    def test_powerN_setExamples(self):
        inputs = [[3,2],[8,4],[2,3],[11,4],[3,9]]
        outputs = [9,4096,8,14641,19683]
        for x in range(len(inputs)):
            self.assertEqual(powerN(inputs[x][0],inputs[x][1]), outputs[x])
    
    def test_powerN_random_smallBase_smallExp(self):
        for x in range(5):
            base = self.random_number_generator(random.randint(1,2))
            exp = self.random_number_generator(random.randint(1,2))
            tester = self.built_function(base,exp)
            main_fx = powerN(base,exp) 
            #print(base,exp, "expected",tester,"obtained",main_fx)
            self.assertEqual( main_fx, tester)
    

    def test_powerN_random_largeBase_large_Exp(self):
        for x in range(3):
            base = self.random_number_generator(random.randint(2,3))
            exp = self.random_number_generator(random.randint(2,3))
            tester = self.built_function(base,exp)
            main_fx = powerN(base,exp) 
            #print(base,exp, "expected",tester,"obtained",main_fx)
            self.assertEqual( main_fx, tester)
