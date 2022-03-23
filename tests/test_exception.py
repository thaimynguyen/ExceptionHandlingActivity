import pytest

from activity.main import *


def test_raises_exception_with_less_than_3_food():
    # arrange
    foodlist = ["ramen", "kimchi"]

    # act & assert
    with pytest.raises(IndexError):
        top_3_food(foodlist)
