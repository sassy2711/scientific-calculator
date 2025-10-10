from calculator import *

def menu():
    while True:
        print("\nScientific Calculator")
        print("1. Square Root (√x)")
        print("2. Factorial (!x)")
        print("3. Natural Logarithm (ln x)")
        print("4. Power (x^b)")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            x = float(input("Enter x: "))
            print("Result:", square_root(x))
        elif choice == 2:
            x = float(input("Enter x: "))
            print("Result:", factorial(x))
        elif choice == 3:
            x = float(input("Enter x: "))
            print("Result:", natural_log(x))
        elif choice == 4:
            x = float(input("Enter base x: "))
            b = float(input("Enter power b: "))
            print("Result:", power(x, b))
        else:
            break

if __name__ == "__main__":
    menu()
