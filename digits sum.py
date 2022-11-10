'''

@author: BShefter25

Created on Oct 1, 2022

Bugs: There are no bugs

'''

def sum_of_digits(n):
    if n < 10:                                              #if n is less than 10
        return n                                            #return the number
    else:                                                   #otherwise
         return sum_of_digits(int(n/10)) + n%10             #return the sum of digits
