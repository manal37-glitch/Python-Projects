import math 

def print_menu():
    """Displays the available operations.""" 
    print("\nAvailable operations:") 
    print("1. Add (+)") 
    print("2. Subtract (-)") 
    print("3. Multiply (*)") 
    print("4. Divide (/)") 
    print("5. Sine (sin)") 
    print("6. Cosine (cos)") 
    print("7. Tangent (tan)") 
    print("0. Exit") 

def get_input(prompt): 
    """Safely gets a float input from the user.""" 
    while True:
        try: 
            user_input = input(prompt).strip()  # Strip whitespace
            return float(user_input)
        except ValueError: 
            print("Invalid input. Please enter a numeric value.")

def add(a, b): 
    return a + b 

def subtract(a, b): 
    return a - b 

def multiply(a, b): 
    return a * b 

def divide(a, b): 
    if b != 0: 
        return a / b 
    else: 
        print("Error: Division by zero is not allowed.") 
        return None 

def sine(angle): 
    return math.sin(math.radians(angle)) 

def cosine(angle): 
    return math.cos(math.radians(angle)) 

def tangent(angle): 
    return math.tan(math.radians(angle)) 

def main(): 
    while True: 
        print_menu() 
        
        # Validate the choice input
        choice = input("Enter your choice (0-7): ").strip()
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 0 and 7.")
            continue
        
        choice = int(choice)
        
        # Handle the exit condition
        if choice == 0: 
            print("Exiting the calculator. Thank you!") 
            break 
        
        # Handle arithmetic operations
        elif choice in [1, 2, 3, 4]: 
            num1 = get_input("Enter the first number: ") 
            num2 = get_input("Enter the second number: ") 
            
            if choice == 1: 
                print("Result:", add(num1, num2)) 
            elif choice == 2: 
                print("Result:", subtract(num1, num2))  # Fixed function call
            elif choice == 3: 
                print("Result:", multiply(num1, num2)) 
            elif choice == 4: 
                result = divide(num1, num2)
                if result is not None: 
                    print("Result:", result)
        
        # Handle trigonometric operations
        elif choice in [5, 6, 7]: 
            angle = get_input("Enter the angle in degrees: ") 
            
            if choice == 5: 
                print("Sine of", angle, "is:", sine(angle)) 
            elif choice == 6: 
                print("Cosine of", angle, "is:", cosine(angle)) 
            elif choice == 7: 
                print("Tangent of", angle, "is:", tangent(angle)) 
        
        # Handle invalid choices
        else: 
            print("Invalid choice. Please choose a valid operation.") 

if __name__ == "__main__": 
    main()
