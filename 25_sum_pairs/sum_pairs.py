def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

 # Create an empty dictionary to store seen numbers and their indices
    seen = {}
    
    # Iterate through the list of numbers
    for num in nums:
        # Calculate the complement needed to reach the goal
        complement = goal - num
        
        # Check if the complement exists in the seen dictionary
        if complement in seen:
            # If the complement exists, return a tuple of the current number and its complement
            return (seen[complement], num)
        
        # If the complement doesn't exist, store the current number in the seen dictionary
        seen[num] = num
    
    # If no pairs are found that sum to the goal, return an empty tuple
    return ()