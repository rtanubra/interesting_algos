"""
inputs:
    1. start: current index 
    2. characters: array of choices - as a string for now.
    3. number_perm: specific selection number to permutate to 

outputs:
    1. a list of possible permutations

Pseudocode - main:
    implement nCr possibilities
    feed each nCr possibilities and 'permutate_string into it.'

Pseudocode - implementation nCr 
            choose_function(my_index, word,chosen,number_perm)
    base case
        if the length of the chosen is same as number perm return the chosen
    else: 
        check if we are in a must pickup scenario 
            -based on how many characters are left in our word and length of current chosen MUST WE PICK THIS UP
            Must pick scenario
                pick the character and recur
            Not a must pick scenario
                1.Pick character and recur
                2.Do not pick character and recur.

Pseudocode for final print permute.

"""

from permutate_string import permute as string_permute

def choose_helper(word,number_perm):
    my_choices = []

    #main function
    def choose_function(my_index, word,chosen,number_perm):
        #base case 
        if my_index >= len(word):
            if len(chosen) == number_perm:
                my_choices.append(chosen)
                return
        else:
            need = number_perm - len(chosen)
            left = len(word) - my_index
            if need == left:
                #Must pickup
                choose_function(my_index+1, word,chosen+word[my_index],number_perm)
                return
            else:
                #Option1 pickup
                choose_function(my_index+1, word,chosen+word[my_index],number_perm)
                #Option2 do not pickup
                choose_function(my_index+1, word,chosen,number_perm)
                return 
    
    #required an input with all unique characters 
    word_list = list(word)
    word_set = list(set(list(word)))
    if len(word_list) != len(word_set):
        return "Incorrect input there are duplicate characters in 'word'."
    else:
        choose_function(0,word,"",number_perm)

    return my_choices

#This is the main function for print_permute
def print_permute(word,number_perm):
    my_choices = choose_helper(word, number_perm)
    all_permutations = [] 
    if type(my_choices) == list:
        for choice in my_choices:
            list_to_add = string_permute(choice)
            print(list_to_add)
            all_permutations.extend(list_to_add )
        return all_permutations
    else:
        return my_choices

