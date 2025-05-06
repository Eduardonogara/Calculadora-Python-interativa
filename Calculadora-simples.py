"""
Calculadora em Python - Projeto Básico
Autor: Eduardo Nogara
Descrição: Permite realizar operações matemáticas básicas como soma, subtração,
multiplicação, divisão, potenciação e radiciação em modo interativo.
"""

# Função para somar dois números
def somar(a, b):
    return a + b

# Função para subtrair o segundo número do primeiro
def subtrair(a, b):
    return a - b

# Função para multiplicar dois números
def multiplicar(a, b):
    return a * b

# Função para dividir o primeiro número pelo segundo
def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

# Função para elevar o primeiro número à potência do segundo
def potenciar(a, b):
    return a ** b

# Função para calcular a raiz b-ésima de a
def radiciar(a, b):
    if b == 0:
        return "Erro: índice da raiz não pode ser zero"
    if a < 0 and b % 2 == 0:
        return "Erro: não se pode extrair raiz par de número negativo"
    return a ** (1 / b)

# Função principal que controla o menu e a execução da calculadora
def main():
    while True:
        # Limpa a tela com quebras de linha
        print("\n" * 100)
        print("=" * 30)
        print(" CALCULADORA PYTHON ".center(30, "-"))
        print("=" * 30)

        # Menu de opções
        print("\nSelecione a operação:")
        print("1 Somar")
        print("2 Subtrair")
        print("3 Multiplicar")
        print("4 Dividir")
        print("5 Potenciar")
        print("6 Radiciar")
        print("7 Sair")

        operacao = input("Escolha a operação (1/2/3/4/5/6/7): ")

        if operacao == '7':
            print("Encerrando calculadora. Até mais!")
            break

        # Entrada dos números com tratamento de erro
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Você deve digitar números válidos.")
            input("Pressione Enter para continuar...")
            continue

        # Escolha da operação
        if operacao == '1':
            print("Resultado:", somar(a, b))
        elif operacao == '2':
            print("Resultado:", subtrair(a, b))
        elif operacao == '3':
            print("Resultado:", multiplicar(a, b))
        elif operacao == '4':
            print("Resultado:", dividir(a, b))
        elif operacao == '5':
            print("Resultado:", potenciar(a, b))
        elif operacao == '6':
            print("Resultado:", radiciar(a, b))
        else:
            print("Operação inválida")

        input("Pressione Enter para retornar ao menu...")

# Execução do programa
if __name__ == '__main__':
    main()