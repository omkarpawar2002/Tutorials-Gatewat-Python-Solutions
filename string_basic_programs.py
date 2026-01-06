# Python Program for ASCII Value of a Single Character
'''
char = input("Enter any character :- ")
print(f"ASCII value of {char} is :- {ord(char)}")
'''

# Python program to print ASCII Value of Total Characters in a String
'''
string = input("Enter any string input :- ")
for i in string:
    print(f"ASCII value of {i} is {ord(i)}")
'''

# Python program to Concatenate Strings
'''
st_1 = "Hello"
st_2 = "World"
print(st_1 + ' ' + st_2)
'''

# Python program to Convert String to Uppercase
'''
st = input("Enter any string :- ")
print(f"String in uppercase :- {st.upper()}")
'''

# Python program to Convert String to Lowercase
'''
st = input("Enter any string :- ")
print(f"String in Lowercase :- {st.lower()}")
'''

# Python program to Copy a String
'''
st = input("Enter any string :- ")
print(f"String  :- {st} and ID {id(st)}")
new_st = st[:]
print(f"String  :- {new_st} and ID {id(new_st)}")
'''

# Python program to check Palindrome or Not
'''
st = input("Enter any string input :- ")
if(st == st[::-1]):
    print(f"{st} is Palindrome")
else:
    print(f"{st} is not Palindrome")
'''

# Python Program to Check If Two Strings are Anagram
'''
st1 = input("Enter first string :- ")
st2 = input("Enter second string :- ")
d1 = {}
d2 = {}
for i in st1:
    if(i not in d1):
        d1[i] = 1
    else:
        d1[i] += 1
for j in st2:
    if(j not in d2):
        d2[j] = 1
    else:
        d2[j] += 1
if(d1 == d2):
    print("Both String Are Anagrams")
else:
    print("Strings Are Not Anagrams")
'''

# Python program to Print the First Occurrence of a Character in a String
'''
st = input("Enter any string input :- ")
char = input("Enter any character :- ")
print(st.find(char))
'''

# Python program to Print the Last Occurrence of a Character in a String
'''
st = input("Enter any string input :- ")
char = input("Enter any character :- ")
print(st.rfind(char))
'''

# Python program to Print Characters in a String
'''
st = input("Enter any string input :- ")
for i in st:
    print(i)
'''

# Python program to find String Length
'''
string = input("Enter any string :- ")
print(f"Length of string is :- {len(string)}")
'''

# Total Occurrence of a Character in a string
'''
string = input("Enter any string input :- ")
d = {}
for i in string:
    if(i not in d):
        d[i] = 1
    else:
        d[i] += 1
print(f"Total Count Of Occurance Of Characters :- {d}")
'''

# Toggle Characters Case
'''
string = input("Enter any string input :- ")
print(string.swapcase())
'''