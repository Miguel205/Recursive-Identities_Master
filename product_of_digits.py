def product_of_numbers_digits(n):
    '''
    @author: mdominguez25
    Created on Nov 11, 2022
    Bugs:
    receives number
    returns product of numbers digits
    '''

    if n < 10:  # if n < than 10
        return n  # return the n
    else:  # otherwise
        return product_of_numbers_digits(int( n /10)) * n% 10  # return the puduct of the remander of n/10 plus the out put of f(n/10)
