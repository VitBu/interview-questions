# Given an array of size n find the element that appears more than floor(n/2) times, if it doesn't exist return None.

from collections import Counter


def majorityElement(self, A):
    counter = Counter(A)
    most_common, times = counter.most_common(1)[0]
    if times > len(A) // 2:
        return most_common
    
    return None
