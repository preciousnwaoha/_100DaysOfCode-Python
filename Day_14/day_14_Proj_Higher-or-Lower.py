# from art import logo, vs
from game_data import data
import random
# from replit import clear


def format_account(acc):
    '''Format the account data into printable format.'''
    acc_name = acc['name']
    acc_descr = acc['description']
    acc_country = acc['country']
    return f"{acc_name}, a {acc_descr}, from {acc_country}"


def check_ans(guess, a_followers, b_followers):
    '''Take the use guess and follower counts and returns if the gost it right.'''
    if a_followers > b_followers:
        return guess == 'a'
    elif b_followers > a_followers:
        return guess == 'b'
    else:
        return guess == 'ab'



# Display Art
#print(logo)

score = 0
game_should_continue = True
account_b = random.choice(data)
# make gane repeatable
while game_should_continue:

    # Generate random account from game data
    
    # Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_account(account_a)}.")
    # print(vs)
    print(f"Against B: {format_account(account_b)}.")

    # Ask user for a guess and make sure it is valid
    valid_guess = False
    while not valid_guess:
        valid_guesses = ['a', 'b', 'ab']
        guess = input("Who has more followers? 'A', 'B' or 'AB' if they have same following: ").lower()
        if guess in valid_guesses:
            valid_guess = True


    # Check if user if correct, set_usecase
    ## Get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    ## Use if statement to check if user is correct
    is_correct = check_ans(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    # clear()
    # print(logo)
    
    # Give user feedback on thier guesss.

    # Score keeping
    if is_correct:
        score *= 2
        print("You're right")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.\n")