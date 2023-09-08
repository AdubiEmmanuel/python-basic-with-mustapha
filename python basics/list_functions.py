names = ["Jack", "Jake", "Dale"]
ages = [ 12, 45, 23]

# Len
print(len(names))
print(len(ages + names))

names.append("Mustapha")
print(names)

# extend 
names.extend(ages)
print(names)

# insert 

names.insert(7, "sleeping")
print(names)

names.pop(6)
print(names)

