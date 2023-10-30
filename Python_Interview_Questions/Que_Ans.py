#Q1) Reverse a given string
# Ans:
string= "hello i am a string"[::-1]
print(string)

#Q2) Check if a string is a palindrome
# Ans:
def isPalindrome(string):
    if(string == string[::-1]):
        return "The string is palindrome"
    else:
        return "The string is not palindrome"
string = input("Enter string :")
print(isPalindrome(string))

#Q3) Calculate the factorial of a number
#Ans:
n=5
factorial=1
for i in range(1, n+1):
    factorial*=i
print(f"The factorail of {n} is: {factorial}")

#Q4) Generate the nth Fibonacci number
#Ans:
def fabonacci(n):
    if n<=0:
        return "Input should be positive integer"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        fab_1, fab_2 = 0,1
        for _ in range(3, n+1):
            fab_1, fab_2= fab_2, fab_1+fab_2
            return fab_2
n=10
result = fabonacci(n)
print(f"The {n}th Fabonacci number is: {result}")

#Q5) Merge two sorted linked lists.
#Ans:
