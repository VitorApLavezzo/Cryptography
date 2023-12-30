from funçoes import carregar_chave, criar_arquivo, criptografar, descriptografar
import sys

def main():
    fernet = carregar_chave()#Variavel que recebe a chave lida pela função

    print("1 - Criptografar Texto \n2 - Descriptografar")
    print(30 * '-')
    opcao = int(input("Digite uma das opções: "))
    print(30 * '-')

    # Verifica a opção escolhida pelo usuário: 1 - Criptografar ou 2 - Descriptografar
    nome_arq = ""
    if opcao == 1:
        opcao2 = input("Já possui um arquivo .txt (S/N)? ")
        if opcao2.lower() == 's':
            nome_arq = input("Digite o nome do arquivo para criptografar: ")
            if nome_arq == "":
                sys.exit()
                
        elif opcao2.lower() == 'n':
            print(30 * '-')
            print("Vamos criar um arquivo!!")
            print(30 * '-')
            texto_dig = input("Digite o texto que deseja criptografar: ")
            if texto_dig == "":
                print("Texto vazio!")
                sys.exit()
            nome_arq = input("Digite o nome do arquivo para guardar o texto: ")
            if nome_arq == "":
                print("Digite um nome valido!")
                sys.exit()
            criar_arquivo(nome_arq, texto_dig)

        elif opcao2 != (opcao2.lower() == 's') or opcao2 != (opcao2.lower() == 'n'):
            print("Você digitou uma opção inválida!")
            sys.exit()
        print("Seu texto foi criptografado!")
        criptografar(nome_arq, fernet)#Chama a função criptografar para criar arquivo .txt e inserir o texto dentro e criptografar o texto

    elif opcao == 2:
        nome_arq = input("Digite o nome do arquivo para descriptografar: ")
        print("Seu texto foi descriptografado")
        descriptografar(nome_arq, fernet)#Chama a função descriptografar para ler o texto dentro do arquivo .txt e descriptografar
    else:
        print("Digite uma opção válida!!")

if __name__ == "__main__":
    main()
