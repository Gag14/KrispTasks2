def find_min_pledge(pledge_list):
    
    pledge_set = set(pledge_list)    
    i = 1
    while i in pledge_set:
        i += 1
    
    return i

assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1