year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else :
            print("Not a Leap Year")
    else:    
        print("leap Year")
else:
    print("yNot a leap year")
