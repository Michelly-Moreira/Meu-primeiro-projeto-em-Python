# para mostrar na tela digite no terminal: python3 dia-01-python-na-pratica.py
print('Detalhamento')


mini_curso = 'Semana python na prática'
print(mini_curso)


nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
peso = input('Digite seu peso: ')
# Obs: Todos os dados que digitamos em input são do tipo string
print(type(peso))

# Convertendo os tipos strings em número inteiro:
peso = int(input('Digite seu peso: '))
# ou
peso = (int(peso))
print(type(peso))


# juntando textos com variáveis (f de formatado)
print(f'Meu nome é {nome}, eu tenho {idade} anos.')
