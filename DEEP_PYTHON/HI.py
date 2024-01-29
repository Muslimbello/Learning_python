print("Multiple checker")

while True:
    try:
        First = int(input("Enter Your First number "))
        Second = int(input("Enter Your Second number "))
    except ValueError:
        print("Your input must be an integer try again")

    else:

        def id_multiple(a, b):
            if a % b == 0:
                print(f"{True},{a} is a multiple of {b}")
            else:
                print(f"{False}, {a} is not a multiple of {b}")

        id_multiple(First, Second)
        break
