import requests

# utilizaremos a lib requests para realizar solicitações HTTP
# primeiro instalar  lib pip install requests

resposta  = requests.get('https://www.digitalocean.com/community')
if resposta:
    print('Conexão bem sucedida')
else:
    print('Não foi possivel se conectar!!')

print(resposta.status_code)

#cabeçalho
print(resposta.headers)

#conteudo html da pagina
# print(resposta.text)
