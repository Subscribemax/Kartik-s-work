while True:
    a = float(input('Enter your first number: '))
    b = float(input('Enter your second number: '))
    c = input('What do you want to do (add, subtract, divide, multiply)? ')

    if c == 'add':
        print("Result:", a + b)
    elif c == 'subtract':
        print("Result:", a - b)
    elif c == 'divide':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Cannot divide by zero.")
    elif c == 'multiply':
        print("Result:", a * b)
    else:
        print("Invalid operation.")

    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != 'yes':
        print("Thanks for using the calculator. Goodbye!")
        break
