print("Welcome to the Love calculator")
# name_1 = str(input("What is your name?\n "))
# name_2 = str(input("What is your name?\n "))
name_1 = "arianna rebolini"
name_2 = " channing tatum"
frmt_name1 = name_1.lower()
frmt_name2 = name_2.lower()
true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]
list_1 = list(frmt_name1)
list_2 = list(frmt_name2)
concat_list_name = list_1 + list_2
for i in true:
    true_count = concat_list_name.count(i)
