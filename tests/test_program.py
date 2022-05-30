import pytest
import functions

def test_check_foods_should_return_calories():
    food = 'beterraba'
    assert isinstance(functions.check_food(food), int)
    assert functions.check_food(food) == 43
    
    
def test_calories():
    food = 'beterraba'
    grams = 100
    
    food = functions.check_food(food)
    assert isinstance(functions.calories(food, grams), float)
    assert functions.calories(food, grams) == 43