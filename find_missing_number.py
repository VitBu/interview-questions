#
# You get array with n-1 unique numbers between 0 and n-1.
# Find Missing number. 
#

from functools import reduce
from operator import xor


def xor_sequence(sequence):
    return reduce(xor, sequence)

def find_missing_element(array):
    n = len(array) + 1
    xor_n = xor_sequence(range(n))
    xor_array = xor_sequence(array)
    return xor_n ^ xor_array


if __name__ == "__main__":
    assert find_missing_element(range(0,8)) == 8
    assert find_missing_element([0, 1, 3, 4, 5, 6, 7]) == 2
