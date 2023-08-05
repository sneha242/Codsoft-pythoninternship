import math

def calculator():
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    elif choice == '5':
        num = float(input("Enter the number: "))
        if num >= 0:
            result = math.sqrt(num)
        else:
            print("Error: Cannot calculate the square root of a negative number.")
            return
    else:
        print("Invalid choice. Please try again.")
        return

    print("Result:", result)

if __name__ == "__main__":
    calculator()
