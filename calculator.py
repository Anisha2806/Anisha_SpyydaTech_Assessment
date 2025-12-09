history = []

def add(a, b):
    result = a + b
    history.append(f"added {a} to {b} got {result}")
    return result

def subtract(a, b):
    result = a - b
    history.append(f"subtracted {b} from {a} got {result}")
    return result

def multiply(a, b):
    result = a * b
    history.append(f"multiplied {a} with {b} got {result}")
    return result

def divide(a, b):
    if b == 0:
        history.append("division by zero error")
        return "error division by zero"
    result = a / b
    history.append(f"divided {a} by {b} got {result}")
    return result

def get_history():
    return history

while True:
    print("\n1 addition")
    print("2 subtraction")
    print("3 multiplication")
    print("4 division")
    print("5 view history")
    print("6 exit")

    choice = input("enter your choice: ")

    if choice in ["1", "2", "3", "4"]:
        a, b = input("enter two numbers separated by space: ").split()
        a = int(a)
        b = int(b)

        if choice == "1":
            print(add(a, b))
        elif choice == "2":
            print(subtract(a, b))
        elif choice == "3":
            print(multiply(a, b))
        elif choice == "4":
            print(divide(a, b))

    elif choice == "5":
        print("\ncalculation history:")
        if not history:
            print("no calculations yet")
        else:
            for record in get_history():
                print(record)

    elif choice == "6":
        print("bye")
        break

    else:
        print("invalid choice")
