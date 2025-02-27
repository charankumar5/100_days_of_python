import art
import random
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")

if user_choice is "y":
    print()
else:
    users_hand = []
    users_hand.extend(random.sample(cards,2))
    computers_hand = []
    computers_hand.extend(random.sample(cards,3))
    print(f"    Your final hand: {users_hand}, final score: {sum(users_hand)}")
    print(f"    Computer's  final hand: {computers_hand}, final score: {sum(computers_hand)}")
    if (sum(users_hand) > sum(computers_hand)) and (sum(users_hand) < 21) and (sum(computers_hand) < 21):
        print("You Win!")
    elif sum(users_hand) == sum(computers_hand):
        print("Draw")
    elif (sum(computers_hand) > 21) and (sum(users_hand) < 21):
        print("You Win!")
    else:
        print("You lose")