salario = float(input("Digite um salario para saber o aumento: "))

if salario >= 1400 and salario <= 2800:
    salario = salario * 1.15
    print("Aumento de salario de 15 porcento, valor total: %.1f" % salario)

elif salario > 2800:
    salario = salario * 1.08
    print("Aumento de salario de 8 porcento, valor total: %.1f" % salario)

else: 
    salario = salario * 1.2
    print("Aumento de salario de 20 porcento, valor total: %.1f" % salario)
