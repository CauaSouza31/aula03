nome1 = input("Informe o nome do time: ")
golt1 = int(input("Informe a quantidade de gol: "))
nome2 = input("Infome o nome do outro time: ")
golt2 = int(input("Informe a quantidade de gol:"))

if golt1 > golt2:
    print(F"O time vencendor é {nome1}")
else:
    if golt1 == golt2:
        print("empate")
    else:
        print(F"O time vencendor é {nome2}")





