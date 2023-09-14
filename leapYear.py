def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
        if year % 400 == 0:  # This line had incorrect indentation
            leap = True
    return leap


year = int(input())
print(is_leap(year))
