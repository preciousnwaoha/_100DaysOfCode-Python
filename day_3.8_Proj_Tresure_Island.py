print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road = input("Your're at a crossroad, (left or right): ")

if road.upper() == "LEFT":
    choco = input("There's a trail of chocho sticks, (follow or wait): ")
    if choco.upper() == "FOLLOW":
        house = input("It leads to a house made of chocholates, (enter or leave): ")
        if house.upper() == "LEAVE":
            print("You turned back and dissappeared...\n")
            print("There are three doors in front of you...")
            doors = input("Open one, (red, yellow or blue): ")
            if doors.upper() == "RED":
                print("Sucked your soul fromyour body...")
                print("Game Over")
            elif doors.upper() == "YELLOW":
                print("You have found the Tresure!")
                print("You Win")
            elif doors.upper() == "YELLOW":
                print("Eaten by strange beast...")
                print("Game Over")
            else:
                print("Sorry, You Lose")
        else:
            print("A witch is behind the door...")
            print("She turns you into chocholate and...")
            print("Sorry, It's Game Over")
    else:
        wolves = input("You hear wolves, (run or hide): ")
        if wolves.upper() == "RUN":
            print("The wolve are getting closer...")
            tree = input("Theres a tree, (climb or go)")
            if tree.upper() == "CLIMB":
                print("Best decision of your life, Wolves can't climb...")
                print("But they're waiting for you to fall...")
                boy = input("A boy is shows up on the tree and gives a hand. (take or no): ")
                if boy.upper() == "TAKE":
                    print("You turned back and dissappeared...\n")
                    print("There are three doors in front of you...")
                    doors = input("Open one, (red, yellow or blue): ")
                    if doors.upper() == "RED":
                        print("Sucked your soul fromyour body...")
                        print("Game Over")
                    elif doors.upper() == "YELLOW":
                        print("You have found the Tresure!")
                        print("You Win")
                    elif doors.upper() == "YELLOW":
                        print("Eaten by strange beast...")
                        print("Game Over")
                else:
                    print("Tree falls off...")
                    print("Boy disappears...")
                    print("It's Game Over")
            else:
                print("The wolves caught up with you..")
                print("Sorry, You're Gone. Game Over.")
        else:
            print("You get surrounded by sniffing wolves...")
            print("Oooops they've find you...")
            print("Game Over.")
else:
    print("You fell into a hole")
    print("Its Game Over.")