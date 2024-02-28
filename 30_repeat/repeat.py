def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
     # Check if num is a positive integer
    if isinstance(num, int) and num >= 0:
        # Repeat the phrase num times and return the result
        return phrase * num
    else:
        # If num is not a positive integer, return None
        return None