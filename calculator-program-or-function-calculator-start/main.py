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

num1 = int(input("what is the first number\n"))
num2 = int(input("what is the second number\n"))

for calu in calculator:
    print(calu)  

calu_symbol =input("what is the operation you want to choose\n")

new_symbol = calculator[calu_symbol]

answer = new_symbol(num1 ,num2)

print(f"{num1} {calu_symbol} {num2} {answer}")