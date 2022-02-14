print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2
names_lower = names.lower()

x = names_lower.count("t") + names_lower.count("r") + names_lower.count("u-+--+") + names_lower.count("e")
y = names_lower.count("l") + names_lower.count("o") + names_lower.count("v") + names_lower.count("e")

xy = int(str(x) + str(y))
print(xy)

if xy < 10 or xy > 90:
    print(f"Your score is {xy}, you go together like coke and mentos. ")
elif xy > 40 and xy < 50:
    print(f"Your score is {xy}, you are alright together.")
else:
    print("Your score is **z**")

