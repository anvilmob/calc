def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero.")

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = add(num1, num2)
    print("Result:", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("Result:", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("Result:", result)
elif choice == '4':
    try:
        result = divide(num1, num2)
        print("Result:", result)
    except ValueError as e:
        print("Error:", str(e))
else:
    print("Invalid input")
