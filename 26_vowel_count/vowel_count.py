def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

 # Initialize an empty dictionary to store vowel frequencies
    vowel_freq = {}
    
    # Convert the phrase to lowercase to make the comparison case-insensitive
    phrase = phrase.lower()
    
    # Iterate through each character in the lowercase phrase
    for char in phrase:
        # Check if the character is a vowel
        if char in 'aeiou':
            # Increment the count of the vowel in the dictionary
            vowel_freq[char] = vowel_freq.get(char, 0) + 1
    
    # Return the dictionary containing the frequency map of vowels
    return vowel_freq
