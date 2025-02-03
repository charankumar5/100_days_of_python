def main():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))
    
    if height > 120:
        print("You can ride the rollercoaster.")
        age=int(input("What is your age? "))
        if age>18:
            print("Adult ticket costs: $12")
            bill = 12
        elif age >12 & age <18:
            print("Teen ticket costs: $7")
            bill = 7
        else:
            print("Kids ticket costs: $5")
            bill = 5
        check= input("Do you want to take photo?, Type 'Y' for Yes and 'N' for No ")
        if check == "Y":
            print(f"Please pay in total: {bill+3}")
        else:
            print(f"please pay in total: {bill}")
    else:
        print("Sorry you have to grow taller before you can ride.")
    return 0

if __name__ == "__main__":
    main()