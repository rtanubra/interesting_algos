"""
In this directory (perhaps this module) we will look at nCr.
Explained as number of possible combinations that can be obtained by taking a sample of items for a larget set.
Shows how many different possible subsets can be made from the larger set. Order within the subset does not matter.
We will explore several methods to figure this out. 
1.Recurrsive approach
    -this approach provides the most intuition but I believe is the most difficult to explore
    -that is why I am also looking to enable the prints to visualize this algorithm
    -Important to note this is by far the slowest. 
2.Factorial equation approach:
    nCr = n! / (r!(n-r)!)
    -abstract reasoning but this tends to be the mathematical approach.
3.Multiplicative approach
    -logic behind this I believe is slightly abstract, similar to factorial approach but rearranged.


Though the Factorial Equation is indeed interesting and quick
it does not add much insight in terms of how it works. 
"""

#Brought from a previous module as a dependant of implementing the factorial equation.
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

def factorial_equation_approach(n,r):
    if n > r:
        n_fact= iterative_factorial(n) 
        r_fact = iterative_factorial(r)
        n_r_fact = iterative_factorial(n-r)
        return n_fact / (r_fact * n_r_fact)
    else:
        return "INVALID INPUTS PROVIDED"

def recursive_nck(n,k):
    if k == 0 or k ==1:
        return 1
    else:
        return recursive_nck(n-1,k) + recursive_nck(n-1,k-1)

def multiplicative_ncr(n,r):
    result = 1
    for i in range(1,k+1):
        result = result * (n-(k-i))/i
    return result

