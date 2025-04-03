tipo = input("Informe o tipo de combustivel: (e-etanal, g-gasolina)")
litros = float(input("Quantos litros: "))
vgaso = 5.80
vEtal = 4.90
valor = 0
if tipo == 'G'or tipo =='g':
    valor = vgaso*litros
else:
   if tipo == 'E'or tipo =='e':
       valor = vEtal * litros
   else:
       print("Tipo de combustivel invalido")

print(f'Você gastou R$ {valor: .2f}')




