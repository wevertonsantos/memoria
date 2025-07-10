import random

def main():
    if mostrar_menu():
            print(embaralhar_cartas(montar_cartas(criar_pares())))

def mostrar_menu():
    print("Bem-vindo ao jogo da memória")
    while True:
        try:
            escolha = int(input("Qual opção você deseja?\n1. Jogar\n2. Sair\nOpção: "))
            if escolha == 1:
                return True
            elif escolha == 2:
                print("Obrigado. Volte sempre!")
                return False
            else:
                print("Essa opção não existe.")
        except ValueError:
            print("Você digitou algo errado.")

def criar_pares():
    pares = [
        {"palavra":'escola',"palavra_ingles":'school'},
        {"palavra":'verde',"palavra_ingles":'green'}
    ]
    return pares

def montar_cartas(pares):
    lista_palavras = []
    for par in pares:
        lista_palavras.append(par['palavra'])
        lista_palavras.append(par['palavra_ingles'])
    return lista_palavras

def embaralhar_cartas(lista_palavras):
    random.shuffle(lista_palavras)
    return lista_palavras

def mostrar_tabulheiro(palavras):
    ...

main()