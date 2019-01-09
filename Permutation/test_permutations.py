import unittest
import calculating_possibilities as cs 
from calculating_possibilities import iterative_factorial
import permutate_string as ps 
from print_permute import * 

class TestCalculatingPossibilities(unittest.TestCase):
    
    def test_calculating_possibilities(self):
        print("Testing calculating_possibilities\n")
        totals = [8,8,8,8,10,10,10,10,10,5,5,5,5,5]
        selections = [
            1,8,3,4,
            1,2,5,8,9,
            1,2,3,4,5
            ]
        answers = [
            8,40320,336,1680,
            10,90,30240,1814400,3628800,
            5,20,60,120,120
        ]
        for x in range(len(totals)):
            self.assertEqual(cs.count_permutations(totals[x],selections[x]),answers[x])


class TestPermutateString(unittest.TestCase):
    
    def helper_fx_compare_lists(self,list1,list2):
        #Helper function to test the equality of lists:
        if len(list1) != len(list2):
            return False
        else:
            for x in list1:
                if x not in list2:
                    return False
                if list1.count(x) != list2.count(x):
                    return False
            return True 

    def test_permutate_string_number_check(self):
        print("Testing permutate_string to see if we obtain the correct number of results\n")
        inputs = [
            "12345",
            "123",
            "1234",
            "123456"
        ]
        for x in inputs:
            self.assertEqual(len(ps.permute(x)), iterative_factorial(len(x)))
    
    def test_permutate_string_set_example(self):
        print("Testing permutate_string through set examples to check the resultant list in their entirety \n")
        inputs = ["abc","reyt","ap","1234","12345"]
        outputs = [
            ["abc", "acb", "bac", "bca", "cab", "cba"],
            "erty eryt etry etyr eyrt eytr rety reyt rtey rtye ryet ryte tery teyr trey trye tyer tyre yert yetr yret yrte yter ytre".split(" "),
            "ap pa".split(" "),
            "1234 1243 1324 1342 1423 1432 2134 2143 2314 2341 2413 2431 3124 3142 3214 3241 3412 3421 4123 4132 4213 4231 4312 4321".split(" "),
            "12345 12354 12435 12453 12534 12543 13245 13254 13425 13452 13524 13542 14235 14253 14325 14352 14523 14532 15234 15243 15324 15342 15423 15432 21345 21354 21435 21453 21534 21543 23145 23154 23415 23451 23514 23541 24135 24153 24315 24351 24513 24531 25134 25143 25314 25341 25413 25431 31245 31254 31425 31452 31524 31542 32145 32154 32415 32451 32514 32541 34125 34152 34215 34251 34512 34521 35124 35142 35214 35241 35412 35421 41235 41253 41325 41352 41523 41532 42135 42153 42315 42351 42513 42531 43125 43152 43215 43251 43512 43521 45123 45132 45213 45231 45312 45321 51234 51243 51324 51342 51423 51432 52134 52143 52314 52341 52413 52431 53124 53142 53214 53241 53412 53421 54123 54132 54213 54231 54312 54321".split(" ")
        ]
        for i,x in enumerate(inputs):
            print("-"*5+"Testing:",x,"-"*5)
            self.assertEqual(self.helper_fx_compare_lists(ps.permute(x),outputs[i]), True)
    

class TestPrintPermute(unittest.TestCase):
    
    #two helper functions for our tests
    def dupe_checker(self,my_list):
        new_list = []
        if len(my_list) != len(list(set(my_list))):
            return False
        else:
            for x in my_list:
                new_list.append( "".join(sorted(list(x))) )
            for x in new_list:
                if new_list.count(x) != 1:
                    return False
            return True
    
    def helper_fx_compare_lists(self,list1,list2):
        #Helper function to test the equality of lists:
        if len(list1) != len(list2):
            return False
        else:
            for x in list1:
                if x not in list2:
                    return False
                if list1.count(x) != list2.count(x):
                    return False
            return True 
    
    #Beginning of tests
    def test_choose_helper_no_duplicates(self):
        print("Testing choose_helper for duplicates\n")
        words = [
            "REYT","REYT","REYT",
            "REYTANUB","REYTANUB","REYTANUB"
        ]
        choice_length = [
            2,3,4,
            3,4,5,7
        ]
        for i,x in enumerate(words):
            my_list = choose_helper(x,choice_length[i])
            print(f"Test {i+1}, {x} subset l = {choice_length[i]}, out of {len(words)} tests")
            self.assertEqual(self.dupe_checker(my_list),True)
    
    def test_choose_helper_incorrect_inputsDupeCharacters(self):
        print("Testing choose helper for incorrect inputs\n")
        words = [
            "REYTT","REEYT","RERYT",
            "REYTBANUB","REYTAANUB","REYTUANUB"
        ]
        choice_length =2 
        for i,x in enumerate(words):
            my_list = choose_helper(x,choice_length)
            self.assertEqual(my_list,"Incorrect input there are duplicate characters in 'word'.")
        print("Test complete for incorrect inputs")

    def test_print_permute_incorrect_inputsDupeCharacters(self):
        print("Testing main fx <print_permute> for incorrect inputs\n")
        words = [
            "REYTT","REEYT","RERYT",
            "REYTBANUB","REYTAANUB","REYTUANUB"
        ]
        choice_length =2 
        for i,x in enumerate(words):
            my_list = print_permute(x,choice_length)
            self.assertEqual(my_list,"Incorrect input there are duplicate characters in 'word'.")
        print("Test complete for incorrect inputs")

    def test_print_permute_no_duplicate(self):
        print("Testing print_permute for duplicates\n")
        words = [
            "REYT","REYT","REYT",
            "REYTANUB","REYTANUB","REYTANUB"
        ]
        choice_length = [
            2,3,4,
            3,4,5,7
        ]
        for i,x in enumerate(words):
            my_list = print_permute(x,choice_length[i])
            print(f"Test {i+1}, {x} subset l = {choice_length[i]}, out of {len(words)} tests")
            self.assertEqual(len(my_list),len(set(my_list)))

    def test_print_permute_set_tests(self):
        print("Testing print_permute using set examples for thorough completeness\n")
        words = ["REYT","EDITH"]
        lengths = [2,2]
        outputs = [
            ["RE","ER","RY","YR","RT","TR","EY","YE","ET","TE","TY","YT"],
            ["ED","DE","EI","IE","ET","TE","EH","HE","DI","ID","DT","TD","DH","HD",
            "IT","TI","IH","HI","TH","HT"]
        ]
        for i,x in enumerate(words):
            output_list = print_permute(x,lengths[i])
            print(f"Testing {x}, length {lengths[i]} ")
            self.assertEqual(self.helper_fx_compare_lists(output_list,outputs[i]),True)
        print("TEST RUN COMPLETE!")