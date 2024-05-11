# 1. Write a program that will determine weather when the value of temperature and humidity is provided by the user. TEMPERATURE(C) HUMIDITY(%) WEATHER
# >=30 >=90 Hot and Humid 
# >=30 <90 Hot 
# <30 >=90 Cool and Humid
# <30 <90 Cool 
# Temperature = int(input("Enter the value of Temperature : "))
# Humidity = int(input("Enter the value of Humidity : "))
# if(Temperature>=30 and Humidity>=90):
#     print(f'The weather is hot and humid')
# if(Temperature>=30 and Humidity<90):
#     print(f'The weather is hot')
# if(Temperature<30 and Humidity>=90):
#     print(f'The weather is cool and humid')
# if(Temperature<30 and Humidity<90):
#     print(f'The weather is cool')

# 2. Write a program that will take three digits from the user and add the square of each digit.
# input_number = int(input("Enter the three digit number : "))
# hold = input_number
# rev = 0
# count = 0
# while(input_number>0):
#     count+= 1
#     input_number = input_number//10
# if(count==3):
#     while(hold>0):
#         rev = rev + (hold%10)**2
#         hold = hold//10
#     print(f'The sum of square of each digit is {rev}')
# else:
#     print(f'Please enter the three digit number ')

# 3. Write a program that will check whether the number is armstrong number or not.
# input_number = int(input("Enter the number : "))
# temp = input_number
# temp2 = input_number
# count = 0
# sum = 0
# while(input_number>0):
#     count+= 1
#     input_number = input_number//10
# while(temp>0):
#     sum = sum + (temp%10)**count
#     temp = temp//10
# if(sum==temp2):
#     print("The given number is armstrong number")
# else:
#     print("The given number is not a armstrong number")

# 4.  Write a program that will give you the inhand salary after deduction of HRA(10%), DA(5%), PF(3%), and tax (if salary is between 5-10lakh–10%),(11-20lakh–20%),(20<lakh–30%).
# input_salary = int(input("Enter your CTC : "))
# Hra_deduction = 0.1*input_salary
# Da_deduction = 0.05*input_salary
# Pf_deduction = 0.03*input_salary
# total_deductions = Hra_deduction + Da_deduction + Pf_deduction
# rem_ctc = input_salary - total_deductions
# if(rem_ctc<500000):
#     print(f'Your inhand salary is after deduction is {rem_ctc} rs')
# elif(rem_ctc>=500000 and rem_ctc<1000000):
#     print(f'Your inhand salary is after deduction is {rem_ctc - rem_ctc*0.1} rs')
# elif(rem_ctc>=1000000 and rem_ctc<2000000):
#     print(f'Your inhand salary is after deduction is {rem_ctc - rem_ctc*0.2} rs')
# elif(rem_ctc>=2000000):
#     print(f'Your inhand salary is after deduction is {rem_ctc -rem_ctc*0.3} rs')

# 5. Write a menu driven program-1.cm to ft 2.km to miles 3.usd to inr 
# centimetre = int(input("Enter the value of centrimetre :"))
# kilometre= int(input("Enter the value of kilometre :"))
# usd = int(input("Enter the value of usd :"))
# centimetre_conversion = centimetre*0.0328084
# kilometre_conversion = kilometre*0.621371
# usd_conversion = usd*83.39
# print(f'The value of {centimetre} CM is {centimetre_conversion} in Foot')
# print(f'The value of {kilometre} KM is {kilometre_conversion} in Miles')
# print(f'The value of {usd} USD is {usd_conversion} in INR')


# 6. Write a program that will swap numbers
# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number :  "))
# a = a + b 
# b = a - b 
# a = a - b
# print(f"The numbers after swapping will be {a,b}")

# 7. Write a program to find the sum of first n numbers,where n will be provided by the user
# input_number = int(input("Enter the no of terms you want to add : "))
# result = input_number*(input_number + 1)/2
# print(f"The sum of {input_number} numbers are : {result}")

# 8. Write a program that can multiply 2 numbers provided by the user without using the * operator 
# def multiply(a,b):
#     if(b<0):
#         return -multiply(a,-b)
#     elif b == 0:
#         return 0
#     elif b == 1:    
#         return a
#     else:
#         return a + multiply(a,b-1)
# obj1 = multiply(6,10)
# print(obj1)

# 9. Write a program that can find the factorial of a given number provided by the user.
# number = int(input("Enter the number for calculation of factorial : "))
# factorial = 1
# while(number>0):
#     factorial = number*factorial
#     number-= 1
# print(f"The factorial of given number is {factorial}")
    
# 10. Write a program to print the first 25 odd numbers
# result = [i for i in range(50) if i%2==1]
# print(result)

# 11. Write a program to print whether a given number is prime number or not
number  = int(input("Enter the number :"))
if number>1:
    for i in range(2,number):
        if (number%i == 0):
            print(number , "is not a prime number ")
            break
    else:
        print(number , "is a prime number")


# 12. Print all the armstrong numbers in the range of 100 to 1000
# for i in range(100,1001):
#     count = len(str(i))
#     temp = i
#     sum = 0
#     while(temp>0):
#         sum = sum + (temp%10)**count
#         temp = temp//10
#     if (sum == i):
#         print(sum)


