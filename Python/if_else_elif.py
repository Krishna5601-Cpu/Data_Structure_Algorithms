"""
Python Conditional Statements
Covers: if, elif, else, Nested if, Ternary Operator, Match-Case, and Guards
"""

def main():
    print("1. Basic IF-ELIF-ELSE")
    score = 85

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score} -> Grade: {grade}\n")

    print("2. NESTED IF STATEMENTS")
    age = 20
    has_license = True

    if age >= 18:
        if has_license:
            print("Status: Eligible to drive independently.")
        else:
            print("Status: Age-eligible, but missing a valid license.")
    else:
        print("Status: Underage for driving.")
    print()

    print("3. TERNARY OPERATOR")
    user_age = 20

    # Syntax: value_if_true if condition else value_if_false
    status = "Adult" if user_age >= 18 else "Minor"
    
    # Inline usage inside print/formatting
    print(f"User is an {status} (Access: {'Granted' if status == 'Adult' else 'Denied'}).\n")

    print("4. MATCH-CASE (Python 3.10+)")
    
    # Example A: Value and OR (|) matching
    day = "Monday"
    match day:
        case "Monday" | "Friday":
            print(f"{day}: Transition day between work and weekend!")
        case "Tuesday" | "Wednesday" | "Thursday":
            print(f"{day}: Core work week.")
        case "Saturday" | "Sunday":
            print(f"{day}: Weekend!")
        case _:
            print(f"{day}: Invalid day entry.")

    # Example B: Pattern Matching with Guards (case + if)
    number = -12
    match number:
        case n if n > 0 and n % 2 == 0:
            print(f"Number {n} is positive and EVEN.")
        case n if n > 0 and n % 2 != 0:
            print(f"Number {n} is positive and ODD.")
        case n if n < 0:
            print(f"Number {n} is NEGATIVE.")
        case _:
            print("Number is ZERO.")


if __name__ == "__main__":
    main()