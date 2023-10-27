'''
Executar no terminal:

pip install requests
OU
py -3.11 -m pip install requests
'''

'''API Ninjas'''

import requests

cep = input('Informe o CEP: ')
url = f'https://viacep.com.br/ws/{cep}/json/'
try:
    resposta = requests.get(url)                # realiza uma requisição a API
    if resposta.status_code == 200:             # verifica o codigo de retorno (200 - sucesso)
        print(resposta.text)

        dicionario = resposta.json()            # converte a string de retorno em um dicionario
        
        if 'erro' in dicionario:
            print('CEP inexistente')
        else:                                   # exibe as informações
            print(f"Rua: {dicionario['logradouro']}")
            print(f"Complemento: {dicionario['complemento']}")
            print(f"Bairro: {dicionario['bairro']}")
            print(f"Cidade: {dicionario['localidade']}")
            print(f"Estado: {dicionario['uf']}")
  
    else:
        print(resposta.status_code)
except ConnectionError:
    print('Erro de conexão')
except Exception as erro:
    print(f'Erro: {erro}')
