# 1. Write a Python program to find the first occurrence of a number in a list using a for loop and break statement.
# numbers = [10, 20, 30, 40, 50, 60]
# target = 30

# for num in numbers:
#     if num == target:
#         print(f"The first occurrence of {target} is at index {numbers.index(target)}")
#         break

# 2. Write a Python program to search for a specific element in a list using a while loop and break statement.
# numbers = [10, 20, 30, 40, 50, 60]
# target = 30
# found = False
# i = 0

# while i < len(numbers):
#     if numbers[i] == target:
#         found = True
#         print(f"{target} found at index {i}")
#         break
#     i += 1

# if not found:
#     print(f"{target} not found in the list")

# 3. Write a Python program to find the prime numbers between 1 and 100 using a for loop and break statement.
# for num in range(2, 101):
#     for i in range(2, num):
#         if (num % i) == 0:
#             break
#     else:
#         print(num)

# 4. Write a Python program to check if a number is present in a list using a while loop and break statement.
# numbers = [10, 20, 30, 40, 50, 60]
# target = 30
# found = False
# i = 0

# while i < len(numbers):
#     if numbers[i] == target:
#         found = True
#         print(f"{target} is present in the list.")
#         break
#     i += 1

# if not found:
#     print(f"{target} is not present in the list.")

# 5. Write a Python program to find the largest palindrome number in a given range using a for loop and break statement.
# def is_palindrome(num):
#     return str(num) == str(num)[::-1]

# largest_palindrome = 0

# for i in range(100, 1000):
#     for j in range(100, 1000):
#         product = i * j
#         if is_palindrome(product) and product > largest_palindrome:
#             largest_palindrome = product

# print(f"The largest palindrome number is: {largest_palindrome}")

# 6. Write a Python program to find the first negative number in a list using a while loop and break statement.
# numbers = [10, -20, 30, -40, 50, 60]
# found = False
# i = 0

# while i < len(numbers):
#     if numbers[i] < 0:
#         found = True
#         print(f"The first negative number is: {numbers[i]}")
#         break
#     i += 1

# if not found:
#     print("No negative numbers found in the list.")

# 7. Write a Python program to print the elements of a list until a specific condition is met using a for loop and break statement.
# numbers = [10, 20, 30, 40, 50, 60]
# condition_met = False

# for num in numbers:
#     if num == 40:
#         condition_met = True
#         break
#     print(num)

# if condition_met:
#     print("Condition met. Stopping loop.")
# else:
#     print("Condition not met.")

# 8. Write a Python program to search for a specific character in a string using a while loop and break statement.
# string = "Hello, World!"
# target = 'o'
# found = False
# i = 0

# while i < len(string):
#     if string[i] == target:
#         found = True
#         print(f"{target} found at index {i}")
#         break
#     i += 1

# if not found:
#     print(f"{target} not found in the string.")

# 9. Write a Python program to find the first occurrence of a vowel in a string using a for loop and break statement.
# string = "Hello, World!"

# for char in string:
#     if char.lower() in 'aeiou':
#         print(f"The first vowel is: {char}")
#         break

# 10. Write a Python program to find the index of the first occurrence of a substring in a string using a while loop and break statement.
# string = "Hello, World!"
# substring = "lo"
# found = False
# i = 0

# while i < len(string) - len(substring) + 1:
#     if string[i:i+len(substring)] == substring:
#         found = True
#         print(f"The substring '{substring}' found at index {i}")
#         break
#     i += 1

# if not found:
#     print(f"The substring '{substring}' not found in the string.")
