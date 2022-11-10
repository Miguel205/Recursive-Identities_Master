'''

@author: BShefter25

Created on Oct 1, 2022

Bugs: There are no bugs

Description: Finds the factorial of a number given 
             by the user

'''


def factorial_1(fact):                                   #will run the function if user input is more than 0
        
    if fact == 0:
        return 1
    
    else:
        return fact * factorial_1(fact-1)

       
