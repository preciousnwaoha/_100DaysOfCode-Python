print("Welcome to Python Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0;

if size == "S":
    bill = bill + 15
    if add_pepperoni == "Y":
        bill = bill + 2
elif size == "M":
    bill = bill + 20
    if add_pepperoni == "Y":
        bill = bill + 3
elif size == "L":
    bill = bill + 25
    if add_pepperoni == "Y":
        bill = bill + 3
else:
    print("Invalid size!")

if extra_cheese == "Y":
    bill = bill + 1

print(f"Your final bill is: ${bill}")