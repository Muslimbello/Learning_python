def scold(
    punishment,
):
    didJump = str(input("Who played ?:"))
    Arr = ["BILAL", "FARHAN", "HANEEF", "ABDULQADR", "ABDULMUIZ"]
    for i in Arr:
        if didJump == i:
            print(punishment + " " + didJump)


scold("slap")
