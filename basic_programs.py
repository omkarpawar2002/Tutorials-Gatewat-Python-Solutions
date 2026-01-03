# Python program for Hello World
'''
print("Hello World")
'''

# Python program to add Two Numbers
'''
num1 = int(input("Enter first number :- "))
num2 = int(input("Enter second number :- "))
print(f"Addition of {num1} and {num2} is :- {num1 + num2}")
'''

# Python program to subtract two numbers
'''
num1 = int(input("Enter first number :- "))
num2 = int(input("Enter second number :- "))
print(f"Subtraction of {num1} and {num2} is :- {num1 - num2}")
'''

# Python Program to Multiply Two numbers
'''
num1 = int(input("Enter first number :- "))
num2 = int(input("Enter second number :- "))
print(f"Multiplication of {num1} and {num2} is :- {num1 * num2}")
'''

# Python program for Arithmetic Operations
'''
num1 = int(input("Enter first number :- "))
num2 = int(input("Enter second number :- "))
print(f"Addition of {num1} and {num2} is :- {num1 + num2}")
print(f"Subtraction of {num1} and {num2} is :- {num1 - num2}")
print(f"Multiplication of {num1} and {num2} is :- {num1 * num2}")
print(f"Division of {num1} and {num2} is :- {num1 / num2}")
print(f"Modulus of {num1} and {num2} is :- {num1 % num2}")
print(f"Floor Division of {num1} and {num2} is :- {num1 // num2}")
print(f"Exponent of {num1} and {num2} is :- {num1 ** num2}")
'''

# Python program to print Calendar
'''
import calendar

year = int(input("Enter year :- "))
month = int(input("Enter month :- "))
print(calendar.month(year,month))
'''

# Python program to find Largest of 2 Numbers
'''
num1 = int(input("Enter first number :- "))
num2 = int(input("Enter second number :- "))
if(num1 > num2):
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")
'''

# Python program to find Largest of 3 Numbers
'''
num1 = int(input("Enter first number :- "))
num2 = int(input("Enter second number :- "))
num3 = int(input("Enter third number :- "))
if(num1 > num2 and num1 > num3):
    print(f"{num1} is greater than {num2} and {num3}")
elif(num2 > num3):
    print(f"{num2} is greater than {num1} and {num3}")
else:
    print(f"{num3} is greater than {num1} and {num2}")
'''

# Python program for Leap Year
'''
year = int(input("Enter any year :- "))
if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("It is a Leap Year")
else:
    print("Not A Leap Year")
'''

# Python Program to Print Negative Numbers in a Range
'''
for i in range(-10,0):
    print(i)
'''

# Python Program to Print Positive Numbers in a Range
'''
for i in range(1,11):
    print(i)
'''

# Python program to find Positive or Negative
'''
num = int(input("Enter any number :- "))
if(num > 0):
    print(f"{num} is Positive")
else:
    print(f"{num} is Negative")
'''

# Python program to check Number Divisible by 5 and 11
'''
num = int(input("Enter any number :- "))
if(num % 5 == 0 and num % 11 == 0):
    print(f"{num} is divisible by 5 and 11")
else:
    print(f"{num} is not divisible by 5 and 11")
'''

# Python Program to Find the Sum and Average Of Three Numbers
'''
num1 = int(input("Enter first number :- "))
num2 = int(input("Enter second number :- "))
num3 = int(input("Enter third number :- "))
total = num1 + num2 + num3
avg = total / 3
print(f"Total is :- {total}")
print(f"Average is :- {avg}")
'''

# Python Program to Find the Average Of Two Numbers
'''
num1 = int(input("Enter first number :- "))
num2 = int(input("Enter second number :- "))
total = num1 + num2 
avg = total / 2
print(f"Average is :- {avg}")
'''

# Python Program to Get Current Date and Time
'''
import datetime

print(datetime.datetime.today())
'''