# While loop in python... 

count = 4 
while count <= 10:
    print(count)
    count +=1

names = ["Mustapha", "Mazeedah", "Samuel", "Kehinde"]
counter = 0 
while counter < len(names):
    # print(names[counter])
    if names[counter] == "Mazeedah":
        counter +=1
        continue
    print(names[counter])
    counter +=1
print("The code are doing the same thing #############################")    
name_to_skip ="Mazeedah"
index = 0

while index < len(names):
    current_name = names[index]
    # Check if the current name is the one to skip
    if current_name == name_to_skip:
        # Skip this name and move to the next iteration
        index += 1
        continue
    
    print(current_name)
    
    index += 1