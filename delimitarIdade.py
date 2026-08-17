''' < Crie um programa que peça para o usuário digitar nome e idade.
Se a idade for maior ou igual a 18, imprimir seu nome e idade
Se a idade for menor que 18, imprimir que o usuário é menor de idade.'''

nome = str(input("Insira seu nome, por favor."))
idade = float (input("Insira sua idade, por favor."))

if idade >= 18:
    print( nome, "Você é maior de idade.")
else:
    print("Você é menor de idade.")