def Addition (n1,n2):
    return n1+n2

def  Subtraction(n1, n2):
    return n1-n2

def multiplication(n1,n2):
    return n1*n2

def Division(n1,n2):
    return n1/n2


operation ={
    "+":Addition,
    "-":Subtraction,
    "*":multiplication,
    "/":Division,
}


def calculation():
    num1=float(input("enter first number?: "))

    should_accomulate = True
    while should_accomulate :
        for symbol in operation:
         print(symbol)
        Operation = input("pic and operation ")
        num2 = float(input("what is the next number?"))
        print(operation[Operation])

        value = operation[Operation](num1,num2)
        print(value)

        choice = input("if you want to continue the operation then type Y or Type N for the ").lower()

        if choice == "y":
            num1=value
        else:
            should_accomulate=False
            print("\n")
calculation()            