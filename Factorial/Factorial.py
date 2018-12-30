import time

"""
This module is intended to explore the different methods to approach a factorial problem.
1. Primary recurrsive sequential approach
    -Slow approach
    -necessary aproach needs to be built to utilize for smaller numbers in fast doubling approach
2. Primary iterative approach 
    -Should have linear time complexity

"""

def recurrsive_factorial(n):
    #Traditional sequential approach
    if n == 1:
        return 1
    elif n==0:
        return 1
    elif n < 1:
        return "FAILED inappropriate input value"
    else:
        return n * recurrsive_factorial(n-1)
        
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
