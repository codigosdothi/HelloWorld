'''< Crie um programa que receba um número inteiro e o converta em um mês do ano.
Tenha Janeiro como o número 1 até Dezembro sendo o 12.
Imprima na tela "Mês Inexistente" se o número for maior que 12'''

mes = int(input ("Digite o número do mês correspondente, por favor"))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3: 
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Mês Inexistente")