def  soma():
   num1 = int(input("Digite um numero: ")) 
   num2 = int(input("Digite outro numero: "))
   result = num1 + num2 
   print(result)


def  sub():
    num1 = int(input("Digite um numero: ")) 
    num2 = int(input("Digite outro numero: "))
    result = num1 - num2 
    print(result)

def  mult():
    num1 = int(input("Digite um numero: ")) 
    num2 = int(input("Digite outro numero: ")) 
    result = num1 * num2
    print(result)


def  divi():
    num1 = int(input("Digite um numero: ")) 
    num2 = int(input("Digite outro numero: "))
    result = num1/num2
    print(result)


conta = int(input("Digite de 1 para soma, 2 para subtracao, 3 para multiplicacao, 4 para divisao: "))

match conta:
    case 1: 
       soma()
    case 2:
       sub()
    case 3:
       mult()
    case 4:
       divi()
    case _:
       print("Numero invalido")
     