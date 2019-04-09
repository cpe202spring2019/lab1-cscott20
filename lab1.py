
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == []:
        return None
    if int_list == None:
        raise ValueError
    maxnum = int_list[0]
    for x in int_list:
        if x > maxnum:
            maxnum = x
    return maxnum

def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return int_list
    return reverse_rec(int_list[1:len(int_list)]) + [(int_list[0])]

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    mid = (high + low)//2
    if int_list == None:
        raise ValueError
    if int_list == []:
        return None
    if ((high - low) == 1):
        if int_list[low] == target:
            return low
        elif int_list[high] == target:
            return high
        else: return None
    if (int_list[mid] == target):
        return (mid)
    if (int_list[mid] < target):
        return bin_search(target, mid, high, int_list)
    if (int_list[mid] > target):
        return bin_search(target, low, mid, int_list)    
