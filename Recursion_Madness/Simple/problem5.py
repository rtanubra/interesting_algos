"""
Problem5 - ChangePi 

Given a string, 
compute recursively (no loops) a new string where all 
appearances of "pi" have been replaced by "3.14".
"""
import unittest

#Main function
def change5_py(str):
    if len(str) <= 2:
        if str == "Pi":
            return "3.14"
        else:
            return str
    else:
        check_str = str[:1]
        rest = str[1:]
        if check_str == "P":
            check_str = str[:2]
            rest = str[2:]
            if check_str == "Pi":
                return "3.14"+change5_py(rest)
            else:
                return check_str+change5_py(rest)
        else:
            return check_str+change5_py(rest)

#A method for simple testing through prints no unittest required   
def mini_test():
    inputs = [
        "","PI","Pi",
        "PIPijabPiberPi","PiabPiPibyPI",
        "LPiorum",
        "abby","Rey","Lorum"
    ]
    for x in inputs:
        print(x)
        print("obtained:",change5_py(x),"\n")

#mini_test() #uncomment to view a mini test run.

#Full test suite run through python3 -m unittest problem5.py
class TestChange5_py(unittest.TestCase):

    def test_change5_multiplePi(self):
        print("Testing strings that require multiple changes\n")
        inputs = ["PIPijabPiberPi","","PiabPiPibyPI","PiRePiyPi","LPiorumPi"]
        outputs = ["PI3.14jab3.14ber3.14","","3.14ab3.143.14byPI","3.14Re3.14y3.14","L3.14orum3.14"]
        for i,x in enumerate(inputs):
            self.assertEqual(change5_py(x),outputs[i])

    def test_change5_singlePi(self):
        print("Testing strings that require a single change\n")
        inputs = ["jabPiber","","Piabby","ReyPi","LPiorum"]
        outputs = ["jab3.14ber","","3.14abby","Rey3.14","L3.14orum"]
        for i,x in enumerate(inputs):
            self.assertEqual(change5_py(x) , outputs[i])

    def test_change5_null_test(self):
        #Create tests with no change in the string including empty string.
        print("Testing strings that require no change\n")
        inputs= ["jabber","","abby","Rey","Lorum"]
        for x in inputs:
            self.assertEqual( change5_py(x) , x)
        
    def test_change5_base_case(self):
        #base case - len of string <=2
        print("Testing base cases, strings of lenghts 2 or less")
        inputs = ["","PI","Pi","Jo","J","R","P"]
        outputs= ["","PI","3.14","Jo","J","R","P"]
        for i,x in enumerate(inputs):
            self.assertEqual(change5_py(x),outputs[i])

