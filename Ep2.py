import random
import string
from palavras import words

def filtra(lista_palavras, num_letras):
    palavras_filtradas = []

    for palavra in lista_palavras:
        palavra_processada = palavra.lower().strip(string.punctuation)
        
        if len(palavra_processada) == num_letras:
            palavras_filtradas.append(palavra_processada)

    palavras_filtradas = list(set(palavras_filtradas))  

    return palavras_filtradas

def inicializa(lista_palavras):
    n = len(lista_palavras[0])   

    dicionario = {
        'n': n,
        'tentativas': n + 1,
        'especuladas': [],
        'sorteada': random.choice(lista_palavras)
    }

    return dicionario

def indica_posicao(sorteada, especulada):
    if len(sorteada) != len(especulada):
        return []  

    resultado = []

    for i in range(len(sorteada)):
        if especulada[i] == sorteada[i]:
            resultado.append(0)  # Letra na posição correta
        elif especulada[i] in sorteada:
            resultado.append(1)  # Letra existe na palavra sorteada, mas em posição errada
        else:
            resultado.append(2)  # Letra não existe na palavra sorteada

    return resultado
