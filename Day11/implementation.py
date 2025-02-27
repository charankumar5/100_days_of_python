import random
from art import logo
# def __init__(, user_cards, choice, user_score, another_card, cards):
#     user_cards = user_cards
#     choice = choice
#     user_score = user_score
#     another_card = another_card
#     cards = cards
    
def initiate_game():

    initiate_game.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
    
    if user_choice == "y" or user_choice == "Y":
        print(logo)
        first_chance()
    else:
        print("end game!!..")
    return 0

def first_chance():
    first_chance.user_cards = []
    first_chance.choice = 0
    user_score = 0
    #print(random.randint(0,12))
    for I in range(0,2):
    #while len(user_cards) == 2:
        choice = initiate_game.cards[random.randint(0,12)]
        if choice not in first_chance.user_cards:
            first_chance.user_cards.append(choice)
    for J in first_chance.user_cards:
        user_score = user_score + J
    print(f"Your cards: {first_chance.user_cards}, current score: {user_score}")
    print(f"Computer's first card: {random.randint(0,12)}")
    return 0
def another_chance():
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "y" or another_card == "Y":
        first_chance.choice = initiate_game.cards[random.randint(0,12)]
        first_chance.user_cards.append(first_chance.choice)
    print(f"Your cards: {first_chance.user_cards}")
    return 0
def main():
    initiate_game()
    another_chance()
    return 0

if __name__=="__main__":
    main()
    
# if user_choice == "y" or user_choice == "Y":
#     print(logo)
    
#     # fetch the 2 rounds of cards and add them.
#     your_cards = []
#     your_score = 0
#     your_cards = random.sample(cards,2)
#     for i in your_cards: your_score+=i
#     computers_score = 0
#     computers_score = random.sample(cards,1)
#     print(f"Your cards: {your_cards}, current score: {your_score}")
#     print(f"Computer's firt card: {computers_score}")
#     continue_game = input(f"Type 'y' to get another card, type 'n' to pass: ")
#     if continue_game == "y" or continue_game == "Y":
#         your_cards.append(random.sample(cards,1))
#         your_score = 0
#         print(your_cards)
#         for i in your_cards: your_score+=i
#         print(f"Your cards: {your_cards}, current score: {your_score}")
        
        
# else:
#     print()