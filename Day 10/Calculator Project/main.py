from lib2to3.pgen2.grammar import opmap_raw
import art


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
    input1 = float(input("What's the first number? "))
    while calculator_operation:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        # print("You have selected this operation to perform: " + operation)
        input2 = float(input("What's the next number? "))
        answer = float(operations[operation](input1, input2))
        print(f"{input1} {operation} {input2} = {answer}")
        user_preference = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: " )
        if user_preference in " yes ":
            input1 = answer
        else:
            calculator_operation = False
            print("\n "* 50)
            calculation()
calculation()
