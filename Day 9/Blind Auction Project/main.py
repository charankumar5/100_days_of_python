from art import logo
# TODO-1: Ask the user for input
print("Welcome to the secret auction program.")
Bids = {}
name  = input("Enter your name? ")
bid_amount = int(input("What's your bid?$ "))
Bids[name] = bid_amount
# TODO-3: Whether if new bids need to be added
while True:
    confirm = input("Are there any other bidders? Type 'yes' or 'no'." ).lower()
    if confirm == "no":
        break
    else:
        name  = input("Enter your name? ")
        bid_amount = int(input("What's your bid?$ "))
        Bids[name] = bid_amount
# TODO-2: Save data into dictionary {name: price}
max_bid = 0
winner = ""
for key, value in Bids.items():
    if value > max_bid:
        max_bid = value
        winner = key
print(f"The winner is {winner} with a bid of ${max_bid}")        









