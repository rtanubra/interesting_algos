"""
Backtracking:
    -the backbone to a majority of these problems. Let's explore some backtracking.

What does it mean: 
    In some problems, as we search for a solution, we may reach
    a dead end and have to go back to a previous part. 

Implementation of Generate Parantheses:
    Given an integer 'n'. Print all the possible pairs of 'n'
    balanced parantheses. 

    input:
        single integer value n
    
    output 

"""

def generate_paranthesis(openB,closeB,n,s=[]):
    #base case
    if closeB == n:
        print("".join(s))
        return
    
    else:
        if openB > closeB:
            s.append(")")
            generate_paranthesis(openB,closeB + 1,n,s)
            #BACKTRACKING STEP IS IN THE POP
            s.pop()
        if openB < n:
            s.append("(")
            generate_paranthesis(openB + 1,closeB,n,s)
            #BACKTRACKING STEP IS IN THE POP
            s.pop()
    
#generate_paranthesis(0,0,4)

        
        

