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

"""
from permutate_string import permute as string_permute

my_list = []
start = 0 
word = "reytanub"
number_perm = 3
chosen = ""

def choose_function(my_index, word,chosen,number_perm):
    #base case 
    if my_index >= len(word):
        if len(chosen) == number_perm:
            print(chosen)
            #Empty breaks to return
            
    else:
        choose_function(my_index+1, word[:my_index]+word[my_index:],chosen+word[my_index],number_perm)
        chosen = chosen[:len(chosen)-1]
        choose_function(my_index+1, word,chosen,number_perm)
        #Empty breaks to return 
        return 

choose_function(0,"rey","",2)