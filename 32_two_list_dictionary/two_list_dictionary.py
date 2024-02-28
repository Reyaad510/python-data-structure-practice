def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    
    # Use a dictionary comprehension to create the dictionary
    # Pair each key from the 'keys' list with its corresponding value from the 'values' list
    # If there are fewer values than keys, pad the 'values' list with None values
    # The zip function pairs elements from 'keys' and 'values' lists, and the + operator combines the lists
    # The [None] * (len(keys) - len(values)) part pads the 'values' list with None values if necessary
    return {k: v for k, v in zip(keys, values + [None] * (len(keys) - len(values)))}