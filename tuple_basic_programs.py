# Python Program to add an Item to a tuple
'''
t = (10,20,30,40)
print(f"Original tuple :- {t}")
li = list(t)
li.append(101)
t = tuple(li)
print(f"Updated tuple :- {t}")
'''

# Python Program to create a Tuplea
'''
t = (10,20,30,40)
print(t)
'''

# Python Program to create Tuple of Different Types
'''
t = (10,"welcome",True,23.34)
print(t)
'''

# Python Program to Find Tuple Length
'''
t = (10,20,30,40)
print(f"Original tuple :- {t}")
print(f"Length of tuple :- {len(t)}")
'''

# Python Program to Remove an Item from Tuple
'''
t = (10,20,30,40)
print(f"Original tuple :- {t}")
li = list(t)
li.remove(20)
t = tuple(li)
print(f"Updated tuple :- {t}")
'''

# Python Program to Slice a Tuple
'''
t = (10,20,30,40)
print(f"Original tuple :- {t}")
print(t[::-1])
'''

# Python Program to Unpack Tuple Items
'''
t = (10,20,30,40)
print(f"Original tuple :- {t}")
a,b,c,d = t
print(a)
print(b)
print(c)
print(d)
'''

# Python Program to Create a Tuple with Numbers
'''
t = (10,20,30,40)
print(f"Original tuple :- {t}")
'''

# Python Program to Check Item exists in Tuple
'''
t = (10,20,30,40)
print(20 in t)
print(20 not in t)
'''

# Python Program to Find Sum of Even and Odd Numbers in Tuple
'''
even = odd = 0
t = (10,23,31,40)
for i in t:
    if(i % 2 == 0):
        even += i
    else:
        odd += i
print(f"Even :- {even}")
print(f"Odd :- {odd}")
'''

# Python Program to Find Sum of Tuple Items
'''
t = (10,20,30,40)
print(f"Sum of tuple :- {sum(t)}")
'''

# Python Program to Reverse Tuple
'''
t = (10,20,30,40)
print(f"Original tuple :- {t}")
print(f"Reversed tuple :- {t[::-1]}")
'''

# Count Positive and Negative Numbers in a Tuple
'''
t = (10,20,-30,40)
positive = negative = 0
print(f"Original tuple :- {t}")
for i in t:
    if(i > 0):
        positive += 1
    elif(i < 0):
        negative += 1
print(f"Positive Numbers are :- {positive}")
print(f"Negative Numbers are :- {negative}")
'''

# Count Even and Odd Numbers in Tuple
'''
t = (10,20,33,40)
even = odd = 0
print(f"Original tuple :- {t}")
for i in t:
    if(i % 2 == 0):
        even += 1
    else:
        odd += 1
print(f"Even Numbers are :- {even}")
print(f"Odd Numbers are :- {odd}")
'''