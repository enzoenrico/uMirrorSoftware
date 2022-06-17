    #Precisa de um intervalo de tempo / quant de informação pra parar o reconhecimento
    #Como implementar esse intervalo de forma que o feed de video continue funcionando?
from asyncio import gather
from datetime import date, datetime

def data_gather():
    file_exp = open('expressions.txt', 'r')
    date_now = datetime.now()

    #Talvez substituir a lista por um dicionario, tipo {'felicidade': len(num_felicidade)}, talvez isso funcione

    list_emotions = {
        "Felicidade": 0,
        "Neutro" : 0,
        "Raiva" : 0,
        "Nojo" : 0,
        "Medo" : 0,
        "Tristeza" : 0,
        "Surpresa" : 0,
        "data" : str(date_now)
    }

    with file_exp:
        lines_in_file = file_exp.readlines()

    #implementar todas as emoções

    

    num_neutro = lines_in_file.count('Neutro \n')
    num_feliz = lines_in_file.count('Felicidade \n')
    num_raiva = lines_in_file.count('Raiva \n')
    num_nojo = lines_in_file.count('Nojo \n')
    num_medo = lines_in_file.count('Medo \n')
    num_triste = lines_in_file.count('Triste \n')
    num_surpresa = lines_in_file.count('Surpresa \n')
        
    #implementar todas as emoções
    list_emotions.update({"Felicidade": num_feliz})
    list_emotions.update({"Neutro": num_neutro})
    list_emotions.update({"Raiva": num_raiva})
    list_emotions.update({"Nojo": num_nojo})
    list_emotions.update({"Medo": num_medo})
    list_emotions.update({"Tristeza": num_triste})
    list_emotions.update({"Surpresa": num_surpresa})


    # print(f'[-]Emoções totais: {len(lines_in_file)}')
    # print(f'[+]Emoções distintas: {len(list_emotions)}')
    # print(list_emotions)
    
    return list_emotions
    #Assign um valor para cada emoção, quando uma aparecer mudar uma var indicando seu valor, jogar os valores em uma lista e fazer sua média ou pegar o que mais aparece
    #Quem sabe criar um .json em um servidor mongo, mandar os dados, pegar e os processar novamente?