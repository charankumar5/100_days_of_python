def main():
    number=int(input("Enter a number to find even or odd! "))
    evenOdd = number % 2
    if evenOdd == 0:
        print(f"Entered number {number} is even number!")
    else:
        print(f"Entered number {number} is odd number!")
    return 0

if __name__ == "__main__":
    main()