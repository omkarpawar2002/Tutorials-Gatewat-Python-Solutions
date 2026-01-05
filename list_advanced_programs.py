# Python program to Print Elements in a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
for i in li:
    print(i)
'''

# Python Program to Print List Items in Reverse Order
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li.reverse()
print(f"Updated List :- {li}")
'''

# Python Program to Print List Items Greater Than Average
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
avg = sum(li) / len(li)
for i in li:
    if(i > avg):
        print(i)
'''

# Python Program to Print List Items at Even Position
'''
li = [10,20,30,40]
for index,ele in enumerate(li):
    if(index % 2 == 0):
        print(ele)
'''

# Python Program to Print List Items at Odd Position
'''
li = [10,20,30,40]
for index,ele in enumerate(li):
    if(index % 2 != 0):
        print(ele)
'''

# Python Program to Print Even Numbers in a List
'''
li = [10,23,30,40]
for i in li:
    if(i % 2 == 0):
        print(i)
'''

# Python program to Print Odd List Numbers
'''
li = [10,23,30,40]
for i in li:
    if(i % 2 != 0):
        print(i)
'''

# Python program to Put Even and odd Numbers in Separate List
'''
even = []
odd = []
li = [10,20,33,40]
for i in li:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
'''

# Python program to Print Positive Numbers
'''
li = [10,20,-30,40]
for i in li:
    if(i > 0):
        print(i)
'''

# Python program to Print Negative Numbers
'''
li = [10,20,-30,40]
for i in li:
    if(i < 0):
        print(i)
'''

# Python program to Put Positive and Negative Numbers in Separate List
'''
positive , negative = [] , []
li = [10,20,-30,40]
for i in li:
    if(i < 0):
        negative.append(i)
    elif(i > 0):
        positive.append(i)
print(f"Positive Number :- {positive}")
print(f"Negative Number :- {negative}")
'''

# Python program to Print the Largest Number in a List
'''
li = [10,20,30,40]
print(f"Largest Number is :- {max(li)}")
'''

# Python program to Print the Second Largest Number in a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li.sort()
print(f"Second Largest :- {li[-2]}")
'''

# Python program to Print the Largest and Smallest Number
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
print(f"Largest :- {max(li)}")
print(f"Smallest :- {min(li)}")
'''

# Python program to Print the Smallest Element in a List
'''
li = [10,20,30,40]
print(f"Smallest :- {min(li)}")
'''

# Python program to Remove Duplicates from List
'''
li = [10,20,30,40,20,40]
new_li = []
for i in li:
    if(i not in new_li):
        new_li.append(i)
print(f"Updated List :- {new_li}")
'''

# Python program to Remove Even Numbers in a List
'''
li = [10,20,33,40]
print(f"Original List :- {li}")
li = [i for i in li if(i % 2 != 0)]
print(f"Updated List :- {li}")
'''

# Python program to Reverse List Items
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li.reverse()
print(f"Updated List :- {li}")
'''

# Python program to Sort List Items in Ascending Order
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li.sort()
print(f"Updated List :- {li}")
'''

# Python Program to Sort List Items in Descending Order
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li.sort(reverse=True)
print(f"Updated List :- {li}")
'''