import random

def main():
    if mostrar_menu():
        pares = criar_pares()
        cartas = montar_cartas(pares)
        embaralhar_cartas(cartas)
        mostrar_tabulheiro(cartas)
        escolha1,escolha2 = receber_escolhas()
        verificar_par(escolha1,escolha2,cartas)

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

def embaralhar_cartas(cartas):
    random.shuffle(cartas)

def receber_escolhas():
    while True:
        try:
            escolha1 = int(input("Qual a primeira carta que você gostaria de virar? "))
            escolha2 = int(input("Qual a segunda carta que você gostaria de virar? "))
            return escolha1,escolha2
        except ValueError:
            print("Você digitou algo errado.")

def mostrar_tabulheiro(cartas,escolha1,escolha2):
    for i in range(len(cartas)):
        print(f"{i} - ?")
    for i in range(len(cartas)):
        if i == escolha1:
            print(f"{i} - {cartas[i]}")
        if i == escolha2:
            print(f"{i} - {cartas[i]}")

def verificar_par(escolha1,escolha2,cartas):
    ...

main()
