"""
Problem 6 - Arrray 6
Given an array of ints, 
compute recursively if the array contains a 6. 
We'll use the convention of considering only the part of 
the array that begins at the given index. In this way, 
a recursive call can pass index+1 to move down the array. 
The initial call will pass in index as 0.
"""
import unittest
import random

def array6(arr):
    #base case
    if len(arr) == 1:
        if arr[0] == 6:
            return True
        else:
            return False
    else:
        check = arr[0]
        new_arr = arr[1:len(arr)]
        if check == 6 :
            return True
        else:
            return array6(new_arr)

class TestArray6(unittest.TestCase):

    def solution_array6(self,arr):
        #Helper function to iteratively solve the array
        for x in arr:
            if x == 6:
                return True
        return False
    
    def build_random_array6(self,length):
        #Helper function build a random array 
        arr = []
        for x in range(length):
            arr.append(random.randint(1,9))
        return arr
    
    def build_random_array6_No(self,length):
        #Helper function build a random array with no 6 in it
        arr = []
        while len(arr) < length:
            proposed_number = random.randint(1,9)
            if proposed_number != 6:
                arr.append(proposed_number)
        return arr
    
    def test_array6_set_solutions(self):
        print("Testing set tests!\n")
        inputs = [
            [1,2,3,4,5,6],[3,4,7,8,9,10,2],[3,4,7,8,9,10,2,6],[3,6,4,7,8,9,10,2],[3,4,7,8,9,10,2]
        ]
        outputs = [
            True, False, True, True, False
        ]
        for x in range(len(inputs)):
            self.assertEqual( array6(inputs[x]) ,outputs[x])
    
    def test_array6_randomNo(self):
        print("Testing random tests without 6!\n")
        for x in range(10):
            arr = self.build_random_array6_No(random.randint(1,40))
            calculated_answer = array6(arr)
            self.assertEqual(calculated_answer,False)

    def test_array6_random_short(self):
        print("Testing random tests on short arrays (less than length of 10)\n")
        for x in range(10):
            arr = self.build_random_array6(random.randint(1,10))
            calculated_answer = array6(arr)
            solution_answer = self.solution_array6(arr)
            print("Testing",arr,"Expected",solution_answer ,"Output",calculated_answer,"\n")
            self.assertEqual(calculated_answer,solution_answer)
    
    def test_array6_random_long(self):
        print("Testing random tests on short arrays (less than length of 10)\n")
        for x in range(10):
            arr = self.build_random_array6(random.randint(20,40))
            calculated_answer = array6(arr)
            solution_answer = self.solution_array6(arr)
            print("Testing",arr,"\n","Expected",solution_answer ,"Output",calculated_answer,"\n")
            self.assertEqual(calculated_answer,solution_answer)
    
    def test_array6_base_case(self):
        print("Testing base case (arrays of legnth 1)\n")
        inputs = [
            [2],[3],[4],[5],[6]
        ]
        outputs = [False,False,False,False,True]
        for x in range(len(inputs)):
            self.assertEqual( array6(inputs[x]) ,outputs[x])
