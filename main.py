from ast import arg
from face_rec_v2 import Video
import send2server
import face_rec_v2
import gather

import time
import multiprocessing

if __name__ == "__main__":
    print('[+]Inicializando...')
    face_rec_v2.gen(Video())

    time.sleep(2)

    print('[+]Iniciando recolhimento de dados')
    print(gather.data_gather())

    print('[+]Enviando dados para o Servidor...')
    send2server.send()
    print('[+]Dados enviados com sucesso!')
    # send2server.send()

# Criar metodo para criar imagem
