import Table

def calories(food, grams):
    result = (grams / 100) * food
    return result

def check_food():
    while True:
        try:
            food = input("Digite o nome da comida: ")
            food = Table.alimentos[food]
        except KeyError:
            print("Comida inválida, tente novamente.")
            continue
        else:
            break
    return food

def check_grams():
    while True:
        try:
            grams = int(input("Quantas gramas você comeu?\nGramas: "))
        except ValueError:
            print("Número inválido. Digite apenas números inteiros.")
            print("Tente novamente.")
            continue
        else:
            break
    return grams