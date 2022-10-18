# how many ways to climb stairs, if you can climb 1 or 2 steps

def calc_ways_to_climb_stairs(stairs_num):
    if stairs_num in [0, 1]:
        return 1
        
    last, prev = 1, 1
    for i in range(2, stairs_num + 1):
        last, prev = last + prev, last
    
    return last
