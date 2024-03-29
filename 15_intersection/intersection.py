def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    new_lst = []
    for num1 in l1:
        for num2 in l2:
            if num1 == num2:
                new_lst.append(num1)
            
    return new_lst


    # Alternatively, using built-in set math:
    # return list(set(l1) & set(l2))