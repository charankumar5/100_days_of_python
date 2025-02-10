import os
from subprocess import call
call(["python", "art.py"])
bid_dictionary = {}
# TODO-1: Ask the user for input
def bid():
    name = input(str("What is your name?: "))
    bid_price = input(str("What is your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bid_dictionary[name] = int(bid_price)
    print(bid_dictionary)

# TODO-3: Whether if new bids need to be added
continue_bidding = True
name = input(str("What is your name?: "))
bid_price = input(str("What is your bid?: $"))
# TODO-2: Save data into dictionary {name: price}
bid_dictionary[name] = int(bid_price)
print(bid_dictionary)
while continue_bidding:
    next_bid = input(str("Are there any other bidders? Type 'Yes' or 'no'."))
    if next_bid == "Yes":
        os.system('cls')
        bid()
    elif next_bid == "no":
        # TODO-4: Compare bids in dictionary
        winner = ""
        for bidder in bid_dictionary:
            bid_amount = bid_dictionary[bidder]
            for alpha in bid_dictionary:
                if bid_amount > bid_dictionary[alpha]:
                    winner = bidder
        print(winner)




