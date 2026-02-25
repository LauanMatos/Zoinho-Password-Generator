import random
import string

def gerar_senha(tamanho, tem_maiusculas, tem_numeros, tem_simbolos):
    """Gera uma senha aleatória com as opções escolhidas"""
    caracteres = string.ascii_lowercase
    
    if tem_maiusculas:
        caracteres += string.ascii_uppercase
    if tem_numeros:
        caracteres += string.digits
    if tem_simbolos:
        caracteres += string.punctuation
    
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha