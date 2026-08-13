#Crie um programa que peça ao usuário digitar três números com casas decimais.
# Calcule a média dos números e exiba o resultado com duas casas decimais.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

media = (num1 + num2 + num3) / 3
print(f"A média dos números digitados é: {media:.2f}")