def main():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M or L: ")
    pepporoni = input("Do you want pepporoni on your pizza? Y or N: ")
    extra_cheese = input("Do you wnat extra cheese? Y or N: ")
    bill = 0
    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    else:
        bill += 25
    
    if pepporoni == "Y" and size == "S":
        bill += 2
    elif pepporoni == "Y" and (size == "M" or size == "L"):
        bill +=3
    
    if extra_cheese == "Y":
        bill +=1
        
    print(f"Your final bill is: {bill}.")
    return 0

if __name__=="__main__":
    main()