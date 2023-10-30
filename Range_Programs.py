# 1. Write a Python program to iterate over a range of numbers and print them.
#
# def print_numbers_in_range(start, end):
#     for num in range(start, end+1):
#         print(num)

# start = 1
# end = 5
# print_numbers_in_range(start, end)

# 2. Write a Python program to find the sum of all numbers in a range.

# def find_sum_in_range(start, end):
#     return sum(range(start, end+1))

# start = 1
# end = 5
# sum_in_range = find_sum_in_range(start, end)
# print(f"The sum of numbers in the range is: {sum_in_range}")

# 3. Write a Python program to print all even numbers in a given range.

# def print_even_numbers_in_range(start, end):
#     for num in range(start, end+1):
#         if num % 2 == 0:
#             print(num)

# start = 1
# end = 10
# print_even_numbers_in_range(start, end)

# 4. Write a Python program to print all odd numbers in a given range.

# def print_odd_numbers_in_range(start, end):
#     for num in range(start, end+1):
#         if num % 2 != 0:
#             print(num)

# start = 1
# end = 10
# print_odd_numbers_in_range(start, end)

# 5. Write a Python program to find the average of all numbers in a range.

# def find_average_in_range(start, end):
#     return sum(range(start, end+1)) / (end - start + 1)

# start = 1
# end = 5
# average = find_average_in_range(start, end)
# print(f"The average of numbers in the range is: {average}")

# 6. Write a Python program to check if a number is present in a given range.

# def check_if_number_in_range(start, end, num):
#     return start <= num <= end

# start = 1
# end = 10
# num_to_check = 7

# if check_if_number_in_range(start, end, num_to_check):
#     print(f"{num_to_check} is in the range.")
# else:
#     print(f"{num_to_check} is not in the range.")

# 7. Write a Python program to reverse a range of numbers and print them.

# def reverse_and_print_range(start, end):
#     for num in range(end, start-1, -1):
#         print(num)

# start = 1
# end = 5
# reverse_and_print_range(start, end)

# 8. Write a Python program to find the product of all numbers in a range.

# def find_product_in_range(start, end):
#     product = 1
#     for num in range(start, end+1):
#         product *= num
#     return product

# start = 1
# end = 5
# product = find_product_in_range(start, end)
# print(f"The product of numbers in the range is: {product}")

# 9. Write a Python program to print the squares of all numbers in a range.
# def print_squares_in_range(start, end):
#     for num in range(start, end+1):
#         print(f"The square of {num} is: {num**2}")

# start = 1
# end = 5
# print_squares_in_range(start, end)

# 10. Write a Python program to print the cube of all numbers in a range.

# def print_cubes_in_range(start, end):
#     for num in range(start, end+1):
#         print(f"The cube of {num} is: {num**3}")

# start = 1
# end = 5
# print_cubes_in_range(start, end)
