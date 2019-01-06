"""
Problem1 GroupSum:
Given an array of ints, is it possible to choose a group of some of the ints, 
such that the group sums to the given target? 
This is a classic backtracking recursion problem. 
Once you understand the recursive backtracking strategy in this problem, 
you can use the same pattern for many problems to search a space of choices. 
Rather than looking at the whole array, our convention is to consider the part of 
the array starting at index start and continuing to the end of the array. 
The caller can specify the whole array simply by passing start as 0. No loops are needed 
-- the recursive calls progress down the array.

groupSum(0, [2, 4, 8], 10) → true
groupSum(0, [2, 4, 8], 14) → true
groupSum(0, [2, 4, 8], 9) → false
groupSum(start,nums,target)
"""

def groupSum(start,nums,target):
    #Base case
    if start >= len(nums):
        return target == 0 
    else:
        #Run two threads either include current number in subgroup
        if groupSum(start+1, nums, target-nums[start]):
            return True 
        #Do not include current number in subgroup.
        elif groupSum(start+1, nums, target):
            return True
        else:
            return False

def mini_test():
    starts = [
        0,0,0,0,0,0
        ]
    nums_s = [
        [2,4,8],[2,4,8],
        [2,4,8],[2,8,9],[12,13,90],
        [2,4,8,2,8,9,12,13,90]
        ]
    targets = [
        10,14,
        9,1,50,
        115
        ]
    answers = [
        True,True,
        False,False,False,
        True
    ]
    for x in range(len(starts)):
        expected = groupSum(starts[x],nums_s[x],targets[x])
        print("Testing",nums_s[x],"Target:",targets[x])
        print("Expected:",answers[x],"Obtained:",expected)
        fail_counter = 0 
        if expected == answers[x]:
            print("Passed Test "+str(x+1))
        else:
            print("Failed Test "+str(x+1))  
            fail_counter += 1
            print("\nTESTING STOPPED FAILED TESTS\n")
            break  

mini_test()