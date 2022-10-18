# Given an array of size n find the element that appears more than floor(n/2) times, if it doesn't exist return None.


from collections import Counter


def majority_element(A):
    counter = Counter(A)
    most_common_result = counter.most_common(1)
    if most_common_result == []:
        return None

    most_common, times = most_common_result[0]
    if times > len(A) // 2:
        return most_common
    
    return None



if __name__ == '__main__':
    assert majority_element([]) == None
    assert majority_element([1]) == 1
    assert majority_element([1, 2]) == None
    assert majority_element([1, 3, 1]) == 1
