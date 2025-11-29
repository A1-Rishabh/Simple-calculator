# Simple Calculator Application- rishabh
def add(a, b):# Addition function
    return a + b

def subtract(a, b):# Subtraction function
    return a - b

def multiply(a, b):# Multiplication function
    return a * b

def divide(a, b):# Division function
    if b == 0:
        return "Error! Division by zero." # Handle division by zero
    return a / b

def main():
    print("==== Simple Calculator ====")
    print("Operations Available:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("closing calculator...")
            break

        if choice not in ['1','2','3','4']:
            print("Invalid choice! Try again.")
            continue

        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        if not (num1.replace('.','').isdigit() and num2.replace('.','').isdigit()):
            print("Invalid number input! Try again.")
            continue

        num1 = float(num1)# Convert input to float
        num2 = float(num2)

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))

if __name__ == "__main__":
    main()