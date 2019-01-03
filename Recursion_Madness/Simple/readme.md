This directory wills store several recursion problems and their tests. Recursion is an important part of programming and quite a concept to grasp and play with. Therefore deliberate practice can benefit the developer.

1. BunnyEars2 - completed

    We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

2. Triangle - completed

    We have triangle made of blocks. 
    The topmost row has 1 block, the next row down has 2 blocks,
    the next row has 3 blocks, and so on. 
    Compute recursively (no loops or multiplication) 
    the total number of blocks in such a triangle with 
    the given number of rows.

3. SumDigits - completed with caveats

    Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

4. Count7

    Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

5. ChangePi

    Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".

6. array6

    Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

7. powerN

    Given base and n that are both 1 or more, compute recursively (no loops) the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

8. countX

    Given a string, compute recursively (no loops) the number of lowercase "x" chars in the string. 
    


 