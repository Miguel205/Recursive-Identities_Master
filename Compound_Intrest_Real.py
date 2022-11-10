
def get_intrest(intrest_input1 , intrest_input2 , intrest_input3):                                                          #states function and defines inputs
    '''
    Author: Brady Calhoun
    Date: 11/10/22
    Bugs: None
    Description: Runs code to find compound intrest of a given whole number, based on a given float
    '''

    if intrest_input3 == 0:                                                                                                 #checks for zero in time/year input

        intrest_output = intrest_input1                                                                                     #zero in time input keeps output as input 1

    else:                                                                                                                   #all other positive amounts of time

        intrest_output = (1 + intrest_input2) * get_intrest(intrest_input1 , intrest_input2 , intrest_input3 - 1)           #creates function chain to find the compound intrest and set it as output 

    return intrest_output                                                                                                   #returns output