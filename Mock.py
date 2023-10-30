# input dict from user

dict = {}

dict_pairs = int(input("Enter num of key value pairs: "))

for i in range(dict_pairs):
    key = input("Enter key: ")
    value = input("Enter value: ")

    dict[key]= value
print("Dict is: ", dict)
