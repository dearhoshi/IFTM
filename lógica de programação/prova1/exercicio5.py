# peça um número ao usuário e exiba a soma de todos os números de 1 até o número informado.

num = int(input('digite o número que deseja ver a tabuada de adição:'))
for x in range(1, num):
    resultado = x + num
    print(f'{x} + {num} = {resultado}')