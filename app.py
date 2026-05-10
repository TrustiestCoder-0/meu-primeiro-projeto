print('Oi, tudo bem?')

resposta = input()

print('Que legal!')

nome = input('Qual é o seu nome, programador? ')

idade = input('Qual é a sua idade? ')

with open('dados.txt', 'w') as arquivo:
    arquivo.write(f'Nome: {nome}\n')
    arquivo.write(f'Idade: {idade}')

print('Dados salvos com sucesso!')

print('Uau', nome + '!', 'Você é muito novo para um programador tão bom!')