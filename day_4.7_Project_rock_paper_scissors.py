import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choices = [rock, paper, scissors]

user_choice_index = int(input("What do you choose? (0 for Rock, 1 for Paper, 2 for Scissors): "))
choice = choices[user_choice_index]
print(choice)

comp_choice_index = random.randint(0, 2)
comp_choice = choices[comp_choice_index]
print(f"Computer chose: {comp_choice_index}")
print(comp_choice)

if comp_choice_index == user_choice_index:
  print("Its a draw")
elif user_choice_index == 0:
  if comp_choice_index == 1:
    print("Computer win.")
  else:
    print("You win.") 
elif user_choice_index == 1:
  if comp_choice_index == 0:
    print("You win.")
  else:
    print("Computer win.") 
elif user_choice_index == 2:
  if comp_choice_index == 0:
    print("Computer win.")
  else:
    print("You win.")
else:
  print("invalid choice")

