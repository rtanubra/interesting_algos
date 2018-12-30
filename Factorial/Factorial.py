import time

"""
This module is intended to explore the different methods to approach a factorial problem.
Explores two recursive appraoches to compute factorials. 
1. Primary recurrsive sequential approach
    -Slow approach
    -necessary aproach needs to be built to utilize for smaller numbers in fast doubling approach

"""

def sequential_factorial(n):
    #Traditional sequential approach
    if n == 1:
        return 1
    elif n < 1:
        return "FAILED inappropriate input value"
    else:
        return n * sequential_factorial(n-1)
        