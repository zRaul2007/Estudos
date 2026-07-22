larg = int(input("Digite a largura do retângulo: "))
alt = int(input("Digite a altura do retângulo: "))
for i in range(alt):
    for j in range(larg):
        print("#", end="") # Imprime "#" sem pular linha. o parâmetro end="" define o que será impresso ao final
    print()