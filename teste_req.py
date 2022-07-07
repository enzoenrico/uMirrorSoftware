from unicodedata import name
import requests
import json
import request_maker

data = {
    "name" : "Among Us da Silva",
    "isAlive" : True   #Fazer o isAlive e outros protocolos serem o metodo de autenticação pra mudança de fase do reconhecimento
}

data_post = requests.post('https://httpbin.org/post', data)

print(data_post.text)


if data_post.status_code == 200:
    print('[+]Tudo funfando poggers')

json_format = json.loads(data_post.text)

print(f'Dados enviados {json_format["form"]}')

print("Request maker")

print(
request_maker.req_maker(data)
)