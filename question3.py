# 1. User will input (3 ages).find the oldest one
# input_ages1 = int(input("Enter the first age : "))
# input_ages2 = int(input("Enter the second age : "))
# input_ages3 = int(input("Enter the third age : "))
# oldest_one = max(input_ages1,input_ages2,input_ages3)
# print(f'The Oldest age is : {oldest_one}')

# 2. write a program that will convert celsius value to fahrenheit
# c = int(input("Enter the value of Celsius : "))
# f = (9/5)*c + 32
# print(f'The value of celsius {c} degree will be {f} degree in fahreneit')

# 3. User will input 2 numbers .write a program to swap the numbers
# first_number = int(input("Enter the first number : "))
# second_number = int(input("Enter the second number : "))
# temp = first_number
# first_number = second_number
# second_number = temp
# print(f'The first number after swapping is {first_number} and the second number after swapping is {second_number}')

# 4. Write a program to reverse the number. Also check whether reverse is true
# n = int(input("Enter the number : "))
# temp = n
# rev = 0
# while(n>0):
#     rev = rev*10 + n%10
#     n = n//10
# print(f'The reverse of given number {temp} is {rev}')
# print(reversed(temp) is rev)

# 5. Check whether the given number is odd or even
# input_number = int(input("Enter the number :"))
# if(input_number%2==0):
#     if(input_number<0):
#         print(f'The given number {input_number} is Negative Even number')
#     elif(input_number>0):
#         print(f'The given number {input_number} is Even number')
# elif(input_number%2==1):
#     if(input_number<0):
#         print(f'The given number {input_number} is Negative Odd number')
#     elif(input_number>0):
#         print(f'The given number {input_number} is Odd number')

# 6. Whether given year is leap or not
# input_year = int(input("Enter the year : "))
# if((input_year%4==0 and input_year%100!=0 ) or (input_year%400==0)):
#     print(f'The given year {input_year} is leap year')
# else :
#     print(f'The given year {input_year} is not a leap year')

# 7. find the euclidean distance between two cordinates
# import math
# x1 = int(input("Enter the first cordinate of x : "))
# x2 = int(input("Enter the second cordinate of x : "))
# y1 = int(input("Enter the first cordinate of y : "))
# y2 = int(input("Enter the second cordinate of y : "))
# res = math.sqrt((x2 -x1)**2 + (y2 - y1)**2)
# print(f"The euclidean distance is {res}")

# 8. User input of three angles find out whether it will form triangle or not
# first_angle = int(input("Enter the first angle : "))
# second_angle = int(input("Enter the second angle : "))
# third_angle = int(input("Enter the third angle : "))
# sum = first_angle + second_angle + third_angle
# if(first_angle and second_angle and third_angle>=0):
#     if(sum==180):
#         print(f'The given three angles will form the triangle')
#     else:
#         print(f"The given three angles will not form the triangle ")
# elif(first_angle and second_angle and third_angle<0):
#     print(f'Please Enter the positive value of angles ')


# 9. Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
# cost_price = int(input("Enter the cost price : "))
# selling_price = int(input("Enter the selling price : "))
# if(cost_price and selling_price < 0):
#     print("Please enter the positive value")
# else:
#     if(cost_price == selling_price):
#         print("Neither a profit nor a loss")
#     elif(cost_price>selling_price):
#         print(f'You occur a loss of {cost_price - selling_price} rs')
#     else:
#         print(f'You occur a profit of {selling_price - cost_price} rs')

# 10. Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
# principle = int(input("Enter the principle amount : "))
# rate_of_interest = int(input("Enter the interest rate : "))
# time_period = int(input("Enter the time period : "))
# simple_interest = principle*rate_of_interest*time_period/100
# print(f'The simple interest is {simple_interest} rs ')


# 11. Write a program to find the volume of the cylinder.Also find the cost,when the cost of 1 litre milk is 40Rs.
# import math
# radius = int(input("Enter the value of Radius in metre : "))
# height = int(input("Enter the value of height in metre : "))
# volume_of_cylinder = round(math.pi*radius**2*height,2)
# print(f'The volume of cylinder is {volume_of_cylinder} m3')
# cost_of_milk = round(1000*volume_of_cylinder*40)
# print(f'The total cost of milk is {cost_of_milk} rs')

# 12. Write a program that will tell whether the given number is divisible by 3&6.
# input_number = int(input("Enter the number : "))
# if(input_number%3==0 and input_number%6==0 ):
#     print(f'The given number {input_number} is divisible by 3 and 6')
# elif(input_number%3==0):
#     print(f'The given number {input_number} is divisible by 3 ')
# elif(input_number%6!=0 and input_number%3!=0):
#     print(f'The given number {input_number} is not divisible by 3 and 6')

# 13. Calculate tha angle between hour hand and minute hand
# hour_hand = int(input("Enter the value of hour hand between 0 to 11 : "))
# minute_hand = int(input("Enter the value of minute hand between 0 to 59 : "))
# hour = hour_hand*30 + minute_hand/2
# min = minute_hand*6
# result = abs(hour - min)
# print(f'The angle between hour and minute hand is {result}')

# 14. Check whether the rectangles are overlapping or not.
# def rectangle(rect1,rect2):
#     if (rect1['bottom']>=rect2['top'] or rect1['top']<=rect2['bottom'] or rect1['left']>=rect2['right'] or rect1['right']<=rect2['left'] ):
#         return False
#     else:
#         return True
# rect1 = {'bottom':0, 'top':1, 'left':1, 'right':2}
# rect2 = {'bottom':0, 'top':1, 'left':0, 'right':3}
# print(rectangle(rect1,rect2))

# 15. Write a program that will give you sum of three digit 
input_number = int(input("Enter the three digit number : "))
temp = input_number
rev = 0
count = 0
while(input_number>0):
    count = count + 1
    input_number = input_number//10
if(count == 3):
    while(temp>0):
        rev = rev + temp%10
        temp = temp//10
    print(f'The sum of the digits is {rev}')
else:
    print(f'Please enter the three digit number ')
