"""
In this directory (perhaps this module) we will look at nCr.
Explained as number of possible combinations that can be obtained by taking a sample of items for a larget set.
Shows how many different possible subsets can be made from the larger set. Order within the subset does not matter.
We will explore several methods to figure this out. 
1.Direct iterative approach
2.Factorial equation approach:
    nCr = n! / (r!(n-r)!)


Though the Factorial Equation is indeed interesting and quick
it does not add much insight in terms of how it works. 
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

def factorial_equation_approach(n,r):
    if n > r:
        n_fact= iterative_factorial(n) 
        r_fact = iterative_factorial(r)
        n_r_fact = iterative_factorial(n-r)
        return n_fact / (r_fact * n_r_fact)
    else:
        return "INVALID INPUTS PROVIDED"

print(factorial_equation_approach(10000,18))