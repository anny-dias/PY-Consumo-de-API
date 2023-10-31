'''
Executar no terminal:

pip install requests
OU
py -3.11 -m pip install requests
'''

'''API Ninjas'''

import requests

try:
    cep = input('Informe o CEP: ')
    url = f'https://viacep.com.br/ws/{cep}/json/'

    resposta = requests.get(url)                # realiza a requisição
    if resposta.status_code == 200:             # verifica o codigo de retorno: OK (200)
        dicionario = resposta.json()            # gera um dicionário a partir da resposta da API

        if 'erro' in dicionario:
            print('CEP inexistente')
        else:
            print(f"Rua: {dicionario['logradouro']}")
            print(f"Complemento: {dicionario['complemento']}")
            print(f"Bairro: {dicionario['bairro']}")
            print(f"Cidade: {dicionario['localidade']}")
            print(f"Estado: {dicionario['uf']}")

    elif resposta.status_code == 400:            # Bad Request
        print('ERRO: O cep deve ter 8 caracteres')
except ConnectionError:
    print('ERRO: Não foi possivel acessar a API')
except Exception as mensagem:
    print(f'ERRO: {mensagem}')



