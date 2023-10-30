# 1. Write a Python program to count the number of characters in a string.

# string = 'Hello I am a string'
# count = 0
#
# l = len(string) - string.count(" ")
#
# for i in range(0, l):
#     if (string !=''):
#         count = count+1
# print("Total nuber of characters in string: ",str(count))

#2. Write a Python program to reverse a string.

# string = "Hello I am a string"[:: -1]
# print(string)

#3. Write a Python program to check if a string is a palindrome.

# def isPalindrome(string):
#     if (string == string[::-1]):
#         return "The string is palindrome"
#     else:
#         return "The string is not palindrome"
# string = input("Enter string: ")
# print(isPalindrome(string))

#4. Write a Python program to remove all the vowels from a string.

# def remove_vowels(string):
#     vowels = ['a','e','i','o','u','A','E','I','O','U']
#     result = ""
#     for char in string:
#         if char not in vowels:
#             result += char
#     return result
#
# input_string = input("Enter string: ")
# output_string = remove_vowels(input_string)
# print(output_string)

#5. Write a Python program to find the first non-repeating character in a string.

# string = "india"
# index = -1
# fnc = ""
#
# if len(string)==0:
#     print("Empty string")
#
# for i in string:
#     if string.count(i)==1:
#         fnc += i
#         break
#     else:
#         index+= 1
#     if index==len(string)-1:
#         print("All characters are repeting")
#     else:
#         print("First non-repeting character is :", i)
#-------------------------------------------------------------
# str = "pune"
# l = len(str)
# flag = 0
# for i in range(l):
#     flag = 0
#     for j in range(l):
#         if str[i] == str[j] and i != j:
#             flag = 1
#             break
#     if flag == 0:
#         print("First non-repeating character is :", str[i])
#         break
#
# if flag == 1:
#     print("No non-repeating character")
#6. Write a Python program to capitalize the first letter of each word in a string.

# string = "hello i am an indian and i am proud of it"
# result = string.title()
# print(result)

#7. Write a Python program to check if a string is an anagram of another string.

# def check(string1, string2):
#     if (sorted(string1)== sorted(string2)):
#         print("The strings are anagrams")
#     else:
#         print("The strings are not anagrams")
# string1 = input("Enter string1: ")
# string2 = input("Enter string2: ")
# check(string1, string2)

#8. Write a Python program to find the most frequent character in a string.

# string = "aabbbccccdddddeeeeeee"
# char_freq={}
# for i in string:
#     if i in char_freq:
#         char_freq[i]=char_freq[i]+1
#     else:
#         char_freq[i]=1
# result = max(char_freq, key=char_freq.get)
# print("Most frequent character: ", result)

#9. Write a Python program to check if a string is a valid email address.
# import re
#
# def validate_email(email):
#     if re.match(r"[^@]+@[^@]+\.[^@]+", email):
#         return True
#     else:
#         return False
#
# email= input("Enter your email: ")
#
# if validate_email(email):
#     print("Valid email address")
# else:
#     print("Invalid email address")

#10. Write a Python program to find the length of the longest substring without repeating characters.


# name = "Mangesh Kashid"
# a = name.split()
# rev_name =""
# for i in a:
#     rev_name = rev_name+ ' '+ i[::-1]
#     print(rev_name)

# num_pairs = []
#
# for i in range(5):
#     num = int(input("Enter a number: "))
#     num_pairs.append((num, num*2))
#
# print(num_pairs)

# t = ((3,10),(2,4),(5,1))
# sorted_t = sorted(t, key=lambda a: a[1])
# print(sorted_t)

