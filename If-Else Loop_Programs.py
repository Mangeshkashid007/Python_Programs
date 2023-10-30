# 1. Write a Python program to check if a number is positive, negative, or zero.
# def check_number(num):
#     if num > 0:
#         return "Positive"
#     elif num < 0:
#         return "Negative"
#     else:
#         return "Zero"

# number = 5
# result = check_number(number)
# print(f"The number {number} is {result}.")

# 2. Write a Python program to check if a number is even or odd.

# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# number = 7
# result = check_even_odd(number)
# print(f"The number {number} is {result}.")

# 3. Write a Python program to check if a year is a leap year or not.

# def check_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return "Leap Year"
#     else:
#         return "Not a Leap Year"

# year = 2024
# result = check_leap_year(year)
# print(f"The year {year} is {result}.")

# 4. Write a Python program to find the maximum of three numbers using if-else.

# def find_max(num1, num2, num3):
#     max_num = num1
#     if num2 > max_num:
#         max_num = num2
#     if num3 > max_num:
#         max_num = num3
#     return max_num

# num1, num2, num3 = 5, 8, 3
# max_number = find_max(num1, num2, num3)
# print(f"The maximum of {num1}, {num2}, and {num3} is: {max_number}")

# 5. Write a Python program to check if a number is prime.

# def check_prime(num):
#     if num < 2:
#         return "Not Prime"
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return "Not Prime"
#     return "Prime"

# number = 11
# result = check_prime(number)
# print(f"The number {number} is {result}.")

# 6. Write a Python program to check if a number is divisible by both 3 and 5.

# def check_divisibility(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "Divisible by both 3 and 5"
#     else:
#         return "Not divisible by both 3 and 5"

# number = 15
# result = check_divisibility(number)
# print(f"The number {number} is {result}.")

# 7. Write a Python program to check if a character is a vowel or consonant.

# def check_vowel_consonant(char):
#     vowels = 'aeiouAEIOU'
#     if char in vowels:
#         return "Vowel"
#     else:
#         return "Consonant"

# character = 'e'
# result = check_vowel_consonant(character)
# print(f"The character '{character}' is a {result}.")

# 8. Write a Python program to check if a given string is a palindrome using if-else.

# def is_palindrome(input_str):
#     if input_str == input_str[::-1]:
#         return "Palindrome"
#     else:
#         return "Not a Palindrome"

# string = "radar"
# result = is_palindrome(string)
# print(f"The string '{string}' is {result}.")

# 9. Write a Python program to determine the largest among three numbers using nested if-else.

# def find_largest(num1, num2, num3):
#     if num1 >= num2:
#         if num1 >= num3:
#             return num1
#         else:
#             return num3
#     else:
#         if num2 >= num3:
#             return num2
#         else:
#             return num3

# num1, num2, num3 = 7, 2, 5
# largest_number = find_largest(num1, num2, num3)
# print(f"The largest among {num1}, {num2}, and {num3} is: {largest_number}")

# 10. Write a Python program to check if a triangle is equilateral, isosceles, or scalene based on its side lengths using if-else.

# def check_triangle_type(side1, side2, side3):
#     if side1 == side2 == side3:
#         return "Equilateral Triangle"
#     elif side1 == side2 or side2 == side3 or side3 == side1:
#         return "Isosceles Triangle"
#     else:
#         return "Scalene Triangle"

# side1 = 5
# side2 = 5
# side3 = 5

# triangle_type = check_triangle_type(side1, side2, side3)
# print(f"The triangle with side lengths {side1}, {side2}, and {side3} is a {triangle_type}.")
