def main():
    print("Welcome to the tip calculator!")
    totalBill = int(input("What was the total bill? $"))
    #print(totalBill)
    yourTip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    #print(yourTip)
    splitBill = int(input("How many people to split the bill? "))
    #print(splitBill)
    youPay = (totalBill/splitBill)*(1+yourTip/100)
    print(f"Each person should pay: {youPay}")
    return 0

if __name__=="__main__":
    main()