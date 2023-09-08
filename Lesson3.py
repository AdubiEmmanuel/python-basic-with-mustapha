# Lists, indexing and slicing
# List modules and functions.... sort, pop, index, reverse. 
# [] square brackets, {} curly brace, () - round bracket
name1 = ["Mustapha", "Mazeedah"] #list uses square bracket
name2 = {"Mustapha", "Mazeedah", "Mustapha"} #set usees curly brace
# a set cannot have repeated values  

name3 = ("Mustapha", "Mazeedah") #Tuple uses round bracket 
# tuple is immutable - i.e you cannot modify the content

print("The value of name1 index 0 is: ",name1[0])
# The index of a list is also the key of the list... 

print(type(name1))
print(type(name2))
print(type(name3))
print(len(name2))
s = set()
s.add(1)
print(s)
s.add(5)
print(s)
s.add(7)
print(s)
s.remove(5)
print(s)

# t = tuple()
# t.add(99)
# print(t)

# a dictionary is a key value pair data type. 
# dictionary also uses the same curly bracket with set 
student_profile = {"age":12, "name":"Tomiwa", "class":"Jss2"}
nested_list = [[2,3,4],[1,2,3]] #nested list 
print(student_profile)
print(nested_list[1][0:])

# 1. Create a nested list containing 4 child list in the parent list 
# 2 use list slicing to pring element from the second child list
# 3 use list slicing to pring element from the third child list... 
# Create a dictionary about your_profile, set name, age, height, fav_food
# print the dictionary... 


