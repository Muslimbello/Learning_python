bill_total = 110
discount_total = 10
if bill_total > 100:
    bill_total = bill_total - discount_total
    print("Your bill is greater than 100 so a discoungt has been applied to your bill")
    print("Your current bill is : ", bill_total)  # This will work
    # print("Your current bill is : " + str(bill_total)# Python cannot convert the int to a string implicitly so i have to do it explicit
