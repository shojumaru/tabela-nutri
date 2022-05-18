def calorias(comida, gramas):
    resultado = (gramas / 100) * comida
    return resultado

alimentos = {
'beterraba': 43,
'banana': 98,
'batata inglesa': 77,
'batata doce': 86,
'cenoura': 34,
'ervilha': 81,
'maca': 52,
'milho': 96,
'leite': 42,
'arroz': 130,
'macarrao': 371,
'carne': 143,
'linguiça': 154,
'pao': 265,
'pao minuto': 110,
'frango': 165,
'maionese': 692,
'ovo': 155,
'queijo mussarela': 280,
'mortadela': 247,
'mortadela fatia': 36,
'queijo fatia': 100
}

total = 0
print("Calculadora de Calorias")
cond = int(input("Para calcular as calorias da sua refeição, digite 1: "))

while cond == 1:
    escolha1 = input("Digite o nome da comida: ")
    comida = alimentos[escolha1]
    gramas = int(input("Digite a quantidade de gramas (somente números): "))
    total += calorias(comida, gramas)
    cond = int(input("Digite 1 para continuar ou 0 para parar."))

print("Total de calorias: {} kcal." .format(total))