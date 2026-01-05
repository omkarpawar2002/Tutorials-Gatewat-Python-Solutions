# Get Tuple Items
'''
t = (10,20,30,40)
print(f"Original tuple :- {t}")
print(t[0])
print(t[1])
print(t[2])
print(t[3])
'''

# Python Program to Print Tuple using string formatting
'''
t = (10,20,30,40)
print(f"Original tuple :- {t}")
'''

# Python Program to Print Even Numbers in Tuple
'''
t = (10,20,33,40)
for i in t:
    if(i % 2 == 0):
        print(i)
'''

# Python Program to Print Negative Numbers in Tuple
'''
t = (10,20,-30,40)
for i in t:
    if(i < 0):
        print(i)
'''

# Python Program to Print Positive Numbers in Tuple
'''
t = (10,20,-30,40)
for i in t:
    if(i > 0):
        print(i)

'''
# Python Program to Print Odd Numbers in Tuple
'''
t = (10,20,-33,40)
for i in t:
    if(i % 2 != 0):
        print(i)
'''

# Python Program to Print Smallest Item in a Tuple
'''
t = (10,20,30,40)
small = t[0]
for i in range(len(t)):
    if(t[i] < small):
        small = t[i]
print(f"Smallest Item are :- {small}")
'''

# Python Program to Print Largest Item in a Tuple
'''
t = (10,20,30,40)
large = t[0]
for i in range(len(t)):
    if(t[i] > large):
        large = t[i]
print(f"Largest Item are :- {large}")
'''

# Python Program to Find Largest and Smallest Item in a Tuple
'''
t = (10,20,30,40)
print(f"Original tuple :- {t}")
print(f"Smallest Item :- {min(t)}")
print(f"Largest Item :- {max(t)}")
'''

# Python Program to Print Tuple Items
'''
t = (10,20,30,40)
for i in t:
    print(i)
'''