conta = int(input("Digite de 1 para soma, 2 para subtracao, 3 para multiplicacao, 4 para divisao: "))

match conta:
    case 1: 
       num1 = int(input("Digite um numero: ")) 
       num2 = int(input("Digite outro numero: "))
       result = num1 + num2 
       print(result)
    case 2:
       num1 = int(input("Digite um numero: ")) 
       num2 = int(input("Digite outro numero: "))
       result = num1 - num2 
       print(result)
    case 3:
       num1 = int(input("Digite um numero: ")) 
       num2 = int(input("Digite outro numero: ")) 
       result = num1 * num2
       print(result)
    case 4:
       num1 = int(input("Digite um numero: ")) 
       num2 = int(input("Digite outro numero: "))
       result = num1/num2
       print(result)
    case _:
       print("Numero invalido")
     