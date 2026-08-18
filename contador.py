'''< Crie um programa que mostre na tela, um contador. O contador deve ser inicializado com zero.
O usuário deve ter a opção de incrementar uma unidade ao contador, ou de encerrar o programa.
Enquanto o usuário continuar decidindo incrementar o contador, o programa não deve ser encerrado.
O programa deve encerrar quano o usuário decidir encerrar.
Utilize um laço com os comandos: continue e break.>'''

contador = 0
print("Contador inicializado em:", contador)

while True:
    print("\nEscolha uma opção:")
    print("1 - Incrementar contador")
    print("2 - Encerrar programa")
    
    escolha = input("Digite sua escolha (1 ou 2): ")
    
    if escolha == '1':
        contador += 1
        print("Contador incrementado! Novo valor:", contador)
        continue
    elif escolha == '2':
        print("Encerrando o programa. Valor final do contador:", contador)
        break
    else:
        print("Opção inválida. Tente novamente.")


