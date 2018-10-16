def sacados(lst, i):
    """Check if there exist a sub-list of lst whose total value is exactly i
    
    Arguments:
        lst {list} -- the list
        i {int} -- sub list total value seeked
    """
    if len(lst) == 0:
        return i == 0
    else:
        return (sacados(lst[1:], i) or sacados(lst[1:], i - lst[0]))

print(sacados([2, 7, -1, 9], 16))
print(sacados([2, 7, -1, 9], 4))