# Write a program to count the occurences of substring in string

# str1 = "abcabcabcabcbaba"
# sub_str = "ca"
# res = str1.count(sub_str)
# print(f'The number of substring is : {res}')

# Write a program to count the occurences of each word in given sequence

# given_sentence = "Good morning , How are you , I am Good"
# given_word = "Good"
# a = []
# count = 0
# a = given_sentence.split(" ")
# for i in range(0,len(a)):
#     if(given_word==a[i]):
#         count = count + 1
# print("Count of the word is : ",count)


# Write a program to get a single string from two given string, separated by space and swap the first two charcters of each string.

# str1 = "Hello"
# str2 = "World"
# new_str1 = list(str1)
# new_str1[0],new_str1[1] = new_str1[1],new_str1[0]
# list_new = "".join(new_str1)

# new_str2 = list(str2)
# new_str2[0],new_str2[1] = new_str2[1],new_str2[0]
# list_new2 = "".join(new_str2)
# print(list_new,list_new2)
# res = str1 + " " + str2
# print(res)

# Write a program to add 'ing' at the end of a given string(len should be atleast 3). If given string is already end with 'ing' then add 'ly' if len is less than 3 leave it unchanged.

# str1 = input("Enter the String : ")
# modified_str1 = list(str1)
# res2 = modified_str1[-3:]
# res3 = "".join(res2)
# res =  len(str1)
# if res >=3 :
#     if res3 == "ing":
#         print(str1 + "ly")
#     else: print(str1 + "ing")
# elif res<3:
#     print(str1)


# Write a python function that take list of words and returns the length of longest one.

# def list1(words):
#     res =  max(words,key=len)
#     print(f'The word with longest length is : {res} and the its length is {len(res)}')
# a = ["one","two","three"]
# list1(a)    

# Write a python function to reverse a string if its length is a multiple of 4.

# def reverse_string(string):
#     if len(string)%4 == 0:
#         return "".join(reversed(string))
#     else:
#         return string
# obj1 = reverse_string("abcd")
# obj2 = reverse_string("hello")
# print(f'The reversed string is {obj1}')
# print(f'The string is {obj2}')

# write a program to get a string made of the first 2 and the last 2 chars from a given string. if the string length is less than 2 return instead of the empty string.
# given_string = "Helloworld"
# res = given_string[0:2]
# res2 = given_string[-2:]
# new_string = []
# new_string.append(res)
# new_string.append(res2)
# if len(given_string)>=3:
#     res3 = "".join(new_string)
#     print(res3)
# else:
#     print("The String is Empty : ", " ")

# write python function to insert a string in the middle of a string.

# def input_string(str,words):
#     return str[:2] + words + str[2:]
# print(input_string("World","{}"))


#  Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring  with 'good'. Return the resulting string. 
def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')
    if (spoor>snot and snot>0 and spoor>0):
        str1 = str1.replace(str1[snot:(spoor+3)],"good")
        return str1
    else:
        return str1
print(not_poor("The lyrics is not that poor"))
print(not_poor("The lyrics is good"))
