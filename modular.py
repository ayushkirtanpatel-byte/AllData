import time
import random
import uuid
import math
from datetime import datetime

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("enter 1 to. Display current date and time")
        print("enter 2 to. Countdown Timer")
        print("enter 3 to exit :")
        

        choice = input("Enter your choice: ")

        if choice == "1":
            now = datetime.now()
            print("Current Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "2":
            sec = int(input("Enter seconds: "))
            while sec > 0:
                print(sec)
                time.sleep(1)
                sec -= 1
            print("Time's Up!")

        elif choice == "3":
            break
        else:
            print("Invalid choice!")


def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("enter 1 to. Factorial")
        print("enter 2 to. Compound Interest")
        print("enter 3 to exit :")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter number: "))
            print("Factorial:", math.factorial(n))

        elif choice == "2":
            p = float(input("Principal: "))
            r = float(input("Rate (%): "))
            t = float(input("Time (years): "))
            ci = p * (1 + r/100)**t
            print("Compound Interest:", round(ci, 2))

        elif choice == "3":
            break
        else:
            print("Invalid choice!")


def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("enter 1 to. Random Number")
        print("enter 2 to. Random Password")
        print("enter 3 to exit :")
        

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Random Number:", random.randint(1, 100))

        elif choice == "2":
            length = int(input("Password length: "))
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%&*"
            pwd = "".join(random.choice(chars) for _ in range(length))
            print("Generated Password:", pwd)

        elif choice == "3":
            break
        else:
            print("Invalid choice!")


def uuid_menu():
    print("\nGenerated UUID:", uuid.uuid4())


def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Filename: ")
            open(name, "w").close()
            print("File created.")

        elif choice == "2":
            name = input("Filename: ")
            text = input("Enter text: ")
            with open(name, "w") as f:
                f.write(text)
            print("Written.")

        elif choice == "3":
            name = input("Filename: ")
            with open(name, "r") as f:
                print("\nFile Content:\n", f.read())

        elif choice == "4":
            name = input("Filename: ")
            text = input("Enter text: ")
            with open(name, "a") as f:
                f.write("\n" + text)
            print("Appended.")

        elif choice == "5":
            break
        else:
            print("Invalid choice!")


def explore_module():
    name = input("Enter module name: ")
    try:
        module = __import__(name)
        print(dir(module))
    except:
        print("Module not found!")



while True:
    print("\n===============================")
    print("Welcome to Multi-Utility Toolkit 👏")
    print("===============================")
    print("\n1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate UUID")
    print("5. File Operations")
    print("6. Explore Module (dir())")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        datetime_menu()
    elif choice == "2":
        math_menu()
    elif choice == "3":
        random_menu()
    elif choice == "4":
        uuid_menu()
    elif choice == "5":
        file_menu()
    elif choice == "6":
        explore_module()
    elif choice == "7":
        print("Thank you for using the Toolkit!")
        break
    else:
        print("Invalid choice!")
