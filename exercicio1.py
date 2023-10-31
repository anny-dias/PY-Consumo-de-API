'''
EXERCICIO 1:
Utilizar a API viaCEP para buscar um CEP a partir de um endereço digitado pelo usuário.
Instalar o módulo requests utilizando o comando abaixo no terminal:
py -3.11 -m pip install requests
'''

import requests

uf = input('Informe a UF: ')
cidade = input('Informe a cidade: ')
logradouro = input('Informe a Rua: ')

url = f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/'

data = requests.get(url)

if data.status_code == 200:     #OK
    print(data.text)            #exibe o texto de retorno de requisição

    lista = data.json()         #converte o texto para uma estrutura python

    ceps = {}
    codigo = 1
    for dicionario in lista:    #percorre a lista
        print(dicionario)
        ceps[codigo] = f'Complemento: {dicionario["complemento"]} CEP: {dicionario["cep"]}'
        codigo += 1
    
    for chave, valor in ceps.items():       #percorre dicionario de ceps para o usuário escolher
        print(f'{chave} - Complemento: {valor[0]} CEP: {valor[1]}')
    opcao = input('Selecione uma opção: ')

    cep_escolhido = ceps[opcao][1]          #seleciona o cep selecionado pelo usuário
    print(cep_escolhido)
else:
    print(f'ERRO {data.status_code}')