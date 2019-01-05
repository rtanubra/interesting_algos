"""
Problem5 - ChangePi 

Given a string, 
compute recursively (no loops) a new string where all 
appearances of "pi" have been replaced by "3.14".
"""
import unittest

def change5_py(str):
    pass

class TestChange5_py(unittest.TestCase):

    def test_change5_multiplePi(self):
        print("Testing strings that require a multiple change\n")
        inputs = ["PIPijabPiberPi","","PiabPiPibyPI","PiRePiyPi","LPiorumPi"]
        ouputs = ["PI3.14jab3.14ber3.14","","3.14ab3.143.14byPI","3.14Re3.14y3.14","L3.14orum3.14"]
        for i,x in enumerate(inputs):
            self.assertEqual(change5_py(x),outputs[i])

    def test_change5_singlePi(self):
        print("Testing strings that require a single change\n")
        inputs = ["jabPiber","","Piabby","ReyPi","LPiorum"]
        ouputs = ["jab3.14ber","","3.14abby","Rey3.14","L3.14orum"]
        for i,x in enumerate(inputs):
            self.assertEqual(change5_py(x) , outputs[i])

    def test_change5_null_test(self):
        #Create tests with no change in the string including empty string.
        print("Testing strings that require no change\n")
        inputs= ["jabber","","abby","Rey","Lorum"]
        for x in inputs:
            self.assertEqual( change5_py(x) , x)
