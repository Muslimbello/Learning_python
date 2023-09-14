def cal(a, b):
    total = a / b
    return total


try:
    output = cal(4, 0)
except Exception as e:
    print(e, "You can't devide by zero")
