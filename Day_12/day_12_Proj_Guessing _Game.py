import random

number = random.randint(0, 100)
attempts = 0

print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100..")

get_diff = True
while get_diff:
    difficulty = input("Choose difficulty, Type 'hard' or 'easy': ").lower()
    if difficulty == "hard":
        attempts = 10
        get_diff = False
    elif difficulty == "easy":
        attempts = 5
        get_diff = False
    else:
        print("Invalid difficulty, Type 'easy' or 'hard'")

def check_guess(_guess, num):
    if _guess == num:
        return "You got it, You win!"
    elif _guess > num:
        return "Too high!"
    else:
        return "Too low!"


attempting = True
while attempting:
    if attempts == 5:
        guess = int(input("Make a Guess: "))
        message = check_guess(guess, number)
        print(message)
        if message == "You got it, You win!":
            print("\n\n")
            attempting = False
            break
    else:
        guess = int(input("Guess Again: "))
        message = check_guess(guess, number)
        print(message)
        if message == "You got it, You win!":
            print("\n\n")
            attempting = False
            break
        print(f"You have {attempts} attempts remaining to guess the number.")
    
    attempts -= 1
    if attempts == 1:
        print("You have no more attempts\n")
        attempting = False
    
    
