
def get_powers(power_input1 , power_input2):                                                #states function and defines two variables

    '''
    Author: Brady Calhoun
    Date: 11/10/22
    Bugs: None
    Description: Runs code to find uses two whole numbers to find a whole number to a given power
    '''

    if power_input2 == 0:                                                                   #checks for zero as power

        power_output = 1                                                                    #proper output for zero power

    else:                                                                                   #all other positive numbers
        
        power_output = power_input1 * get_powers(power_input1,power_input2 - 1)           #finds what the first input is to the power of the second input using function chain

    return power_output                                                                     #returns proper output
