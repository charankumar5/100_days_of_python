from lib2to3.pgen2.grammar import opmap_raw


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return  n1 * n2

def divide(n1, n2):
    return  n1 / n2

operations = { "+" : add ,  "-" : subtract,  "*" : multiply,  "/" : divide}





def calculation():
    calculator_operation = True
    input1 = float(input("Please enter the first number: "))
    while calculator_operation:
        for symbol in operations:
            print(symbol)
        operation = input("Enter the mathematical operator: ")
        print("You have selected this operation to perform: " + operation)
        input2 = float(input("Please enter the second number: "))
        answer = operations[operation](input1, input2)
        print(f"final operation: {answer}")
        user_preference = input("You want to continue with the previous results, type 'yes' or 'no': ")
        if user_preference in " yes ":
            input1 = answer
        else:
            calculator_operation = False
            print("\n "* 50)
            calculation()
calculation()
