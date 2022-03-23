import pytest

from activity.main import *


def test_raises_exception_with_less_than_3_food():
    # arrange
    foodlist = ["ramen", "kimchi"]

    # act & assert
    with pytest.raises(IndexError):
        top_3_food(foodlist)


def test_top_3_food_2_raises_exception():
    # arrange
    foodlist = ["ramen", "kimchi"]

    # act & assert
    with pytest.raises(Exception, match="Please enter at least 3 types of food."):
        top_3_food_2(foodlist)
