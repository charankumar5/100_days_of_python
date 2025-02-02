def bandNameGenerate():
    print("Welcome to the Band Name Generator.")
    nameOfCity = input("What's the name of the city you grew up in? ")
    petName = input("What is your pet's name? ")
    print(f"Your band name could be {nameOfCity} {petName}")
    
    return 0


def main(): 
    
    bandNameGenerate()
    return 0

if __name__ == "__main__":
    main()