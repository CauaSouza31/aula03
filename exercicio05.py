nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua segunda nota: "))

media=(nota1 + nota2 + nota3)/3
if media >= 7:
    print(f"Aprovado {media}")
else:
        if media < 4:
            print(f"reprovado {media}")
        else:
            print(F"recuperação {media}")

