def main():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm?"))
    
    if height > 120:
        print("You can ride the rollercoaster.")
    else:
        print("Sorry you have to grow taller before you can ride.")
    return 0

if __name__ == "__main__":
    main()