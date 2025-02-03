def main():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))
    
    if height > 120:
        print("You can ride the rollercoaster.")
        age=int(input("What is your age? "))
        if age>18:
            print("You have to pay $12")
        elif age >12 & age <18:
            print("Your have to pay $7")
        else:
            print("You have to pay $5")
    else:
        print("Sorry you have to grow taller before you can ride.")
    return 0

if __name__ == "__main__":
    main()