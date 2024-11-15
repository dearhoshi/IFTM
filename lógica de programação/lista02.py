# Exercício 1: Contagem Progressiva

for x in range(1, 11):
    print(x)
   
# Exercício 2: Contagem Regressiva

for y in range(10, 0, -1):
    print(y)

# Exercício 3: Tabuada

tab = int(input('digite um numero:'))

for x in range(1, 11):
    resultado = tab * x
    print(f"{tab} x {x} = {resultado}")
   
# Exercício 4: Soma dos Números Pares

num = int(input("digite um numero inteiro positivo: "))
soma = 0

for x in range(1, num + 1):
    if x % 2 == 0:
        soma += x
   
print(f"o resultado da soma dos numeros pares é: {soma}")

# Exercício 5: Média de Notas

numero = 1
contador = 0
media = 0

while numero != 0:
    numero = int(input('digite um valor:'))
    contador = contador + 1
    media = media + numero
   
print("a media dos", (contador-1), "valores é", media/(contador-1))

# Exercício 6: Fatorial

x = int(input('Digite um número inteiro positivo: '))
fatorial = 1

for i in range(1, x + 1):
    fatorial *= i

print(f"O fatorial de {x} é {fatorial}.")

# Exercício 7: Tabuada

tab = int(input('digite um numero:'))

for x in range(1, 11):
    resultado = tab * x
    print(f"{tab} x {x} = {resultado}")


# Exercício 8: Impressão de Números Ímpares

for i in range(1, 50 + 1, 2):
    if i % 2 != 0:
        print(i)