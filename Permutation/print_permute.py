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
    else: #2 main choices, include this character or exclude this character w backtracking
        select this letter and place in chosen explore recursively
            BACKTRACK by removing this letter
        elect not to place this letter into chosen explore recursively
            BACKTRACK by removing this letter 
REY-choose 2
picked R
    Picked  *
    NOT PICKED R
        MUST PICK RY *
not picked 
    MUST PICK EY *

EDITH choose 3
picked E
    picked ED
        picked EDI *********
        not picked ED
            picked EDT *******
            not picked ED
            MUSTPICK EDH *******
    not picked E
        picked EI
            picked EIT ******
            not picked EI
                MUST PICK EIH ******
        not picked E
            MUST PICK ETH ******
not picked 
    picked D
        picked DI
        not picked D
            MUST PICK DTH ********
    not picked 
"""
from permutate_string import permute as string_permute

my_list = []
start = 0 
word = "reytanub"
number_perm = 3
chosen = ""
def choose_helper(word,number_perm):
    my_choices = []
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
choose_function(0,"reytan","",2)