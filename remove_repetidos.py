# 1 - Usuário digita números até digitar "fim"
# 2 - Armazena os números em uma lista
# 3 - Remove os números repetidos da lista
# 4 - Reordena e imprime a lista sem números repetidos

def remove_repetidos(lista_inicial):
    lista_final = []
    for item in lista_inicial:
        if item not in lista_final:
            lista_final.append(item)
    lista_final.sort()
    return lista_final

fim = False
lista_inicial = []
entrada = 0
while not fim:
    entrada = input("Digite um número ou 'fim' para encerrar: ").lower()
    if entrada == "fim":
        fim = True
        print(remove_repetidos(lista_inicial))
    else:
        lista_inicial.append(int(entrada))