import random

with open("filing/pet.txt", "w") as file:
    petFile = file.writelines(["Harry\n", "john\n", "bingo"])

with open("filing/pet.txt", "r") as file:
    file_content = file.read()
    list_file_content = file_content.split("\n")

petName = random.choice(list_file_content)
print(list_file_content)
print(petName)
