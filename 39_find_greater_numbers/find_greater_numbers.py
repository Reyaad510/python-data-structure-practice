def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """

    # Initialize a variable to keep track of the count
    count = 0
    
    # Iterate through the elements of the nums list
    for i in range(len(nums)):
        # Iterate through the subsequent elements
        for j in range(i + 1, len(nums)):
            # If the subsequent element is greater, increment the count
            if nums[j] > nums[i]:
                count += 1
    
    # Return the final count
    return count