def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

# Create an empty set to store seen numbers
    seen = set()
    
    # Iterate through the list of numbers
    for num in nums:
        # Check if the number is already seen
        if num in seen:
            # If it's seen, it's the duplicate, so return it
            return num
        # Add the number to the set of seen numbers
        seen.add(num)
    
    # If no duplicate is found, return None
    return None