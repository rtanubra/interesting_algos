"""
Problem 4
groupSum5

    Given an array of ints, 
    is it possible to choose a group of some of the ints, 
    such that the group sums to the given target 
    with these additional constraints: all multiples of 5 in the array must be included 
    in the group. 
    
    If the value immediately following a multiple of 5 is 1, it must not be chosen. 
    (No loops needed.)

    groupSum5(0, [2, 5, 10, 4], 19) → true
    groupSum5(0, [2, 5, 10, 4], 17) → true
    groupSum5(0, [2, 5, 10, 4], 12) → false

Pseudocode:
    base case 
        if start is beyond the length of our array we return whether or not we achieved our target

    else:
        if multiple of 5:
            if last number in array 
                include and explore through recursion
            else not the last number in array
                if preceeds a 1:
                    do not include explore through recursion
                    FAIL CASE
                else:
                    include and explore through recursion
                    FAIL CASE
        else:
            explore a pickup through recursion
            explore a not pickup through recursion
            FAIL CASE


"""

def groupSum5(start,nums,target):
    #Base case
    if start >= len(nums):
        return target == 0 
    else:
        #Multiple of 5
        if nums[start] % 5 == 0:
            #This is NOT a final number
            if start < len(nums)-1:
                #Followed by a 1 do not pickup
                if nums[start+1] == 1:
                    if groupSum5(start+1, nums, target):
                        return True
                    else:
                        return False
                #Not Followed by a 1 pickup
                else:
                    if groupSum5(start+1, nums, target-nums[start]):
                        return True
                    else:
                        return False
            #This is a final number must pickup 
            else:
                if groupSum5(start+1, nums, target-nums[start]):
                    return True
                else:
                    return False
        #Not multiple of 5
        else:
            #Run two threads either include current number in subgroup
            if groupSum5(start+1, nums, target-nums[start]):
                return True 
            #Do not include current number in subgroup.
            elif groupSum5(start+1, nums, target):
                return True
            else:
                return False

def mini_test():
    start = 0
    my_arrs = [
        [2, 5, 10, 4],[2, 5, 10, 4],[2, 5, 10,1,4],[2, 5, 10, 4,2, 5, 10,1,4],
        [2, 5, 10, 4],[2, 5, 10,1,4],[2, 5, 10, 4,2, 5, 10,1,4]
    ]
    targets = [
        19,17,9,28,
        12,15,38
    ]
    outputs = [
        True,True,True,True,
        False,False,False
    ]
    for i,x in enumerate(outputs):
        obtained = groupSum5(start,my_arrs[i],targets[i])
        print(f"Test {i+1}:\nTarget:{targets[i]} inside {my_arrs[i]}")
        if x != obtained :
            print("You Failed","Expected:",x,"Obtained:",obtained)
            break
        else:
            print(f"Passed test {i+1} from {len(outputs)} tests total")

#Uncomment/comment below line to toggle testing. No unittest implementation
#mini_test()