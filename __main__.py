import functions

total = 0
while True:
    food = functions.check_food()
    grams = functions.check_grams()
    calories = functions.calories(food, grams)
    total += calories
    print("Total: {}" .format(total))
    while True:
        try:
            conditional = int(input("Deseja continuar?\n1- Sim\n2- Não\n"))
        except ValueError:
            print("Você deve digitar 1 ou 2.")
            continue
        else:
            break
    if conditional == 2:
        break