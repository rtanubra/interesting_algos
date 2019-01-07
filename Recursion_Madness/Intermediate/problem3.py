"""
Problem 3
groupNoAdj
3. groupNoAdj

    Given an array of ints, is it possible to choose a group of some of the ints, 
    such that the group sums to the given target with this additional constraint: 
    If a value in the array is chosen to be in the group, 
    the value immediately following it in the array must not be chosen. 
    (No loops needed.)

    groupNoAdj(0, [2, 5, 10, 4], 12) → true
    groupNoAdj(0, [2, 5, 10, 4], 14) → false
    groupNoAdj(0, [2, 5, 10, 4], 7) → false
"""

def groupNoAdj(start,nums,target,last_chosen=False):
    #base case- if we reach the end of our array we check is our target 0. 
    if start >= len(nums):
        return target == 0 
    else:
        #Check did we select the last number?
        if last_chosen == False:
        #Two basic choices in exploration: 
            #Select the number
            if groupNoAdj(start+1,nums,target-nums[start],last_chosen=True):
                return True
            #Do not select the number
            elif groupNoAdj(start+1,nums,target):
                return True
            #Neither selecting or not selecting the number returns false
            else:
                return False
        else:
            #only one basic choice that is not to pickup the number because we picked up the last number
            if groupNoAdj(start+1,nums,target):
                return True
            else:
                return False

def mini_test():
    start = 0
    my_arrs = [
        [2, 5, 10, 4],[6,6,6,3,6],[10,8,20],
        [2, 5, 10, 4],[2, 5, 10, 4],[6,6,6,3,6],[10,20],[10,8,20],[10,8,20]
    ]
    targets = [
        12,18,30,
        14,7,24,30,18,28
    ]
    outputs = [
        True,True,True,
        False,False,False,False,False,False
    ]
    for i,x in enumerate(outputs):
        obtained = groupNoAdj(start,my_arrs[i],targets[i])
        print(f"Test {i+1}:\nTarget:{targets[i]} inside {my_arrs[i]}")
        if x != obtained :
            print("You Failed","Expected:",x,"Obtained:",obtained)
            break
        else:
            print(f"Passed test {i+1} from {len(outputs)} tests total")
    

#Uncomment below line to run testing. No unittest developed Simple testing function
#mini_test()