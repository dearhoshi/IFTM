# crie um programa que peça o ano atual e o ano de nascimento do usuário, e exiba sua idade.

ano = int(input('digite o ano atual: '))
ano_nascimento = int(input('digite seu ano de nascimento: '))

idade = (ano - ano_nascimento)

print(f'sua idade é {idade} anos.')