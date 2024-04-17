print("Hello world")

number = int(input("Enter the number: "))
if(number<0):
    print(f'{number} is negative')
elif(number>0):
    print(f'{number} is positive')
elif(number==0):
    print(f'{number} is zero')
else:
    print("try again")
