'''

@author: BShefter25

Created on Oct 1, 2022

Bugs: There are no bugs

Description: Finds the factorial of a number given 
             by the user

'''


def factorial_1(fact):                                   
        
    if fact == 0:                             #if fact is equal to 0
        return 1                              #return 1
    
    else:                                     #otherwise
        return fact * factorial_1(fact-1)     #return factorial

       
