# QUESTION 1:Write a program to get the factorial of a given number
# number = int(input("Enter the Number : "))
# factorial = 1
# while(number > 0):
#     factorial = number * factorial
#     number = number - 1
# print(f'The factorial of given number is {factorial}')

# QUESTION 2: Write a program to get fibonacci series of given range
# n = int(input("Enter the number : "))
# num1 = 0
# num2 = 1
# if(n<=0):
#     print(num1)
# else:
#     print(num1,num2,end=" ")
#     for i in range(2,n):
#         num3 = num1 + num2
#         print(num3,end =" ")
#         num1 = num2
#         num2 = num3

#QUESTION 3: Write the program for swapping two numbers with temp variable and without temp variable
# a = int(input("enter the first number : "))
# b = int(input("enter the second number : "))
# print(f'The numbers before swapping is {a,b}')
# c = a
# a = b
# b = c
# print(f'The numbers after swapping is {a,b}')

# a = int(input("enter the first number : "))
# b = int(input("enter the second number : "))
# print(f'The Numbers before swapping is {a,b}')
# a = a + b
# b = a - b
# a = a - b
# print(f'The Numbers after swapping is {a,b}')


# QUESTION 4: Write a given program to tell the user whether the given number is Even or Odd,Print out an appropriate message to user
# k = int(input("Enter the Number you want to check : "))
# if(k<0):
#     if(k%2==0): 
#         print(f'{k} is the Negative Even Number ')
#     elif(k%2!=0):
#         print(f'{k} is the Negative Odd Number ')
# elif(k%2==0):
#     print(f'{k} is the Positive Even Number')
# elif(k%2!=0):
#     print(f'{k} is the Positive Odd Number')


# QUESTION 5: Write a program to test whether the passed letter is vowel or not
alpha = (input("Enter the alphabet : "))
res = alpha.lower()
lis = ["a","e","i","o","u"]
if res in lis:
    print(f'{alpha} is the vowel')
else:
    print(f'{alpha} is not an vowel')
   
# QUESTION 6: Write apython program to sum of three given integers. However,if two values are equal sum will be zero
# int1 = int(input("Enter the First integer : "))
# int2 = int(input("Enter the Second integer : "))
# int3 = int(input("Enter the Third integer : "))
# sum = int1 + int2 + int3

# if(int1==int2 or int2==int3 or int1==int3):
#     print("The sum of given integers is 0 because value of any two integers is same.")
# else:
#     print(f'The sum of three Integers is {sum}')


# QUESTION 7: Write a program that will return true if the two given integer values are equal or their sum or difference is 5.
# value1 = int(input("Enter the First Integer : "))
# value2 = int(input("Enter the Second Integer : "))
# sum = 5
# difference = 5
# sum1 = value1 + value2
# difference1 = abs(value1-value2)
# print(value1 is value2 or sum is sum1 or difference is difference1)

# QUESTION 8:write a program to sum of the first n positive integers
# n = int(input("Enter the N no of terms : "))
# sum = n*(n+1)/2
# if(n<0):
#     print("Enter the Positive number")
# else:
#     print(f'The sum of first {n} terms is {sum}')

# QUESTION 9: write a program to calculate the length of string
# user_input_string = input("write anything you want : ")
# res = len(user_input_string)
# print(res)












