
while True:
    num1 , num2 = map(float,input("Enter The First Number Then Second Number: ").split())
    operator = str(input("Enter Which Operator You Need (+ - * /) : "))
    
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print(num1 / num2)
    else:
        break
