"""
List
# Ask for user input
# Enter 3 favorite food
# If user enters less than 3 food 
    # raise IndexError
    # print error message "Please input exactly 3 types of food" 
# If user enters more than 3 food
    # print error message "Please input exactly 3 types of food"
"""


def top_3_food(foodlist):

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
            raise IndexError("Please enter at least 3 types of food.")
