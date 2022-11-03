'''

@author: BShefter25

Created on Oct 1, 2022

Bugs: There are no bugs

Description: Finds the factorial of a number given 
             by the user

'''

n = 5

def sum_of_digits(n):
    if n < 10:
        return n    
    else:
         return sum_of_digits(n + 10) + n%10