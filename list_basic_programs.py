# Python Program to Append an Item to a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li.append(101)
print(f"Updated List :- {li}")
'''

# Python Program to access List Index and Values
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
print(li[0])
print(li[1])
print(li[-1])
print(li[-2])
'''

# Python Program to add two Lists
'''
li_1 = [2,3,4]
li_2 = [10,20,30]
print(li_1 + li_2)
'''

# Python Program to Change List Items
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li[2] = 101
print(f"Updated List :- {li}")
'''

# Python Program for Arithmetic Operations on Lists
'''
li_1 = [1,2,3,4,5]
li_2 = [10,10,10,10,10]
add , sub , mul , div , flo , mod , exp = [], [], [] ,[], [], [], []
for i in range(len(li_1)):
    add.append(li_1[i] + li_2[i])
    sub.append(li_1[i] - li_2[i])
    mul.append(li_1[i] * li_2[i])
    div.append(li_1[i] / li_2[i])
    mod.append(li_1[i] % li_2[i])
    flo.append(li_1[i] // li_2[i])
    exp.append(li_1[i] ** li_2[i])
print(f"Addition :- {add}")
print(f"Subtraction :- {sub}")
print(f"Multiplication :- {mul}")
print(f"Division :- {div}")
print(f"Modulus :- {mod}")
print(f"Floor Division :- {flo}")
print(f"Exponent :- {exp}")
'''

# Python Program to Calculate the Average of List Items
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
avg = sum(li) / len(li)
print(f"Average of list :- {avg}")
'''

# Python Program to Clear a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li.clear()
print(f"Updated List :- {li}")
'''

# Python Program to check List is Empty or Not
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
if(li):
    print("List is Not Empty")
else:
    print("List is Empty")
'''

# Python Program to Check if the Element Exists in a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
print(20 in li)
'''

# Python Program to Clone or Copy a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li_copy = li.copy()
print(f"new List :- {li_copy}")
'''

# Python Program to Count Occurrence of an element in a List
'''
li = [1,2,3,4,1,1,2,3]
print("Original List :- ",li)
print(f"2 occurs {li.count(2)} times in list")
'''

# Python program to Count Even and Odd Numbers in a List
'''
li = [1,2,3,4,5,6,7,8,9]
even = odd = 0
for i in li:
    if(i % 2 == 0):
        even += 1
    else:
        odd += 1
print(f"Even elements in list :- {even}")
print(f"Odd elements in list :- {odd}")
'''

# Python program to Count Positive and Negative Numbers in a List
'''
li = [3,45,6,3,1,-23,-34,34]
positive = negative = 0
for i in li:
    if(i > 0):
        positive += 1
    elif(i < 0):
        negative += 1
print(f"Positive elements are :- {positive}")
print(f"Negative elements are :- {negative}")
'''

# Python program to find Length of a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
print("Length of list :- ",len(li))
'''

# Python program to find the List Difference
'''
li_1 = [34,21,4,6,78,4]
li_2 = [7,78,45,23,56,78]
s1 = set(li_1)
s2 = set(li_2)
s1_diff = s1 - s2
s2_diff = s2 - s1
li_1 = list(s1_diff)
li_2 = list(s2_diff)
print(li_2 + li_1)
'''

# Python Program to Find the Average of a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
avg = sum(li) / len(li)
print(f"Average of list :- {avg}")
'''

# Python Program to Merge Two Lists
'''
li_1 = [1,2,3,4,5]
li_2 = [10,20,30,40,50]
print(li_1 + li_2)
'''

# Python List Multiplication Program
'''
li = [1,2,3,4,5]
pro = 1
for num in li:
    pro *= num
print(f"Total Product Is :- {pro}")
'''

# Python program to find the Sum of All List Elements
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
print(f"Sum of all elements in list :- {sum(li)}")
'''

# Sum and Average of a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
print(f"Sum of list :- {sum(li)}")
print(f"Average of list :- {sum(li) / len(li)}")
'''

# Sum of Even and Odd List Numbers
'''
li = [10,20,3,40]
even = odd = 0
print(f"Original List :- {li}")
for i in li:
    if(i % 2 == 0):
        even += i
    else:
        odd += i
print(f"Sum of even numbers are :- {even}")
print(f"Sum of odd numbers are :- {odd}")
'''

# Left Rotate a List by n
'''
li = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
print(f"Original List :- {li}")
num = int(input("Enter how many elements you want to rotate from left :- "))
for i in range(num):
    res = li.pop(0)
    li.append(res)
print(f"Updated List :- {li}")
'''

# Right Rotate a List by n
'''
li = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
print(f"Original List :- {li}")
num = int(input("Enter how many elements you want to rotate from right :- "))
for i in range(num):
    res = li.pop()
    li.insert(0,res)
print(f"Updated List :- {li}")
'''

# Remove an item from a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li.remove(20)
print(f"Updated List :- {li}")
'''

# Remove the First element from a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li.pop(0)
print(f"Updated List :- {li}")
'''

# Remove the Last Element from a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li.pop()
print(f"Updated List :- {li}")
'''

# Iterate Over List Items
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
for i in li:
    print(i)
'''

# Interchange First and Last Elements in a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li[0],li[-1] = li[-1],li[0]
print(f"Updated List :- {li}")
'''

# Swap two items in a List
'''
li = [10,20,30,40]
print(f"Original List :- {li}")
li[1],li[-1] = li[-1],li[1]
print(f"Updated List :- {li}")
'''