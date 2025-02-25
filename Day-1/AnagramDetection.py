def are_anagrams(str1, str2):
    # If lengths are different, they can't be anagrams
    if len(str1) != len(str2):
        return False

    # Create a dictionary to count character frequencies
    char_count = {}

    # Count characters in the first string
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    # Subtract character counts using the second string
    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    # If all values in char_count are zero, they are anagrams
    return all(value == 0 for value in char_count.values())

# Test cases
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("triangle", "integral"))  # True
print(are_anagrams("hello", "world"))  # False
print(are_anagrams("aabbcc", "abcabc"))  # True
