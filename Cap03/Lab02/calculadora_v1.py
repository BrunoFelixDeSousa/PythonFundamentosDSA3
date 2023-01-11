# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

def menu():
    print("\nSelecione o número da operação desejada: \n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Fechar Programa")

def choice():
    escolha = input("\nDigite sua opção (1/2/3/4/5): ")

    while escolha != '5':
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))

        if escolha == '1':
            print("\n")
            print(num1, "+", num2, "=", add(num1, num2))
            print("\n")

        elif escolha == '2':
            print("\n")
            print(num1, "-", num2, "=", subtract(num1, num2))
            print("\n")

        elif escolha == '3':
            print("\n")
            print(num1, "*", num2, "=", multiply(num1, num2))
            print("\n")

        elif escolha == '4':
            print("\n")
            print(num1, "/", num2, "=", divide(num1, num2))
            print("\n")

        else:
            print("\nOpção Inválida!")


if __name__ == '__main__':
    menu()
    choice()