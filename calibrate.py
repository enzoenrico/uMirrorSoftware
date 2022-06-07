#Precisa de um intervalo de tempo / quant de informação pra parar o reconhecimento
#Como implementar esse intervalo de forma que o feed de video continue funcionando?

import json

file_exp = open('expressions.txt', 'r')

i = 0

#Talvez substituir a lista por um dicionario, tipo {'felicidade': len(num_felicidade)}, talvez isso funcione

list_emotions = {
    "Felicidade": 0,
    "Neutro" : 0,
    "Raiva" : 0,
    "Nojo" : 0,
    "Medo" : 0,
    "Tristeza" : 0,
    "Surpresa" : 0
}

with file_exp:
    lines_in_file = file_exp.readlines()

#implementar todas as emoções

num_neutro = lines_in_file.count('Neutro \n')
num_feliz = lines_in_file.count('Felicidade \n')

#implementar todas as emoções
list_emotions.update({"Felicidade": num_feliz})
list_emotions.update({"Neutro": num_neutro})

def emot_value():
    return(max(list_emotions))

print(f'[-]Emoções totais: {len(lines_in_file)}')
print(f'[+]Emoções distintas: {len(list_emotions)}')
print(list_emotions)


#Assign um valor para cada emoção, quando uma aparecer mudar uma var indicando seu valor, jogar os valores em uma lista e fazer sua média ou pegar o que mais aparece
#Quem sabe criar um .json em um servidor mongo, mandar os dados, pegar e os processar novamente?

