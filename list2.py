''' < Crie um programa que peça para o usuário continue informando números inteiros.
O programa deve armazenar os números e deve apenas para de capturar os números quando o usuário digitar 0
Ao final, o programa deve informar a quantidade de elementos adicionados na lista, bem como o menor e o maior elemento digitados (excluindo o zero)'''


numeros = []

while True: 
    try:
        num = int(input("digite um número (0 para sair): "))
        
        if num == 0:
            break 
        
        numeros.append(num)
        
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.")
    
    if len(numeros) > 0:
        quantidade = len(numeros)
        menor = min(numeros)
        maior = max(numeros)
            
    else:
        print ("\nNenhum número válido foi digitado antes de encerrar o programa.")
        
    print("n/ ---Resultados---")
    print(f"Quantidade de elementos digitados: {quantidade}")
    print(f"Menor elemento: {menor}")
    print(f"Maior elemento: {maior}")
    
