# 1. Write a Python program to find the union of two sets.

# def find_union(set1, set2):
#     return set1.union(set2)
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
#
# union_set = find_union(set1, set2)
#
# print(f"The union of the sets is: {union_set}")

# 2. Write a Python program to find the intersection of two sets.

# def find_intersection(set1, set2):
#     return set1.intersection(set2)
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
#
# intersection_set = find_intersection(set1, set2)
#
# print(f"The intersection of the sets is: {intersection_set}")

# 3. Write a Python program to check if a set is a subset of another set.

# def check_subset(set1, set2):
#     return set1.issubset(set2)
#
# set1 = {3, 4, 1}
# set2 = {1, 2, 3, 4, 5}
#
# is_subset = check_subset(set1, set2)
#
# if is_subset:
#     print("set1 is a subset of set2")
# else:
#     print("set1 is not a subset of set2")

# 4. Write a Python program to remove duplicate elements from a set.

# def remove_duplicates_from_set(input_set):
#     return input_set
#
# my_set = {1, 2, 2, 3, 4, 4, 5}
#
# unique_set = remove_duplicates_from_set(my_set)
#
# print(f"The set after removing duplicates is: {unique_set}")

# 5. Write a Python program to add an element to a set.

# def add_element_to_set(input_set, element):
#     input_set.add(element)
#     return input_set
#
# my_set = {1, 2, 3, 4, 5}
# new_element = 6
#
# updated_set = add_element_to_set(my_set, new_element)
#
# print(f"The set after adding {new_element} is: {updated_set}")

# 6. Write a Python program to remove an element from a set.

# def remove_element_from_set(input_set, element):
#     input_set.discard(element)
#     return input_set
#
# my_set = {1, 2, 3, 4, 5}
# element_to_remove = 3
#
# updated_set = remove_element_from_set(my_set, element_to_remove)
#
# print(f"The set after removing {element_to_remove} is: {updated_set}")

# 7. Write a Python program to find the difference between two sets.

# def find_set_difference(set1, set2):
#     return set1 - set2
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
#
# difference_set = find_set_difference(set1, set2)
#
# print(f"The difference between the sets is: {difference_set}")

#8. Write a Python program to check if two sets are disjoint.

# def check_disjoint(set1, set2):
#     return set1.isdisjoint(set2)
#
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
#
# is_disjoint = check_disjoint(set1, set2)
#
# if is_disjoint:
#     print("The sets are disjoint.")
# else:
#     print("The sets are not disjoint.")

# 9. Write a Python program to find the symmetric difference between two sets.

# def find_symmetric_difference(set1, set2):
#     return set1.symmetric_difference(set2)
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
#
# symmetric_difference_set = find_symmetric_difference(set1, set2)
#
# print(f"The symmetric difference between the sets is: {symmetric_difference_set}")

# 10. Write a Python program to check if a set is empty.

# def check_if_empty(input_set):
#     return not bool(input_set)
#
# empty_set = set()
# non_empty_set = {1, 2, 3}
#
# if check_if_empty(empty_set):
#     print("The set is empty.")
# else:
#     print("The set is not empty.")
#
# if check_if_empty(non_empty_set):
#     print("The set is empty.")
# else:
#     print("The set is not empty.")
