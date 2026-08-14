'''<Crie um programa que peça para que o usuário informe o valor de sua nota. 
Caso a nota seja maior ou igual a 7,0 imprima "Aprovado" na tela.
Mas simultaneamente, caso a nota seja maior ou igual a 4,0 imprima "Tem direito a exame.
E se menor que 4,0 imprima "Reprovado"">'''

nota = float(input("Informe sua nota: "))

if nota >= 7.0:
    print("Aprovado")
elif nota >= 4.0:
    print("Tem direito a exame.")
else: 
    print("Reprovado")
        