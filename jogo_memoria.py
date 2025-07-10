def main():
    if mostrar_menu():
        ...

def mostrar_menu():
    while True:
        print("Bem-vindo ao jogo da memória")
        try:
            escolha = int(input("Qual opção você deseja?\n1. Jogar\n2. Sair"))
            if escolha == 1:
                return True
            elif escolha == 2:
                return False
            else:
                print("Essa opção não existe.")
        except ValueError:
            print("Você digitou algo errado.")

main()