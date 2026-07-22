# 1 - Usuário digita números até digitar "fim"
# 2 - Armazena os números em uma lista
# 3 - Soma os elementos da lista
# 4 - Imprime a soma dos elementos

def soma_elementos(lista):
    soma = 0 
    for item in lista:
        soma = soma + item
    return soma

fim = False
lista = []
entrada = 0
while not fim:
    entrada = input("Digite um número ou 'fim' para encerrar: ").lower()
    if entrada == "fim":
        fim = True
        print(soma_elementos(lista))
    else:
        lista.append(int(entrada))