nome = input("Informe seu nome: ")
idade = int(input("infome sua idade: "))
salario = float(input("Informe seu salario: "))
percentual = float(input("Digite sua percentual: "))
valor_real = salario*(percentual/100)+ salario


print(f"Seu nome é {nome}, você tem {idade} anos, seu salario é {salario}, com seu aumento ficaria {valor_real
} ")
