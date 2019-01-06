"""
Problem2 GroupSum6:
Given an array of ints, is it possible to choose a group of some of the ints, 
such that the group sums to the given target? 
This is a classic backtracking recursion problem. 
Once you understand the recursive backtracking strategy in this problem, 
you can use the same pattern for many problems to search a space of choices. 
Rather than looking at the whole array, our convention is to consider the part of 
the array starting at index start and continuing to the end of the array. 
The caller can specify the whole array simply by passing start as 0. No loops are needed 
-- the recursive calls progress down the array.

groupSum6(0, [2, 4, 8], 10) → true
groupSum6(0, [2, 4, 8], 14) → true
groupSum6(0, [2, 4, 8], 9) → false
groupSum6(0, [2, 4, 8,6 ], 10) → false
groupSum6(start,nums,target)
"""

def groupSum6(start, nums, target):
    #base Case
    if start >= len(nums):
        return target == 0
    else:
        if nums[start] == 6:
        #Next number is 6, pickup - True or pickup False
            if groupSum6(start+1, nums, target-nums[start]):
                return True
            else:
                return False 
        else:
        #Next number is not 6 : 2 choices:
            if groupSum6(start+1, nums, target-nums[start]):
                return True
            elif groupSum6(start+1, nums, target):
                return True
            else:
                return False


def mini_test():
    starts = [
        0,0,0,0,0,0,0,0,0,0
        ]
    nums_s = [
        [2,4,8],[2,4,8],[2,4,6,8],
        [2,4,8],[2,8,9],[12,13,90],
        [2,4,8,2,8,9,12,13,90,6],
        [2,4,8,6,6],[2,4,8,6],
        [2,4,6,6,6,6,6,6]
        ]
    targets = [
        10,14,10,
        9,1,50,
        121,
        10,14,
        24
        ]
    answers = [
        True,True,True,
        False,False,False,
        True,
        False,True,
        False
    ]
    for x in range(len(starts)):
        expected = groupSum6(starts[x],nums_s[x],targets[x])
        print("Testing",nums_s[x],"Target:",targets[x])
        print("Expected:",answers[x],"Obtained:",expected)
        if expected == answers[x]:
            print("Passed Test "+str(x+1))
        else:
            print("Failed Test "+str(x+1))  
            print("\nTESTING STOPPED FAILED TESTS\n")
            break  

#Uncomment to run mini_test
#mini_test()