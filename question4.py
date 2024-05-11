# 1. Write a Python function to get the largest number, smallest number and sum of all from a list
# def numbers(*args):
#     for i in args:
#         print(f'The Largest number in list is {max(i)}')
#         print(f'The Smallest number in list is {min(i)}')
#         print(f'The sum of all the number in list is {sum(i)}')
# list1 = []
# n = int(input("Enter the number of elements you want to enter : "))
# for i in range(n):
#     num = int(input("Enter the numbers : "))
#     list1.append(num)
# numbers(list1)

# 2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# list1 = ["abc", "bcb", "aca", "1234", "12341", "7897", "123"]
# count = 0
# for i in list1:
#     if len(i)>1 and i[0] == i[-1]:
#         count = count + 1
# print(count)

# 3. Write a Python program to remove duplicates from a list.
# list1 = [1,2,3,4,3,1,2,1,2,3,3,4,5,6,7,4,52]
# res = list(set(list1))
# print(res)
# OR Another method
# def remove(duplicate):
#     final_list = []
#     for i in duplicate:
#         if i not in final_list:
#             final_list.append(i)
#     return final_list
# duplicate = [1,2,3,4,1,2,4,5,6,4,5]
# print(remove(duplicate))

# 4. Write a Python program to check a list is empty or not.
# def check_list(list1):
#       if(len(list1)!=0):
#             print("The list is not empty")
#       else:
#             print("The list is empty")
# list1 = []
# check_list(list1)

# 5. Write a Python function that takes two lists and returns true if they have at least one common member. 
# def check(list1,list2):
#     for i in list1:
#         for j in list2:
#             if(i==j):
#                 return True
#             else:
#                 return False
# list1 = [1,2,3,4]
# list2 = [11,12,13,14]
# print(check(list1,list2))

# 6. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
# z = [i**2 for i in range(2,30)]
# result1 = z[0:5]
# result2 = z[-5:]
# result1.extend(result2)
# print(result1)

# 7. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# def unique_list(list1):
#     new_list = []
#     for i in list1:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list

# list1 = [1,2,2,1,2,1,3,4,2,5,6,7,3,4,22,33,44,55,66,77,88,99,33,100]
# print(unique_list(list1))

# 8. Write a Python program to convert a list of characters into a string.
# list1 = ["P","Y","T","H","O","N"]
# result = "".join(list1)
# print(result)

# 9. Write a Python program to select an item randomly from a list.
# Fruits = ["Apple", "Banana", "Cherry", "Dragon fruit"]
# import random
# result = random.choice(Fruits)
# print(result)

# 10. Write a Python program to find the second smallest number in a list. 
# list1 = [33,5,67,23,45,66,79,90]
# list1.sort()
# print(f'The second smallest number in given list is {list1[1]}')

# 11. Write a Python program to get unique values from a list 
# list1 = [1,2,3,41,11,12,1,2,22,33,2,3,1]
# result = list(set(list1))
# print(result)

# 12. Write a Python program to check whether a list contains a sub list 
list1 = [5,6,7,8,3,2,3,8,4,5]
sub_list1 = [2,3,8,4]
res = False
for i in range(len(list1) - len(sub_list1) + 1):
    if list1[i:i+len(sub_list1)] == sub_list1:
        res = True
        break
print(res)

# 13. Write a Python program to split a list into different variables
# list1 = [5,10,15,20,25]
# a,b,c,d,e = [list1[i] for i in range(len(list1))]
# print(f'The variables are {str(a)},{str(b)},{str(c)},{str(d)},{str(e)}')
   

    

