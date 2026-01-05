# Python Program to create a Set
'''
s = {10,20,30,40,50}
print(f"Original Set :- {s}")
'''

# Python program to Count Even and Odd Numbers in Set
'''
s = {10,20,30,43,50}
print(f"Original Set :- {s}")
even = odd = 0
for i in s:
    if(i % 2 == 0):
        even += 1
    else:
        odd += 1
print(f"Even Numbers :- {even}")
print(f"Odd Numbers :- {odd}")
'''

# Python program to Count Positive and Negative Numbers in Set
'''
s = {10,20,30,-40,-50}
positive = negative = 0
for i in s:
    if(i > 0):
        positive += 1
    elif(i < 0):
        negative += 1
print(f"Positive :- {positive}")
print(f"Negative :- {negative}")
'''

# Python program to Iterate Set Items
'''
s = {10,20,30,40,50}
for i in s:
    print(i)
'''

# Python program to Print Largest Set Item
'''
s = {10,20,30,40,50}
print(f"Largest element in set :- {max(s)}")
'''

# Python program to find Length of a set
'''
s = {10,20,30,40,50}
print(f"Length of Set :- {len(s)}")
'''

# Python program to Print Even Numbers in Set
'''
s = {10,20,33,40,50}
for i in s:
    if(i % 2 == 0):
        print(i)
'''

# Python program to Print Negative Numbers in Set
'''
s = {10,20,33,-40,50}
for i in s:
    if(i < 0):
        print(i)
'''

# Python program to Print Odd Numbers in Set
'''
s = {10,20,33,-40,50}
for i in s:
    if(i % 2 != 0):
        print(i)
'''

# Python program to Print Positive Numbers in Set
'''
s = {10,20,33,-40,50}
for i in s:
    if(i > 0):
        print(i)
'''

# Python program to find Sum of Even and Odd Numbers in Set
'''
s = {10,20,33,40,50}
even = odd = 0
for i in s:
    if(i % 2 == 0):
        even += i
    else:
        odd += i
print(f"Even Numbers total is :- {even}")
print(f"Odd Numbers total is :- {odd}")
'''

# Python program to find Smallest Set Item
'''
s = {10,20,30,40,50}
print(f"Smallest items in set :- {min(s)}")
'''