def get_2number_product(prod_input1 , prod_input2):                                                 #states function and defines variables

    '''
    Author: Brady Calhoun
    Date: 11/10/22
    Bugs: None
    Description: Runs code to find the product of two whole numbers
    '''

    if prod_input2 == 0:                                                                            #checks for input 2 zero

        prod_output = 0                                                                             #sets output to zero for zero input

    else:                                                                                           #all other positive inputs

        prod_output = prod_input1 + get_2number_product(prod_input1 , prod_input2 - 1)              #finds product using function chain sets to output

    return prod_output                                                                              #returns output

