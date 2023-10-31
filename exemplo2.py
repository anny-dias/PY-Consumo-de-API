import requests
import json


name = 'bull terrier'
api_url = f'https://api.api-ninjas.com/v1/dogs?name={name}'

your_key = ''       # Realizar cadastro e gerar uma chave no site api-ninjas.com

response = requests.get(api_url, headers={'X-Api-Key': your_key})

if response.status_code == requests.codes.ok:           # 200
    
    # exibe o texto de retorno
    print(response.text)                          
    
    # converte para uma esturtura do python
    dados = response.json()   

    # percorre os dados e exibe algumas insformações
    for item in dados:
        print('--------------------')
        print(f'Nome: {item["name"]}')   
        print(f'Imagem: {item["image_link"]}')   
        print(f'Nivel de energia: {item["name"]}')                      

    # exporta para um arquivo json
    with open('dados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
else:
    print("Error:", response.status_code, response.text)






