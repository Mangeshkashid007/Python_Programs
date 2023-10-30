# 1. Write a Python program to print all the even numbers between 1 and 20 except for the number 10 using a for loop and continue statement.
# for i in range(1, 21):
#     if i == 10 or i % 2 != 0:
#         continue
#     print(i)

# 2. Write a Python program to print the elements of a list skipping the negative numbers using a while loop and continue statement.
# numbers = [10, -20, 30, -40, 50, 60]
# i = 0

# while i < len(numbers):
#     if numbers[i] < 0:
#         i += 1
#         continue
#     print(numbers[i])
#     i += 1

# 3. Write a Python program to print the first 10 multiples of 3 except for the number 9 using a for loop and continue statement.
# for i in range(1, 11):
#     if i == 3:
#         continue
#     print(i * 3)

# 4. Write a Python program to iterate over a string and print only the consonants using a for loop and continue statement.
# string = "Hello, World!"

# for char in string:
#     if char.lower() in 'aeiou':
#         continue
#     print(char)

# 5. Write a Python program to print the elements of a list skipping the even numbers using a while loop and continue statement.
# numbers = [10, 21, 30, 45, 50, 63]
# i = 0

# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         i += 1
#         continue
#     print(numbers[i])
#     i += 1

# # 6. Write a Python program to find the sum of all numbers between 1 and 100, excluding the multiples of 5 using a for loop and continue statement.
# sum_of_numbers = 0

# for i in range(1, 101):
#     if i % 5 == 0:
#         continue
#     sum_of_numbers += i

# print(f"The sum of numbers is: {sum_of_numbers}")

# 7. Write a Python program to print the uppercase letters in a string using a while loop and continue statement.
# string = "Hello, World!"
# i = 0

# while i < len(string):
#     if string[i].isupper():
#         print(string[i])
#     i += 1

# 8. Write a Python program to print the elements of a list skipping the elements divisible by 3 using a for loop and continue statement.
# numbers = [10, 21, 30, 45, 50, 63]

# for num in numbers:
#     if num % 3 == 0:
#         continue
#     print(num)

# 9. Write a Python program to iterate over a list of tuples and print only the tuples with a specific condition using a while loop and continue statement.
# tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]
# i = 0

# while i < len(tuple_list):
#     if tuple_list[i][0] % 2 == 0:
#         print(tuple_list[i])
#     i += 1

# 10. Write a Python program to print the numbers from 1 to 50, skipping the multiples of 7 using a for loop and continue statement.
# for i in range(1, 51):
#     if i % 7 == 0:
#         continue
#     print(i)
