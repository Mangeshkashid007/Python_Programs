# 1. Write a Python program to iterate over a dictionary and print its keys and values.
# def iterate_dict(input_dict):
#     for key, value in input_dict.items():
#         print(f"Key: {key}, Value: {value}")
#
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# iterate_dict(my_dict)

# 2. Write a Python program to check if a key exists in a dictionary.
# def check_key_existence(input_dict, key):
#     return key in input_dict
#
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# key_to_check = 'b'
#
# if check_key_existence(my_dict, key_to_check):
#     print(f"The key '{key_to_check}' exists in the dictionary.")
# else:
#     print(f"The key '{key_to_check}' does not exist in the dictionary.")

# 3. Write a Python program to get the value associated with a key in a dictionary.
# def get_value(input_dict, key):
#     return input_dict.get(key)
#
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# key_to_get = 'b'
#
# value = get_value(my_dict, key_to_get)
#
# if value is not None:
#     print(f"The value for key '{key_to_get}' is: {value}")
# else:
#     print(f"The key '{key_to_get}' does not exist in the dictionary.")

# 4. Write a Python program to remove a key from a dictionary.
# def remove_key(input_dict, key):
#     input_dict.pop(key, None)
#     return input_dict
#
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# key_to_remove = 'b'
#
# updated_dict = remove_key(my_dict, key_to_remove)
#
# print(f"The dictionary after removing key '{key_to_remove}' is: {updated_dict}")

# 5. Write a Python program to sort a dictionary by its values.
# def sort_dict_by_values(input_dict):
#     return dict(sorted(input_dict.items(), key=lambda item: item[1]))
#
# my_dict = {'a': 3, 'b': 1, 'c': 2}
# sorted_dict = sort_dict_by_values(my_dict)
#
# print(f"The sorted dictionary by values is: {sorted_dict}")

# 6. Write a Python program to merge two dictionaries.
# def merge_dicts(dict1, dict2):
#     return {**dict1, **dict2}
#
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
#
# merged_dict = merge_dicts(dict1, dict2)
#
# print(f"The merged dictionary is: {merged_dict}")

# 7. Write a Python program to count the frequency of each element in a dictionary.
# from collections import Counter
#
# def count_frequency(input_dict):
#     return Counter(input_dict.values())
#
# my_dict = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 3}
# frequency = count_frequency(my_dict)
#
# print(f"The frequency of each element is: {frequency}")

# 8. Write a Python program to find the length of a dictionary.
# def find_dict_length(input_dict):
#     return len(input_dict)
#
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# length = find_dict_length(my_dict)
#
# print(f"The length of the dictionary is: {length}")

# 9. Write a Python program to check if a dictionary is empty.
# def check_if_empty(input_dict):
#     return not bool(input_dict)
#
# empty_dict = {}
# non_empty_dict = {'a': 1, 'b': 2}
#
# if check_if_empty(empty_dict):
#     print("The dictionary is empty.")
# else:
#     print("The dictionary is not empty.")
#
# if check_if_empty(non_empty_dict):
#     print("The dictionary is empty.")
# else:
#     print("The dictionary is not empty.")

# 10. Write a Python program to find the keys with the maximum and minimum values in a dictionary.

# def find_max_min_keys(input_dict):
#     max_key = max(input_dict, key=input_dict.get)
#     min_key = min(input_dict, key=input_dict.get)
#     return max_key, min_key
#
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 1}
#
# max_key, min_key = find_max_min_keys(my_dict)
#
# print(f"The key with the maximum value is: {max_key}")
# print(f"The key with the minimum value is: {min_key}")
