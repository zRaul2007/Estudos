larg = int(input("Digite a largura do retângulo: "))
alt = int(input("Digite a altura do retângulo: "))
for i in range(alt):
    for j in range(larg):
        if i == 0 or i == alt - 1:
            print("#", end="") # Imprime "#" sem pular linha. o parâmetro end="" define o que será impresso ao final
        else:
            if j == 0 or j == larg - 1:
                print("#", end="")
            else:
                print(" ", end="")
    print()
