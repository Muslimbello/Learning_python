class Recipe:
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def counter(self):
        print(
            "The "
            + str(self.dish)
            + " contains "
            + str(self.items)
            + " and will take "
            + str(self.time)
            + " mins to cook."
        )


Pizza = Recipe("Pizza", ["tomato", "flour", "sugar"], "20")
print(Pizza.dish)
Pizza.counter()
