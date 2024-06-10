def partida():
  youwin = 0
  cpwin = 0
  print("Você escolheu uma partida isolada!")
  print()
  n = int(input(("Quantas peças? ")))
  m = int(input(("Limite de peças por jogada? ")))

  if m+1 == n:
    print("Você começa!")
    youwin, cpwin = usuario_escolhe_jogada(n, m, youwin, cpwin)
  else:
    print("Computador começa!")
    youwin, cpwin = computador_escolhe_jogada(n, m, youwin, cpwin)

  print("===== FINAL DA PARTIDA =====")
  print()
  print("Placar: Você", youwin,"X",cpwin, "Computador")

def campeonato():
  print("Você escolheu um campeonato")
  print()
  print("===== RODADA 1 =====")
  print()
  n = int(input(("Quantas peças? ")))
  m = int(input(("Limite de peças por jogada? ")))
  youwin = 0
  cpwin = 0
  if m+1 == n:
    print("Você começa!")
    youwin, cpwin = usuario_escolhe_jogada(n, m, youwin, cpwin)
  else:
    print("Computador começa!")
    youwin, cpwin = computador_escolhe_jogada(n, m, youwin, cpwin)
  print()
  print("===== RODADA 2 =====")
  print()
  n = int(input(("Quantas peças? ")))
  m = int(input(("Limite de peças por jogada? ")))
  if m+1 == n:
    print("Você começa!")
    youwin, cpwin = usuario_escolhe_jogada(n, m, youwin, cpwin)
  else:
    print("Computador começa!")
    youwin, cpwin = computador_escolhe_jogada(n, m, youwin, cpwin)
  print()
  print("===== RODADA 3 =====")
  print()
  n = int(input(("Quantas peças? ")))
  m = int(input(("Limite de peças por jogada? ")))
  if m+1 == n:
    print("Você começa!")
    youwin, cpwin = usuario_escolhe_jogada(n, m, youwin, cpwin)
  else:
    print("Computador começa!")
    youwin, cpwin = computador_escolhe_jogada(n, m, youwin, cpwin)
  print("===== FINAL DO CAMPEONATO =====")
  print()
  print("Placar: Você", youwin,"X",cpwin, "Computador")

def computador_escolhe_jogada(n, m, youwin, cpwin):
  if m == 1:
    print("O computador tirou uma peça.")
  else:
    if m>n:
      m=n
      print("O computador tirou",m, "peças.")
    else:
      print("O computador tirou",m,"peças.")
  n = n-m
  if n == 0:
    print("Fim do jogo! O computador ganhou!")
    cpwin = cpwin + 1
  else:
    print("Agora restam ",n," peças no tabuleiro.")
    print()
    youwin, cpwin = usuario_escolhe_jogada(n, m, youwin, cpwin)
  return youwin, cpwin

def usuario_escolhe_jogada(n, m, youwin, cpwin):
  print()
  jogadaValida = False
  while not jogadaValida:
    pergunta = int(input("Quantas peças você vai tirar? "))
    if pergunta > m or pergunta <=0:
      print()
      print("Oops! Jogada inválida! Tente de novo.")
      print()
    else:
      jogadaValida = True
  if pergunta == 1:
    print()
    print("Você tirou uma peça.")
  else:
    print("Você tirou ",pergunta, " peças.")
  n = n-pergunta
  if n == 0:
    print("Fim do jogo! Você ganhou!")
    youwin = youwin + 1
  else:
    print("Agora restam ",n," peças no tabuleiro.")
    print()
    youwin, cpwin = computador_escolhe_jogada(n, m, youwin, cpwin)
  return youwin, cpwin


def nim():
  print("Bem-vindo ao jogo do NIM! Escolha: ")
  print()
  print("1 - para jogar uma partida isolada")
  print("2 - para jogar um campeonato")
  print()
  escolha = int(input())
  if escolha == 1:
    partida()
  elif escolha == 2:
    campeonato()
  else:
    print("Escolha inválida.")
    escolha = 0
    nim()

print(nim())
