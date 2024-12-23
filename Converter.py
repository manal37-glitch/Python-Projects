# Creating a conversion programme.
# Start with the functions
# 1. Currency conversion

def convert_currency():
    print("\nWhich conversion would you like to choose: ")
    print("1. Dollars to Ghana Cedis")
    print("2. Ghana Cedis to Dollars")
    print("3. Pounds to Dollars")
    print("4. Dollars to Pounds")
    choice= int(input("Enter your choice: "))
    if choice==1:
        value= float(input("Enter the amount in Dollars: "))
        print(f"{value} dollars will be {value*14.72} cedis ")
    elif choice==2:
        value= float(input("Enter the amount in Ghana Cedis: "))
        print(f"{value} cedis will be {value*0.068} cedis")
    elif choice==3:
        value= float(input("Enter the amount in Pounds: "))
        print(f"{value} pounds will be {value*1.25} dollars")
    elif choice==4:
        value= float(input("Enter the amount in Dollars: "))
        print(f"{value} dollars will be {value/1.25} pounds")
    

# convert_currency()

    # 2. Length conversion
def convert_length():
    print("\nWhich conversion would you like to choose: ")
    print("1. Centimeters to feet and inches")
    print("2. Feet and inches to centimeters")
    choice= int(input("Enter your choice: "))
    if choice==1:
        value=float(input("Enter the length in centimeters: "))
        inches= value/2.54
        feet=inches/12
        print(f"{value} cm will be {feet} feet and {inches} inch")
    elif choice==2:
        feet=float(input("Enter the length in feet: "))
        inches=float(input("Enter the length in inches: "))
        length=round((feet*12 + inches)/2.54,2)
        print(f"{feet} ft and {inches} in will be {length} cm")
# convert_length()


# 3. Temperature conversion

def convert_temp():
    print("\nWhich conversion would you like to choose: ")
    print("1. Degree Celsius to Fahrenheit")
    print("2. Fahrenheit to celsius")
    choice=int(input("Enter your choice: "))
    if choice==1:
        temp=float(input("Enter the tempersture in degree celsius: "))
        print(f"{temp} degree celsius is {(temp*9/5)+32} fahrenheit")
    elif choice==2:
        temp=float(input("Enter the tempersture in Fahrenheit: "))
        print(f"{temp} fahrenheit is {(temp-32)*5/9} degree celsius")
    else:
        print("Invalid input!Try again.\n")
# convert_temp()
    
print("===== Welcome to Value Converter =====")
while 1:
    print("Which option would you like to choose:-")
    print("1. Convert currency")
    print("2. Convert lengths")
    print("3. Convert temperature")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        convert_currency()
    elif choice == 2:
        convert_length()
    elif choice == 3:
        convert_temp()
    elif choice == 4:
        print('Exiting...')
        exit(0)
    

    