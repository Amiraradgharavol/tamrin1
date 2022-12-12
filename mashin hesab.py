import math
x = int(input("plz enter your number :"))
if x == 1:
    c = float(input("plz enter your number :"))
    op = input("plz enter operathion :")
    
    if op == "sin":
        result = math.sin(math.radians(c))
    if op == "cos":
        result = math.cos(math.radians(c))
    if op == "tan":
        result = math.tan(math.radians(c))
    if op == "cot":
        result = math.cot(math.radians(c))
    if op == "factorial":
        c = int(c)
        result = math.factorial(c)
    if op == "radical":
        result = math.sqrt(c)


if x == 2 :

    a = float(input("plz enter first number:"))
    b = float(input("plz enter tow number:"))

    op = input("plz enter operation:")

    if op == "+":
        result = a + b
    if op == "-":
        result = a - b 
    if op == "*":
        rsult = a * b
    if op == "/":
        result = a / b
print(result)                    