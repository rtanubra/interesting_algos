"""
permute the function will accept a string as a parameter and outputs all possible
rearrangements of the letters in the string.
The number of possibilities will be len(str)!

This is a recursion backtracking problem. 
"""
def permute(my_str):
    my_list = []
    def permute_helper(my_str, chosen):
        if my_str == "":
            my_list.append(chosen)
        else:
            #Choose/Explore
            for x in range(len(my_str)):
                #Choose
                my_char = my_str[x]
                #Explore
                permute_helper(my_str[:x]+my_str[x+1:],chosen+my_char)
    permute_helper(my_str,"")
    
    return my_list
