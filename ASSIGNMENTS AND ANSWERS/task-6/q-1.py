try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    result = numerator / denominator

    print(f"Result: {numerator} / {denominator} = {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integer values for the numerator and denominator.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
