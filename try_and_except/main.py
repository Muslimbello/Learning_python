try:
    user = int(input("give a number\n"))
    print(user)
except ValueError as e:
    print(f":please make sure your input is an integer")
