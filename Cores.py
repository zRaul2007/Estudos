class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

n = int(input('Digite um número inteiro para ver sua tabuada: '))

print(f'\n{color.BOLD}{color.RED}\nA tabuada de {n} é: {color.END}\n')
print('*' * 15)

for i in range(10):
   print(f'{color.YELLOW}{n}  x   {i + 1}  =  {n * (i+1)}{color.END}')

print('*' * 15)
