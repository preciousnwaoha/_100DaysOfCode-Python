import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Generate random numbers between 0 and the last index in names
# name_index = random.randint(0, len(names)-1)
# name = names[name_index]

name = random.choice(names)
print(f"{name} is going to buy the meal today!")

