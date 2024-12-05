# calculadora avançada
import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def potencia(base, expoente):
    return base ** expoente

def raiz(numero):
    if numero < 0:
        return "Erro: Raiz de número negativo!"
    return math.sqrt(numero)

def trigonometria(angulo, func):
    angulo = math.radians(angulo)  # Converte para radianos
    if func == "seno":
        return math.sin(angulo)
    elif func == "cosseno":
        return math.cos(angulo)
    elif func == "tangente":
        return math.tan(angulo)
    else:
        return "Função desconhecida!"

def menu():
    print("\n--- Calculadora Avançada ---")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Funções Trigonométricas")
    print("8. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {soma(a, b)}")
        elif opcao == "2":
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {subtracao(a, b)}")
        elif opcao == "3":
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {multiplicacao(a, b)}")
        elif opcao == "4":
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {divisao(a, b)}")
        elif opcao == "5":
            base = float(input("Digite a base: "))
            expoente = float(input("Digite o expoente: "))
            print(f"Resultado: {potencia(base, expoente)}")
        elif opcao == "6":
            numero = float(input("Digite o número: "))
            print(f"Resultado: {raiz(numero)}")
        elif opcao == "7":
            angulo = float(input("Digite o ângulo (em graus): "))
            func = input("Escolha a função (seno, cosseno, tangente): ").lower()
            print(f"Resultado: {trigonometria(angulo, func)}")
        elif opcao == "8":
            print("Saindo... Obrigado por usar a Calculadora Avançada!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
