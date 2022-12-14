def get_summation(sum_input):                                       #states function and defines input

    '''
    Author: Brady Calhoun
    Date: 11/10/22
    Bugs: None
    Description: Runs code to find the summation of a whole number
    '''

    if sum_input == 0:                                              #checks if input is zero

        sum_output = 0                                              #sets output to zero

    else:                                                           #all other cases

        sum_output = sum_input + get_summation(sum_input - 1)       #creates chain of function calls to find output for non-zero input

    return sum_output                                               #returns output
