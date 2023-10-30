# 1. Write a Python program to find the sum of all elements in a list.

# def find_sum(input_list):
#     total = 0
#     for num in input_list:
#         total += num
#     return total
#
# numbers = [1, 2, 3, 4, 5]
# sum_of_numbers = find_sum(numbers)
# print(f"The sum of the elements in the list is: {sum_of_numbers}")

#2. Write a Python program to find the maximum and minimum elements in a list.

# def find_max_min(input_list):
#     if not input_list:  # Check if the list is empty
#         return None, None
#
#     max_element = min_element = input_list[0]
#
#     for num in input_list:
#         if num > max_element:
#             max_element = num
#         if num < min_element:
#             min_element = num
#
#     return max_element, min_element
#
# numbers = [3, 5, 1, 8, 2, 7]
# max_num, min_num = find_max_min(numbers)
#
# print(f"The maximum element in the list is: {max_num}")
# print(f"The minimum element in the list is: {min_num}")

#3. Write a Python program to remove duplicates from a list.

# def remove_duplicates(input_list):
#     return list(set(input_list))
#
# numbers_with_duplicates = [1, 2, 3, 2, 4, 3, 5, 1]
# unique_numbers = remove_duplicates(numbers_with_duplicates)
#
# print(f"The list with duplicates removed is: {unique_numbers}")

#4. Write a Python program to check if a list is sorted in ascending order.

# def is_ascending(input_list):
#     return all(input_list[i] <= input_list[i+1] for i in range(len(input_list)-1))
#
# # Example usage:
# sorted_list = [1, 2, 3, 4, 5]
# unsorted_list = [3, 1, 5, 2, 4]
#
# if is_ascending(sorted_list):
#     print("The list is sorted in ascending order.")
# else:
#     print("The list is not sorted in ascending order.")

#5. Write a Python program to find the second largest element in a list.

# def find_second_largest(input_list):
#     # Make sure the list has at least two elements
#     if len(input_list) < 2:
#         return "List must have at least two elements"
#
#     # Initialize the largest and second largest variables
#     largest = second_largest = float('-inf')
#
#     for num in input_list:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num != largest:
#             second_largest = num
#
#     return second_largest
#
# numbers = [3, 1, 5, 2, 4]
# second_largest_num = find_second_largest(numbers)
#
# print(f"The second largest element in the list is: {second_largest_num}")

#6. Write a Python program to sort a list of strings in alphabetical order.

# def sort_strings_alphabetically(input_list):
#     return sorted(input_list)
#
# words = ['apple', 'cherry', 'fig', 'banana', 'date']
# sorted_words = sort_strings_alphabetically(words)
#
# print(f"The sorted list of strings is: {sorted_words}")

#7. Write a Python program to find the common elements between two lists.

# def find_common_elements(list1, list2):
#     return list(set(list1).intersection(list2))
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
#
# common_elements = find_common_elements(list1, list2)
#
# print(f"The common elements are: {common_elements}")

# 8. Write a Python program to remove the nth occurrence of an element from a list.

# def remove_nth_occurrence(lst, element, n):
#     count = 0
#     new_list = []
#
#     for item in lst:
#         if item == element:
#             count += 1
#             if count == n:
#                 continue  # Skip the nth occurrence
#         new_list.append(item)
#
#     return new_list
#
# numbers = [1, 2, 3, 4, 2, 5, 2, 6]
# element_to_remove = 2
# occurrence_number = 2
#
# new_list = remove_nth_occurrence(numbers, element_to_remove, occurrence_number)
#
# print(f"The list after removing the {occurrence_number}nd occurrence of {element_to_remove} is: {new_list}")

#9. Write a Python program to find the difference between two lists.

# def find_list_difference(list1, list2):
#     return list(set(list1) - set(list2))
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
#
# difference = find_list_difference(list1, list2)
#
# print(f"The elements in list1 that are not in list2 are: {difference}")

#10. Write a Python program to remove the elements of a list that are divisible by 3.

# def remove_divisible_by_3(input_list):
#     return [x for x in input_list if x % 3 != 0]
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# non_divisible_by_3 = remove_divisible_by_3(numbers)
#
# print(f"The list after removing elements divisible by 3 is: {non_divisible_by_3}")
