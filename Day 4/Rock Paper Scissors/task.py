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
import random
options = [rock, paper, scissors]
your_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:"))
print(f"You chose: \n {options[your_option]}")

computer_option = random.randint(0,2)
print(f"Computer chose:\n {options[computer_option]}" )

if your_option < computer_option:
    print("Computer win.")
elif your_option == computer_option:
    print("Draw")
else:
    print("You win.")
