'''<Crie um programa que peça para o usuário digitar um número de 1 a 7.
a cada numéro digitado imprima um dia da semana, de acordo com: 
1 - Domingo, 2- Segunda, 3- Terça, 4- Quarta, 5- Quinta, 6- Sexta, 7, Sábado.
Números maiores que 7, imprima a mensagem "Número invalido>'''


diadaSemana = int(input("Digite um numero de 1 a 7: "))

if diadaSemana == 1:
    print("Domingo")
elif diadaSemana == 2:
    print("Segunda")
elif diadaSemana == 3:
    print("Terça")
elif diadaSemana == 4:
    print("Quarta")
elif diadaSemana == 5:
    print("Quinta")
elif diadaSemana == 6:
    print("Sexta")
elif diadaSemana == 7:
    print("Sábado")
else:
    print("Você digitou um número inválido")