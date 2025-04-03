tipo = input("Informe o tipo de combustivel: (e-etanal, g-gasolina)")
litros = float(input("Quantos litros: "))
vgaso = 5.80
vEtal = 4.90

if tipo == 'g':
    valor = vgaso*litros
else:
    valor = vEtal*litros

print(f"Você gastou R$ {valor: .2f}")




