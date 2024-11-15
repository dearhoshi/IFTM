# peça ao usuário para informar a senha correta. Continue pedindo até ele acertar.

senha = 'nayeon123'
senha_tentativa = " "

while senha_tentativa != senha:
    senha_tentativa = input('digite a senha:')
    
    if senha_tentativa != senha:
        print('senha incorreta, tente novamente:')

print('senha correta. acesso permitido!')

