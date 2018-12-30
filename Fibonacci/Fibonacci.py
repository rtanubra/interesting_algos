import time

"""
This will explore different ways to approach Fibonacci Sequence:
Reccursive
1. Sequential:
    1,1,2,3,5,8,13.
    -Has base case of n =2
    -if n is higher than two it will look to call the previous fib seq. 
2. Fast Doubling:
    F(2k) = F(K)[2F(k+1)-F(k)]
    F(2k+1) = F(K+1)**2 + F(k)**2
    F(2n-1) = F(n)**2 + F(n-1)**2
    -Unsure of the mathematical proof of the fast doubling approach but significantly reduces the time 
        in large numbers 
3.In the future I look to implement dynamic + fast doubling to reduce the number of threads required and thus continue to speed up the process
"""

def fib_seq(n):
    """
    takes positive integer returns the nth number:
    3 base cases provided before.
    - Seed 0 = 0
    - Seed 1 = 1 
        -therefore f(2) = 0 + 1 
    The recurrsive approach for fibonachi is still not the fastest way to do this.
    """
    if n >= 3:
        return fib_seq(n-1) + fib_seq(n-2)
    elif n == 0:
        return 0
    elif 1 <= n <= 2:
        return 1
    else:
        return "FAILED inappropriate input value"

def fib_dub(n):
    #Fast doubling approach, use this approach if we encounter numbers 
    if n > 10:
        if n % 2 == 0:
            return fib_dub(n/2) * (2*fib_dub(n/2+1) - fib_dub(n/2))
        else:
            my_new_n = (n-1)/2
            return fib_dub(my_new_n+1)**2 + fib_dub(my_new_n)**2 
    else:
        return sequential_factorial(n)
