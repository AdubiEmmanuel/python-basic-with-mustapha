""" 
variables in python,
data types,
python arithmetic operations,
Logical operations,
Comparism operators,
Assignment operators.
Structured data types [list, tuple, set, and dictionaries],
if,elif,else conditional statements, nested conditions.
Loop - for loop, while loop?
functions using def...,
String interpolation - f-strings, 
Indexing and slicing the list,
Modules
"""

profile = {'name':"Micheal", 'age':12, 'class':'primary 4'}
for i in profile:
    print(i)
print("###############") 
for i in profile.keys():
    print(i)
print("###############") 
for i in profile.values():
    print(i)
    
print("###############") 
for i in profile.items():
    print(i)
    
print("#####################")
for key,value in profile.items():
    print(key,value)
    
print("#####################")
for key,value in profile.items():
    print(key,"==",value)