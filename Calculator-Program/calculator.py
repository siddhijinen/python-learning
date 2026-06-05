logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    if n2 == 0:
        return "Error! Cannot divide by 0."
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

calculate_again = True
result = 0
num1 = float(input("Enter your first number: "))

while calculate_again:
    operation_chosen = input("\nChoose an operation: \n+\n-\n*\n/\n")
    if operation_chosen not in operations:
        print("Invalid operation! Please choose +, -, *, or /.")
        continue
    num2 = float(input("\nEnter your second number: "))

    result = operations[operation_chosen](num1, num2)
    if result == "Error! Cannot divide by 0.":
        print(result)
        print("Starting afresh...")
        num1 = float(input("Enter your first number: "))
        continue

    print(f"Result: {result}")  

    user_continues = input("Do you want to continue working with previous result? Type 'y' to continue and 'n' to start afresh (X for exit): ").lower()
    if user_continues == "y":
        num1 = result
    elif user_continues == "n":
        num1 = float(input("Enter your first number: "))
    elif user_continues == "x":
        calculate_again = False
        print("Ending Program.")
    else:
        print("Invalid input. Resetting.")
        num1 = float(input("Enter your first number: "))
