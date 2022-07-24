# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3.
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

#criando as funções para cada operação:
def functionSoma(a, b):
    return a + b

def functionSub(a, b):
    return a - b

def functionMult(a, b):
    return a * b

def functionDiv(a, b):
    if b == 0:
        return "Não é possível dividir por zero!"
    else:
        return a / b

print("\n******************* Python Calculator *******************")

print("\nSelecione o número da operação desejada:")
#opções para o usuário
print("\n1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

#gravando a opção digitada pelo user na variável option
option = int(input("\nDigite sua opção (1/2/3/4): "))

while option > 0 and option < 5:
    #entrada dos valores para as operações matemáticas
    number1 = int(input("\nDigite o primeiro número: "))
    number2 = int(input("Digite o segundo número: "))

    if(option == 1):
        print(number1, " + ", number2, " = ", functionSoma(number1, number2))
    elif(option == 2):
        print(number1, " - ", number2, " = ", functionSub(number1, number2))
    elif(option == 3):
        print(number1, " * ", number2, " = ", functionMult(number1, number2))
    elif(option == 4):
        print(number1, " / ", number2, " = ", functionDiv(number1, number2))

    option = int(input("\nDigite sua opção (1/2/3/4): "))

else:
    print("Opção inválida!")