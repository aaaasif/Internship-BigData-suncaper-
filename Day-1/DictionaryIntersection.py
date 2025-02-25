def dictionary_intersection(dict1, dict2):
   
    return {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}

# Example usage:
dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'b': 2, 'c': 4, 'd': 5}

result = dictionary_intersection(dict_a, dict_b)
print(result)  # Output will be {'b': 2}
