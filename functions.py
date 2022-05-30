import Table

def calories(food: int, grams: int) -> float:
    return (grams / 100) * food


def check_food(food: str) -> str:
    # needs while loop outside
    assert food in Table.alimentos.keys(), "Comida inválida, tente novamente"
    return Table.alimentos[food]