'''

@author: BShefter25

Created on Oct 1, 2022

Bugs: There are no bugs

Description: Finds the factorial of a number given 
             by the user

'''

fact = 2
factorial = 1

def factorial_1(fact, factorial):                                   #will run the function if user input is more than 0
    for i in range(1, fact + 1):                                    #adding 1 to the user input
        factorial = factorial*i                                     #getting the factorial of the given input
    return factorial