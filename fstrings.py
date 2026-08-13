## Declare quatro variáveis: id do tipo inteiro, nome do tipo string, salário do tipo float e brasileiro do tipo bool.
## Peça que o usuário registre os dados acima. 
## Imprima na tela usando f-strings.

id = int(input("Digite o ID (número inteiro): "))
nome = input("Digite o nome: ")
salario = float(input("Digite o salário (número decimal): "))
brasileiro_input = input("Você é brasileiro? (s/n): ").strip().lower()
brasileiro = True if brasileiro_input == 's' else False

print(f"ID: {id}")
print(f"Nome: {nome}")
print(f"Salário: {salario}")
print(f"Brasileiro: {brasileiro}")