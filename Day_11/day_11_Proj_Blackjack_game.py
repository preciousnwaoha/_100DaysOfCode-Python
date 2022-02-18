import random
from webbrowser import get
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


play = input("do you want to play a game of blackjack type yes or no: ").lower()



def get_card():
    card_idx = random.randint(0, len(cards)-1)
    return cards[card_idx]

def get_sum(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

def play_game():
    your_cards = []
    comp_cards = []
    score = 0
    your_cards.append(get_card())
    comp_cards.append(get_card())
    another_play = True
    while another_play:
        your_cards.append(get_card())
        comp_cards.append(get_card())
        score = sum(your_cards)
        score_comp = sum(comp_cards)
        print(f"Your cards: {your_cards}, Current score: {score}")
        print(f"Computers first card: {comp_cards[0]}")

        if score > 21 or score_comp > 21:
            if score > 21 and score_comp > 21:
                print(f"Your final hand: {your_cards}, Your final score: {score}")
                print(f"Computer's final hand: {comp_cards}, Computer's final score: {score_comp}")
                print("Draw")
            elif score > 21:
                print(f"Your final hand: {your_cards}, Your final score: {score}")
                print(f"Computer's final hand: {comp_cards}, Computer's final score: {score_comp}")
                print("You went over. You lose.")
            else:
                print(f"Your final hand: {your_cards}, Your final score: {score}")
                print(f"Computer's final hand: {comp_cards}, Computer's final score: {score_comp}")
                print("Computer went over. You win.")
            another_play = False
        else:
            draw_another_card = input("Type 'y' if you want to draw another card or 'n' if not: ").lower()
            if draw_another_card == "n":

                if score == score_comp:
                    print(f"Your final hand: {your_cards}, Your final score: {score}")
                    print(f"Computer's final hand: {comp_cards}, Computer's final score: {score_comp}")
                    print("Its a draw")
                elif score > score_comp:
                    print(f"Your final hand: {your_cards}, Your final score: {score}")
                    print(f"Computer's final hand: {comp_cards}, Computer's final score: {score_comp}")
                    print("You win")
                else:
                    print(f"Your final hand: {your_cards}, Your final score: {score}")
                    print(f"Computer's final hand: {comp_cards}, Computer's final score: {score_comp}")
                    print("You Lose")

                another_play = False

        





play_game()