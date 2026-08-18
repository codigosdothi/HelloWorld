'''< Crie um programa que itere por 10 vezes imprimindo os valores na tela.
Dentro do laço adicione uma condição para que, caso estejamos na 5ª iteração, o comando "Continue" force o laço a interromper a iteração atual e pula para a próxima.>'''

for i in range(10):
    if i == 5:
        continue
    print(i, "", end="")
