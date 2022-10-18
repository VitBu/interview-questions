# You are in the 0th index of a non-negative integers array.
# Each element in the array represents a maximum jump from this position.
# Are you able to reach the last index?


def is_reachable(input_array):
    max_jump = 1
    for cur_jump in input_array[:-1]:
      max_jump = max(max_jump - 1, cur_jump)
      if max_jump == 0:
          return False

    return True


if __name__ == '__main__':
    assert is_reachable([1, 0]) == True
    assert is_reachable([0, 1, 1]) == False
    assert is_reachable([3, 0, 0, 0]) == True
    assert is_reachable([3, 1, 1, 1, 0]) == True
    
