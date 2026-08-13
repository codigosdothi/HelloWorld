# Crie um programa que peça para o usuário informe dois números
# Calcule: soma, subtração, multiplicação e a divisão entre o primeiro e o segundo número
# Imprima os resultados encontrados na tela.

number1 = float(input("Informe o primeiro número: "))
number2 = float(input("Informe o segundo número: "))

soma = number1 + number2
subtracao = number1 - number2
multiplicacao = number1 * number2
divisao = number1 / number2

print("Resultados: ")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
