dia = int(input("Digite de 1 a 7 para saber qual corresponde ao nome dos dias: "))

match dia:
    case 1: 
        print("Domingo")
    case 2:
        print("Segundo")
    case 3: 
        print("Terca")
    case 4:
        print("Quarta")
    case 5: 
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sabado")
    case _:
        print("Dia invalido")
