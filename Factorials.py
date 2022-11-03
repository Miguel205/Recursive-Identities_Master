'''

@author: BShefter25

Created on Oct 1, 2022

Bugs: There are no bugs

Description: Finds the factorial of a number given 
             by the user

'''

def non_factorial(fact):                                            #will run if user input equals a negative number
    print("Sorry, There Is No Factorial For Negative Numbers")      #if the input is negative, then there is no factorial

def factorial_0(fact):                                              #will run the function if user input equals 0
    print("The Factorial of 0 Is 1")                                #if the input is 0, then the factorial of 0 equals 1

def factorial_1(fact, factorial):                                   #will run the function if user input is more than 0
    for i in range(1, fact + 1):                                    #adding 1 to twhe user input
        factorial = factorial*i                                     #getting the factorial of the given input
    print("The Factorial of", fact, "Is", factorial)                #the factorial of the user input is _______


def main(): 

    fact = int(input("What Is The Number? "))                       #setting fact variable equal to the user input
    factorial = 1                                                   #setting the factorial variable equal to an integer of 1
    
    if fact < 0:                                                    #if the user input is a negative number
        non_factorial(fact)                                         #it will call the non_factorial function
    
    elif fact == 0:                                                 #if the user input equals 0
        factorial_0(fact)                                           #it will call the factorial_0 function
    
    else:                                                           #if the input is anything else above 0
        factorial_1(fact, factorial)                                #it will call the factorial_1 function
    
    else:                                                           #otherwise
        print("Ok, Bye")                                            #the program will break


if __name__ == '__main__':
    main()
