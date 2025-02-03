import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# option 1
bill_payer = random.choice(friends)
print(bill_payer)

# option 2:
index = random.randint(0,4)
print(friends[index])