""" 
Creating a function that takes the first
and last name from a user and use these information
to generate an email for the user. 
"""

def email_generator(first_name, last_name):
    email = f"{first_name}.{last_name}@gmail.com".lower()
    return email 


    """
    Create a function that takes a list of numbers and print the 
    repeated number
    """

def num_repeat(num):
    for i in num:
        if num.count(i) > 1:
            print(f"The item that got repeated is {i} and it was repeated {num.count(i)}", )
            break
        
""" 
Take a list of names, print names that start with s
"""

def name_startswith(names):
    for i in names:
        if i.startswith("M"):
            print(i)
            break 

""" 
Function that calculate the area of a circle using the accepted mathematical formular
(pi * r)**2
"""
from math import pi 

def areaOfCircle(r):
    area = (pi * r) ** 2
    return area


    
