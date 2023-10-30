# 1. Write a Python program to print the numbers from 1 to 10 using a while loop.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# 2. Write a Python program to calculate the sum of all numbers from 1 to 100 using a while loop.
# sum_of_numbers = 0
# i = 1

# while i <= 100:
#     sum_of_numbers += i
#     i += 1

# print(f"The sum of numbers from 1 to 100 is: {sum_of_numbers}")

# 3. Write a Python program to find the factorial of a number using a while loop.
# n = 5
# factorial = 1
# i = 1

# while i <= n:
#     factorial *= i
#     i += 1

# print(f"The factorial of {n} is: {factorial}")

# 4. Write a Python program to print all the even numbers between 1 and 50 using a while loop.
# num = 2

# while num <= 50:
#     print(num)
#     num += 2

# 5. Write a Python program to iterate over a string and print each character using a while loop.
# string = "Hello, World!"
# i = 0

# while i < len(string):
#     print(string[i])
#     i += 1

# 6. Write a Python program to iterate over a list of tuples and print each element using a while loop.
# tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]
# i = 0

# while i < len(tuple_list):
#     j = 0
#     while j < len(tuple_list[i]):
#         print(tuple_list[i][j])
#         j += 1
#     i += 1

# 7. Write a Python program to find the largest element in a list using a while loop.
# numbers = [10, 30, 5, 40, 20]
# largest = numbers[0]
# i = 1

# while i < len(numbers):
#     if numbers[i] > largest:
#         largest = numbers[i]
#     i += 1

# print(f"The largest element is: {largest}")

# 8. Write a Python program to check if all elements in a list are even using a while loop.
# numbers = [2, 4, 6, 8, 10]
# all_even = True
# i = 0

# while i < len(numbers):
#     if numbers[i] % 2 != 0:
#         all_even = False
#         break
#     i += 1

# if all_even:
#     print("All elements are even")
# else:
#     print("Not all elements are even")

# 9. Write a Python program to find the common elements between two lists using a while loop.
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common_elements = []

# i = 0
# while i < len(list1):
#     j = 0
#     while j < len(list2):
#         if list1[i] == list2[j]:
#             common_elements.append(list1[i])
#         j += 1
#     i += 1

# print(f"The common elements are: {common_elements}")

# 10. Write a Python program to calculate the sum of the digits of a number using a while loop.
# num = 12345
# sum_of_digits = 0

# while num > 0:
#     digit = num % 10
#     sum_of_digits += digit
#     num = num // 10

# print(f"The sum of the digits is: {sum_of_digits}")
