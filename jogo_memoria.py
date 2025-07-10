import random

def main():
    
    if mostrar_menu():
        pares = criar_pares()
        cartas = montar_cartas(pares)
        cartas_embaralhadas = embaralhar_cartas(cartas)
        reveladas = []
        mostrar_tabulheiro(cartas_embaralhadas,reveladas)

        pos1,pos2 = escolher_cartas(cartas)
        reveladas.append(pos1)
        reveladas.append(pos2)
        
        mostrar_tabulheiro(cartas_embaralhadas,reveladas)
        verificar_par(cartas,reveladas)

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
    return cartas

def mostrar_tabulheiro(cartas,reveladas):
    mostrar_palavras = ""
    for i in range(len(cartas)):
        mostrar_palavras = f"?"
        if i not in reveladas:
            print(mostrar_palavras)
        else:
            mostrar_palavras = f"{cartas[i]}"
            print(mostrar_palavras)

def escolher_cartas(cartas):
    try:
        while True:
            pos1 = int(input("Escolha a primeira posição: "))
            pos2 = int(input("Escolha a segunda posição: "))
            if pos1 < 0 or pos2 < 0 or pos1 >= len(cartas) or pos2 >= len(cartas):
                print("Essa opção não existe")
            elif pos1 == pos2:
                print("Você não pode escolher a mesma posição duas vezes")
            else:
                return pos1,pos2
    except ValueError:
        print("Você escolheu algo errado!")

def verificar_par(cartas,reveladas):
    for i in range(len(cartas)):
        print(cartas[i])
        print(reveladas)

main()
