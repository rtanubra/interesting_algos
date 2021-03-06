"""
Problem 8 - countX
Given a string, compute recursively (no loops) 
the number of lowercase 'x' chars in the string
"""

def problem8(my_str):
    if len(my_str) <= 1:
        if my_str == "x":
            return 1
        else:
            return 0
    else:
        if my_str[len(my_str)-1] == "x":
            return 1 + problem8(my_str[0:len(my_str)-1])
        else:
            return problem8(my_str[0:len(my_str)-1])

#Helper functions for testing
import random
def create_random_string(word_length):
    #create random tests
    possible_letters = ["a","x","X","4","o","a","b","g","d","9"]
    word = ""
    for x in range(word_length):
        word += possible_letters[random.randint(0,len(possible_letters)-1)]
    return word

def implement_test(my_str):
    count = 0 
    for x in my_str:
        if x == "x":
            count+=1 
    return count

import unittest

class TestProblem8(unittest.TestCase):

    def test_problem8_set_problems(self):
        inputs = ["xxhixx","xhixhix","hi","xxxasadbsdajsdlxx"]
        outputs = [4,3,0,5]
        for x in range(len(inputs)):
            self.assertEqual( problem8(inputs[x]), outputs[x])
    
    def test_implement_test(self):
        inputs = ["xxhixx","xhixhix","hi","xxxasadbsdajsdlxx"]
        outputs = [4,3,0,5]
        for x in range(len(inputs)):
            self.assertEqual( implement_test(inputs[x]), outputs[x])

    def test_problem8_random_long(self):
        for x in range(6):
            number = random.randint(18,40)
            word = create_random_string(number)
            iterative = implement_test(word)
            recursive = problem8(word)
            print(word,"answer:",iterative,"obtained:",recursive,"\n")
            self.assertEqual(iterative, recursive)
    
    def test_problem8_random_short(self):
        for x in range(6):
            number = random.randint(0,10)
            word = create_random_string(number)
            iterative = implement_test(word)
            recursive = problem8(word)
            print(word,"answer:",iterative,"obtained:",recursive,"\n")
            self.assertEqual(iterative, recursive)
        
    
