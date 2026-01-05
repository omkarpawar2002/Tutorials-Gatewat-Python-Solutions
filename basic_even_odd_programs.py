# Python Program to find Odd or Even
'''
number = int(input("Enter first number :- "))
if(number % 2 == 0):
    print(f"{number} is Even Number")
else:
    print(f"{number} is Odd Number")
'''

# Python program to Print Natural number 1 to N
'''
number = int(input("Enter stoping number :- "))
for num in range(1,number + 1):
    print(num)
'''

# Python program to Print Natural Numbers in Reverse Order
'''
num = int(input("Enter any number :- "))
for num in range(num,0,-1):
    print(num)
'''

# Python program to Print Even Numbers from 1 to 100
'''
for number in range(1,101):
    if(number % 2 == 0):
        print(number)
'''

# Python program to print Odd Numbers from 1 to 100
'''
for number in range(1,101):
    if(number % 2 != 0):
        print(number)
'''

# Python Program to Print First 10 Even Natural Numbers
'''
count_even = 0
for number in range(1,100):
    if(number % 2 == 0):
        if(count_even < 10):
            print(number)
            count_even += 1
'''
        
# Python Program to Print First 10 Natural Numbers
'''
for num in range(1,11):
    print(num)
'''

# Python Program to Print First 10 Natural Numbers in Reverse
'''
for num in range(10,0,-1):
    print(num)
'''

# Python Program to Print First 10 Odd Natural Numbers
'''
count_odd = 0
for num in range(1,101):
    if(num % 2 != 0):
        if(count_odd < 10):
            print(num)
            count_odd += 1
'''

# Python Program to find the Sum and Average of Natural Numbers
'''
total = 0
num_length = 0
for number in range(1,101):
    total += number
    num_length += 1
avg = total / num_length
print(f"Total is :- {total}")
print(f"Average is :- {avg}")
'''

# Python Program to Read 10 Numbers and Find their Sum and Average
'''
count_num = 0
total = 0
while count_num < 10:
    num = int(input("Enter any number :- "))
    total += num
    count_num += 1
average = total / count_num
print(f"Total :- {total}")
print(f"Average :- {average}")
'''
    
# Python Program to Find the Sum of 10 Numbers and Skip Negative Numbers
'''
count_num = 0
total = 0
while count_num < 10:
    num = int(input("Enter any number :- "))
    if(num > 0):
        total += num
    count_num += 1
print(f"Total :- {total}")
'''

# Python Program to Find the Sum of 10 Numbers until user enters Positive Numbers
'''
count_num = 0
total = 0
while count_num < 10:
    num = int(input("Enter any number :- "))
    if(num > 0):
        total += num
        count_num += 1
print(f"Total :- {total}")
'''

# Python Program to find Sum of Natural Numbers
'''
num = int(input("Enter any number :- "))
total = 0
for i in range(1,num+1):
    total += i
print(f"Sum of Natural Number :- {total}")
'''

# Python Program to find Sum of Even Numbers
'''
total = 0
for num in range(1,11):
    if(num % 2 == 0):
        total += num
print(f"Total Sum Of Even Number :- {total}")
'''

# Python Program to find the Sum and Average of Natural Numbers
'''
total = num_count = 0
for num in range(1,11):
    total += num
    num_count += 1
average = total / num_count
print(f"Total Sum Of Natural Number :- {total}")
print(f"Average of Natural Number :- {average}")
'''

# Python Program to find the Sum of Odd Numbers
'''
total = 0
for num in range(1,11):
    if(num % 2 != 0):
        total += num
print(f"Total Sum Of Odd Number :- {total}")
'''

# Python Program to find the sum of Even and Odd Numbers
'''
even = odd = 0
for num in range(1,11):
    if(num % 2 == 0):
        even += num
    else:
        odd += num
print(f"Total Sum Of Even Number :- {even}")
print(f"Total Sum Of Odd Number :- {odd}")
'''

# Python Program to Read 10 Numbers and Find their Sum and Average
'''
total = count_num = 0
while count_num < 10:
    num = int(input("Enter any number :- "))
    total += num
    count_num += 1
average = total / count_num
print(f"Total is :- {total}")
print(f"Average is :- {average}")
'''