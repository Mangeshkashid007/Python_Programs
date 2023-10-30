# 1. Write a Python program to find the length of a tuple.

# def find_tuple_length(input_tuple):
#     return len(input_tuple)
#
# my_tuple = (1, 2, 3, 4, 5)
# tuple_length = find_tuple_length(my_tuple)
#
# print(f"The length of the tuple is: {tuple_length}")

# 2. Write a Python program to concatenate two tuples.

# def concatenate_tuples(tuple1, tuple2):
#     return tuple1 + tuple2
#
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# concatenated_tuple = concatenate_tuples(tuple1, tuple2)
#
# print(f"The concatenated tuple is: {concatenated_tuple}")

# 3. Write a Python program to convert a tuple to a list.

# def convert_tuple_to_list(input_tuple):
#     return list(input_tuple)
#
# my_tuple = (1, 2, 3, 4, 5)
# my_list = convert_tuple_to_list(my_tuple)
#
# print(f"The converted list is: {my_list}")

# 4. Write a Python program to find the index of an element in a tuple.

# def find_element_index(input_tuple, element):
#     if element in input_tuple:
#         return input_tuple.index(element)
#     else:
#         return f"{element} is not in the tuple."
#
# my_tuple = (1, 2, 4, 5, 3)
# element_to_find = 3
# index = find_element_index(my_tuple, element_to_find)
#
# print(f"The index of {element_to_find} is: {index}")

# 5. Write a Python program to check if an element exists in a tuple.

# def check_element_existence(input_tuple, element):
#     return element in input_tuple
#
# my_tuple = (1, 2, 3, 4, 5)
# element_to_check = 10
# exists = check_element_existence(my_tuple, element_to_check)
#
# if exists:
#     print(f"{element_to_check} exists in the tuple.")
# else:
#     print(f"{element_to_check} does not exist in the tuple.")

#6. Write a Python program to count the number of occurrences of an element in a tuple.

# def count_occurrences(input_tuple, element):
#     return input_tuple.count(element)
#
# my_tuple = (1, 2, 3, 4, 2, 2, 5, 2)
# element_to_count = 7
# occurrences = count_occurrences(my_tuple, element_to_count)
#
# print(f"The number of occurrences of {element_to_count} is: {occurrences}")

#7. Write a Python program to find the maximum and minimum elements in a tuple.

# def find_max_min(input_tuple):
#     max_element = max(input_tuple)
#     min_element = min(input_tuple)
#     return max_element, min_element
#
# my_tuple = (3, 1, 5, 2, 4)
# max_num, min_num = find_max_min(my_tuple)
#
# print(f"The maximum element in the tuple is: {max_num}")
# print(f"The minimum element in the tuple is: {min_num}")

# 8. Write a Python program to reverse a tuple.

# def reverse_tuple(input_tuple):
#     return input_tuple[::-1]
#
# my_tuple = (1, 2, 3, 4, 5)
# reversed_tuple = reverse_tuple(my_tuple)
#
# print(f"The reversed tuple is: {reversed_tuple}")

# 9. Write a Python program to check if all elements in a tuple are the same.

# def check_if_elements_same(input_tuple):
#     return all(x == input_tuple[0] for x in input_tuple)
#
# tuple1 = (1, 1, 1, 1, 1)
# tuple2 = (1, 1, 1, 7, 1)
#
# result1 = check_if_elements_same(tuple1)
# result2 = check_if_elements_same(tuple2)
#
# print(f"For tuple1, all elements are the same: {result1}")
# print(f"For tuple2, all elements are the same: {result2}")

# 10. Write a Python program to create a new tuple with the elements from two existing tuples.

# def create_new_tuple(tuple1, tuple2):
#     return tuple1 + tuple2
#
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# new_tuple = create_new_tuple(tuple1, tuple2)
#
# print(f"The new tuple is: {new_tuple}")

