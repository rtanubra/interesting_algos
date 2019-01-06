"""
inputs:
    1. start: current index 
    2. characters: array of choices
    3. number_perm: specific selection number to permutate to 

outputs:
    1. a list of possible permutations
"""

my_list = []
start = 0 
characters = ["R","E","Y","T","A","N","U"]
number_perm = 3
word = ""
def print_permut(start, characters, number_perm, word):
    #base case return 
    if len(word) == number_perm:
        my_list.append(word)
        word = ""
    else:
        #Include this character
        #Exclude this character