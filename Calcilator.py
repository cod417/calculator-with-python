# Calculator
# Add
def add(n1,n2):
    return n1 + n2
# Sub
def sub(n1,n2):
    return n1 - n2
# mul
def mul(n1,n2):
    return n1* n2
# divide
def divide(n1,n2):
    return n1/ n2
# declare dictionary here and it will in the form of keys and value
#    where the keys should be the the Operator "+",+"-", and value should be the function 

operations = {
"+":add,
"-":sub,
"*":mul,
"/":divide
}
num1 = int(input("Whats the first number?:"))

for symbol in operations:
    print(symbol)

operations_symbol = input("Pick an operation from the line above:")
num2= int(input(("What is the second number?:")))

calculation_function = operations[operations_symbol]
answer = calculation_function(num1,num2)

print(f"{num1} {operations_symbol} {num2}={answer}")




