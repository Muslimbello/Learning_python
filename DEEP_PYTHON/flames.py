def is_multiple():
    print("This program determines if a number is a multiple of another number.\n\n")

    number = input("Enter a valid whole integer for number: ")
    if number.lstrip("-").isnumeric() == True:
        number = int(number)
        if number == 0:
            is_multiple()
            return
    else:
        is_multiple()
        return

    factor = input("Enter a valid whole integer for factor: ")
    if factor.lstrip("-").isnumeric() == True:
        factor = int(factor)
        if factor == 0:
            is_multiple()
            return
    else:
        is_multiple()
        return

    print("\nchecking...\n")

    if number % factor == 0:
        print(f"{number} is a multiple of {factor}.\n")
    else:
        print(f"{number} is not a multiple of {factor}.\n")
    print(number % factor == 0)


is_multiple()
