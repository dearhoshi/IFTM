# escreva um programa que leia uma lista de compras, peça 5 itens e exiba a lista completa.

compras = []

for x in range(1, 6):
    item = input(f'digite o item {x}: ')
    compras += [item]  

print("\nlista de compras:")
for item in compras:
    print(f"- {item}")
