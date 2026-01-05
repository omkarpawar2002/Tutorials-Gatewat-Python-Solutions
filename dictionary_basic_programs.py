# Python Program to Add Key-Value Pair to a Dictionary
'''
student = {}
student["name"] = "kirti"
student["age"] = 23
print(student)
'''

# Python program to Check if a Given key exists in a Dictionary
'''
student = {
    'first_name':'kiran',
    'last_name':'desai',
    'age':23,
    'city':'pune'
}
print('location' in student)
'''

# Python program to Count words in a String using Dictionary
'''
st = input("Enter any string input :- ")
new = st.split()
d = {}
for i in new:
    if(i not in d):
        d[i] = 1
    else:
        d[i] += 1
print(d)
'''

# Python program to Create Dictionary of keys from 1 to n and values are square of keys
'''
num = int(input("Enter any number :- "))
d = {num:num*num for num in range(1,num+1)}
print(d)
'''

# Python program to Create Dictionary of Numbers 1 to n in (x, x*x) form
'''
number = int(input("Enter any number :- "))
d = {num:num*num for num in range(1,number+1)}
print(d)
'''

# Python program to Map two lists into a Dictionary
'''
keys = ["one","two","three"]
values = [1,2,3]
d = dict(zip(keys,values))
print(d)
'''

# Merge Two Dictionaries
'''
student = {
    'first_name':'kiran',
    'last_name':'desai',
    'age':23,
    'city':'pune'
}

marks = {
    "physics":89,
    "maths":56
}
student.update(marks)
print(student)
'''

# Multiply All Items in a Dictionary
'''
d = {
    'one': 1, 
    'two': 2, 
    'three': 3
}
pro = 1
for i,j in d.items():
    pro *= j
print(f"Product of Items :- {pro}")
'''

# Remove Given Key from a Dictionary
'''
student = {
    'first_name':'kiran',
    'last_name':'desai',
    'age':23,
    'city':'pune'
}
print(f"Original Dictionary :- {student}")
student.pop("last_name")
print(f"Original Dictionary :- {student}")
'''

# Sum of Items in a Dictionary
'''
d = {
    'one': 1, 
    'two': 2, 
    'three': 3
}
pro = 0
for i,j in d.items():
    pro += j
print(f"Sum of Items :- {pro}")
'''
