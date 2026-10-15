import math
import operator
from functools import reduce

OPERATIONS = {1: (operator.add, "+"), 2: (operator.sub, "-"), 3: (operator.mul, "*"), 4: (operator.truediv, "/")}

def read_number(prompt):
    try:
        value = float(input(prompt))
    except ValueError:
        return None
    if not math.isfinite(value):
        return None
    return int(value) if value.is_integer() else value

def clean(result):
    if isinstance(result, float):
        result = round(result, 10)
        if result.is_integer():
            result = int(result)
    return result

def calculate(choice):
    operation, symbol = OPERATIONS[choice]
    count = read_number("How many numbers do you want to use? ")
    if not isinstance(count, int) or count < 2:
        print("Please enter a whole number of at least 2")
        return

    numbers = []
    for i in range(1, count + 1):
        number = read_number(f"Enter number {i}: ")
        if number is None:
            print("Invalid number, please try again")
            return
        numbers.append(number)

    try:
        result = reduce(operation, numbers)
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return
    print(f" {symbol} ".join(map(str, numbers)) + f" = {clean(result)}")

def exponential():
    base = read_number("Enter the base number: ")
    power = read_number("Enter the exponent (power): ")
    if base is None or power is None or abs(power) > 100:
        print("Invalid input (exponent must be between -100 and 100)")
        return

    try:
        result = base ** power
    except (ZeroDivisionError, OverflowError):
        print("Cannot calculate this power")
        return
    if isinstance(result, complex):
        print("Result is not a real number")
    else:
        print(f"{base} ** {power} = {clean(result)}")

def expression_calculator():
    text = input("Enter an expression (e.g. 2 + 3 * 4 - (6 / 2)): ").strip()
    if not text or len(text) > 50 or "**" in text or any(ch not in "0123456789+-*/(). " for ch in text):
        print("Invalid expression")
        return

    try:
        print(f"{text} = {clean(eval(text))}")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception:
        print("Invalid expression")

def main():
    print("Simple Python Calculator!")
    print("=" * 20)

    while True:
        choice = read_number(
            "1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exponential\n6. Expression (BODMAS)\n7. Exit\nEnter your choice: "
        )

        match choice:
            case 1 | 2 | 3 | 4:
                calculate(choice)
            case 5:
                exponential()
            case 6:
                expression_calculator()
            case 7:
                print("Thank you for using Simple Python Calculator!")
                break
            case _:
                print("Invalid choice, please enter 1-7")

if __name__ == "__main__":
    main()