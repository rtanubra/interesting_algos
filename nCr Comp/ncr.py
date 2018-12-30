"""
In this directory (perhaps this module) we will look at nCr.
Explained as number of possible combinations that can be obtained by taking a sample of items for a larget set.
Shows how many different possible subsets can be made from the larger set. Order within the subset does not matter.
We will explore several methods to figure this out. 
1.Direct iterative approach
2.Factorial equation approach:
    nCr = n! / (r!(n-r)!)
"""

def iterative_factorial(n):
    #Brought from a previous module as a dependant of implementing the factorial equation.
    prod = 1
    if n < 0: 
        return "FAILED inappropriate input value"
    elif n == 0 :
        return 1
    else:
        for x in range(1,n+1):
            prod *= x
        return prod 