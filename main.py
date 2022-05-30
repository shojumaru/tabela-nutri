import functions


TOTAL = 0

if __name__ == "__main__":
    while True:
        food = input('insira a comida: ')
        food = functions.check_food(food)
        
        grams = input('insira as gramas: ')
        assert grams.isnumeric(), "Gramas deve ser numérico."
        grams = int(grams)
        
        calories = functions.calories(food, grams)
        TOTAL += calories
        
        print(f"Total calories: {TOTAL}")
        
        continue_ = input('deseja adicionar mais? (1-sim/2-nao)')
        if continue_ != "1":
            break