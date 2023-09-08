# calling functions from another module

# import module1
# from module1 import add, subt, mult, div
from module1 import *
from math import *
from statistics import * 

nums = [11,2,2,4,5,6,7,8]

print("The mean is: ", mean(nums))

print(sqrt(4))
print(pi)
print(cos(30))
print(log(30))

print(add(2,3))
print(subt(2,3))