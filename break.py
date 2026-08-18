'''< Crie um programa com um laço que intere por 10 vezes, imprimindo valores na tela.
Dentro do laço, adicione uma condição para que, caso estejamos na quinta interação, o comando break force o laço a interromper a sua excução por completo.>'''

for i in range(10):
    if i == 5:
        break
    print(i, "", end="")