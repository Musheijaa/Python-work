while True:
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        result = first_number / second_number
    except ValueError:
        print("Please enter numbers only. Try again.\n")
    except ZeroDivisionError:
        print("You cannot divide by zero. Please enter a non-zero second number.\n")
    else:
        print(f"\nThe result of {first_number} divided by {second_number} is: {result}")
        break
