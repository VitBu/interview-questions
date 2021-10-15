#
# You get array with n-2 unique numbers between 0 and n-1.
# Find 2 Missing numbers. 
#

from functools import reduce
from operator import xor


def xor_sequence(sequence):
    return reduce(xor, sequence, 0)

def find_missing_elements(array):
    n_numbers = range(len(array) + 2)
    xor_missing_numbers = xor_sequence(array) ^ xor_sequence(n_numbers)    
    splitting_number = find_splitting_number(xor_missing_numbers)
    is_common_bit = lambda num: num & splitting_number
    first_number = xor_sequence(filter(is_common_bit, array)) ^ xor_sequence(filter(is_common_bit, n_numbers))
    second_number = xor_missing_numbers ^ first_number
    return {first_number, second_number}


def find_splitting_number(xor_result):
    if not xor_result:
        raise ValueError('Xor reuslt should be number > 0')
    
    one_bit_number = 1
    found_splitting_number = False
    while not found_splitting_number:
        if xor_result & one_bit_number != 0:
            return one_bit_number

        one_bit_number <<= 1
        
    

if __name__ == "__main__":
    assert find_missing_elements([0, 1, 2, 4, 6]) == {3, 5}
    assert find_missing_elements([1,2,3]) == {0, 4}
