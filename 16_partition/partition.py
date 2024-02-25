def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    
    list_a = []
    list_b = []
    final_list = [list_a,list_b]
    for element in lst:
       ele_boolean = fn(element)
       if ele_boolean == True:
           list_a.append(element)
       else:
           list_b.append(element)


    return final_list