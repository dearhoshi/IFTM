#  solicite ao usuário um número e imprima a tabuada desse número de 1 a 10.

num = int(input('digite o número que deseja ver a tabuada de multiplicação:'))
for x in range(1, 11):
    resultado = num * x
    print(f'{num} x {x} = {resultado}')