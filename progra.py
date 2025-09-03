dinheiro = float (input("quanto voce ganha por hora:"))
horas = float (input("quantas horas voce trabalha por mes:"))

salario_bruto = dinheiro * horas 
print (f"salaio bruto:R${salario_bruto}")

imposto = salario_bruto * 0.11
print (f"imposto:R${imposto}")

inss = salario_bruto * 0.08
print (f"inss:R${inss}")

sindicato = salario_bruto * 0.05
print (f"sindicato:R${sindicato}")

salario_liquido = salario_bruto - imposto - inss - sindicato
print (f"salario_liquido:R${salario_liquido}")
