
def top_3_food(foodlist):
    """
    top_3_food function should throw IndexError if a list of length < 3 is passed into the function.
    """

    print("Your top 3 favorite food is: ")
    for i in range(3):
        print(foodlist[i])


# top_3_food(["a", "b"])


def top_3_food_2(foodlist):
    print("Your top 3 favorite food is: ")
    for i in range(3):
        try:
            print(foodlist[i])
        except IndexError:
            raise Exception("Please enter at least 3 types of food.")
