def get_fibonacci(fib_input):                                                       #fuction is called, fib_input in number inputted

    '''
    Author: Brady Calhoun
    Date: 11/10/22
    Bugs: None
    Description: Runs code to find fibonacci output for any whole number input
    '''



    if fib_input <= 0:                                                              #checks for specific inputs

        fib_output = 0                                                              #sets specific inputs

    elif fib_input == 1:                                                            #checks for specific inputs

        fib_output = 1                                                              #sets specific inputs

    else:

        fib_output = get_fibonacci(fib_input - 1) + get_fibonacci(fib_input - 2)    #sets output to specific based on input ran back through functions

    return fib_output                                                               #returns output