# # # write a program to chek number is possitive or not
# # num = int(input("Please enter a number to find is it positive or not : "))

# # if num >= 0:
# #     print ("is a positive number")
# # else:
# #     print("its not a positive number")

# #write a program for the odd and even number
# num = int(input("Please enter a number to find is it positive or not : "))
# if num % 2 == 0:
#     print("it is a odd number")
# else:
#     print("it is a even number")

# print ("*****Area calculor*****")
# print (""" press 1 to get a area of square 
#        press 2 to get area of rectangle
#        press 3 to get area of triangle""")

# choice = int(input("enter a numer between from 1 - 3 : "))

# if choice == 1:
#     side = float(input("enter the lenght of side:"))
#     area = side ** 2 
#     print("the square of area is ", area )
# elif choice == 2:
#     lenght = float(input("enter the lenght:"))
#     breath = float(input("enter the breath: "))
#     area = lenght * breath
#     print("the are of reactangle is", area )
# elif choice == 3:
#     lenght = float(input("enter the lenght:"))
#     breath = float(input("enter the breath: "))
#     height = float(input("enter the height:"))
#     area = lenght * breath*height
#     print("the are of reactangle is", area )
# else:
#     print("invalid strenght")

# write a program to find wheater it is asingle digit or not
# num = int(input("Please enter a number : "))

# if num >= 0 and num <= 9:
#     print(num, "is a single digit number")
# elif num >= 10 and num <= 99:
#     print(num, "is a two digit number")
# elif num >= 100 and num <= 999:
#     print(num, "is a three digit number")
# elif num >= 1000 and num <= 9999:
#     print(num, "is a four digit number")
# else:
#     print("invalid lenght please enter atleat 4 digit number")


# #create a table 
# n = int(input("enter any number:"))
# for  i in range(1,11):
#     print(n, "x", i,"=", n*i)


# while True:
#     num1 = int(input("please enter the number: "))
#     num2 = int(input("please enter the number: "))
#     print(num1 + num2)

#     stop = input(" do u want to stop the program(Y/N): ")
#     if stop == "Y":
#         break


# n = 0
# for i in range(1,51):
#     if i % 2 == 0:
#         n += i
#         print(n)

# # create a sqaure of the number 
# for i in range(1,21):
#     print(i, "sqaure is", i**2)


# num = 0
# n = 0
# while n <= 20:
#     if n%2 != 0:
#         num += n
#         n += 1
#         print(num)

# n = int(input("please enter a number upto 100: "))
# if n%8 == 0 and n%5 == 0:
#     print(n, "is divisible by 8 and 5 ")
# else:
#     print(n," given number is not divisble by 8 and 5")

# create a shopmark system
# while True:
#     Name = input("please enter your name: ")
#     total = 0
#     while True:
#         print("enter the amt and quantity")
#         quantity = int(input("enter the quantity: "))
#         amt = int(input("enter the amt: "))
#         total += quantity + amt
#         repeat = input("is there any another product u want to add to cart Y/N: ") 
#         if repeat == "no" or repeat == "NO":
#             break
#     print("thing are added to carts succsesfully, please kindly wait for the bill to get generate")
#     print("***************************************************************************")
#     print("Name: ", Name)
#     print ("your total amount is ", total)
#     print("*****************************************************************************")
#     print ("Thank for shopping do pay the bill at the pay counter")
#     repeat1 = input("do u wnat to continue again: Y/N") 
#     if repeat1 == "n" or "NO":
#         break

# to find the lenght of the sting
# n = input("enter a string to find it lenght: ")
# print(len(n))

# n = input("enter a string to find count of o occuring: ")
# print(n.count("o"))

# n = input("enter a string need to convert in lower or upper case: ")
# x = input("chose lower or upper case: ")
# if x == "Lower" or x == "Lower":
#     print(n.lower())
# elif x == "UPPER" or x == "upper":
#     print(n.upper())
# elif x == "title":
#     print(n.title())
# else:
#     print("Please select either 'upper, 'lower','title': ")

# for i in range (1,6):
#     for j in range(6,i,-1):
#         print(i, end=" ")
#     print()

# fibonacci seried
# a = 1
# b = 0
# n = int(input("enter a number her : "))
# if n == 1:
#     print(1)
# else:
#     print(a)
#     print (b)
#     for i in range(2,n):
#         c = a+b
#         a = b
#         b = c
#         print(c)

# num = int(input("enter a value here: "))
# if num%2 != 0:
#     print(num, "it is a prime number")
# else:
#     print(num, "is not a prime number: ")

# num = int(input("enter a value here: "))
# x = lambda num : num*2
# print(x(num))


