from cryptography.fernet import Fernet
import sys

#Função para ler a chave que esta no arquivo .key
def carregar_chave():
    with open('chave.key', 'rb') as filekey:
        chave = filekey.read()
    return Fernet(chave)

#Função para criar um arquivo .txt com texto digitado
def criar_arquivo(nome_arq, texto_dig):
    if nome_arq.strip():
        with open(f'{nome_arq}.txt', 'w') as arquivo:
            arquivo.write(texto_dig)
            print(f"O arquivo '{nome_arq}.txt' foi criado com sucesso")
    else:
        print("Nome do arquivo está vazio")
        sys.exit()

#Função para criptografar o texto que esta no arquivo .txt
def criptografar(nome_arq, fernet):
    with open(f'{nome_arq}.txt', 'rb') as arquivo:
        conteudo_arquivo = arquivo.read()

    criptografado = fernet.encrypt(conteudo_arquivo)
    with open(f'{nome_arq}.txt', 'wb') as arquivo_criptografado:
        arquivo_criptografado.write(criptografado)

#Função para descriptografar o texto que esta no arquivo .txt
def descriptografar(nome_arq, fernet):
    with open(f'{nome_arq}.txt', 'rb') as arquivo:
        conteudo_arquivo = arquivo.read()

    descriptografado = fernet.decrypt(conteudo_arquivo)
    with open(f'{nome_arq}.txt', 'wb') as arquivo_descriptografado:
        arquivo_descriptografado.write(descriptografado)
