#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply

def multi(n1, n2):
    return n1 * n2

#division


def div(n1 ,n2):
    return n1 / n2


calculator = {
    "+": add,
    "-": subtract,
    "*": multi,
    "/": div
}    
def fresh():
    num1 = int(input("what is the first number\n"))
    operation = True
    while operation:
      num2 = int(input("what is the second number\n"))

            for calu in calculator:
            print(calu)  

     calu_symbol =input("what is the operation you want to choose\n")

     new_symbol = calculator[calu_symbol]

     answer = new_symbol(num1 ,num2)

    print(f"{num1} {calu_symbol} {num2} {answer}")

     if input("do you want to continue press y other wise press no") == "y":
            num1= answer
        else:
            operation = False 
            fresh()