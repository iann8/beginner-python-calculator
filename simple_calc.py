print("Select operation.")
print("1.Multiply")
print("2.Divide")
print("3.Subtract")
print("4.Add")

operator = input("Enter an operator: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "1":
    result = num1 * num2
    print(round(result, 4))
elif operator == "2":
    result = num1 / num2
    print(round(result, 4))
elif operator == "3":
    result = num1 - num2
    print(round(result, 4))
elif operator == "4":
    result = num1 + num2
    print(round(result, 4))
else:
    print(f"{operator} is not a valid operator")
