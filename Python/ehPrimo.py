n = int(input("Digite um número inteiro positivo: "))
def eh_primo(n):
    div = 0
    for x in range (1, n + 1):
        if n % x == 0:
            div = div + 1
    return div

while n > 0:
    if n <= 1:
        print("Número inválido")
    else: 
        if eh_primo(n) == 2:
            print(f"{n} é um número primo.")
        else:
            print(f"{n} NÃO é um número primo.")
    n = int(input("Digite um número inteiro positivo: "))
