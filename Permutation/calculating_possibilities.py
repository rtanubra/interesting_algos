"""
Calculating the number of possible permutations is quite simple.
Let:
    total = number of total people to be chosen
    selection = number of people to be selected out of total ORDER MATTERS
    permutations = the total number of permutations possible.
Eq:
    total = total ! / (total-selection) !
"""
#Helper function necessary to calculate permutations.
def iterative_factorial(n):
    prod = 1
    if n < 0: 
        return "FAILED inappropriate input value"
    elif n == 0 :
        return 1
    else:
        for x in range(1,n+1):
            prod *= x
        return prod 

def count_permutations(total, selection):
    return iterative_factorial(total)/ iterative_factorial(total-selection)

