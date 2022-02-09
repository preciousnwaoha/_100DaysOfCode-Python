print("Welcome to the Rollercoaster!")
# Get height from user
height = float(input("What is your height in m? "))

# convert height to centimeter
height_cm = round(height*100, 2)

# Initialize bill user will pay as 0
bill = 0

if height_cm > 120:
    age = int(input("What's your age? "))

    if age < 12:
        bill = 5
        print("Your bill is $5.")
    elif age < 18:
        bill = 7
        print("Your bill is $7.")
    else:
        bill = 12
        print("Your bill is $12.")

    want_photos = input("Do uo want photos? y or n. ")
    if want_photos == "y":
        bill = bill + 3
    
    print(f"The total bill is ${bill}")

else:
    print("Sorry, you cant go on the roller coster until your taller.")