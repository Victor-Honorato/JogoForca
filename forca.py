def mostrar_tracinhos(palavra, letras_certas):
    tracinhos = ''
    for letra in palavra:
        if letra in letras_certas:
            tracinhos += letra + ' '
        else:
            tracinhos += '_ '
    return tracinhos

def jogo_da_forca():
    print("Jogo da Forca")
    tema = input("Jogador 1, escolha o tema da palavra: ")
    palavra = input(f"Jogador 1, escolha uma palavra relacionada ao tema '{tema}': ").lower()
    letras_certas = set()
    letras_erradas = set()
    tentativas = 6

    while tentativas > 0:
        tracinhos = mostrar_tracinhos(palavra, letras_certas)
        print(f"Tema: {tema}")
        print(f"Palavra: {tracinhos}")

        if '_' not in tracinhos:
            print("Parabéns! Você acertou a palavra.")
            break

        print(f"Tentativas restantes: {tentativas}")
        opcao = input("Jogador 2, digite 'letra' para tentar uma letra ou 'chutar' para adivinhar a palavra: ").lower()

        if opcao == 'letra':
            letra = input("Insira uma letra: ").lower()

            if letra in letras_certas or letra in letras_erradas:
                print("Você já tentou essa letra. Tente outra.")
                continue

            if letra in palavra:
                letras_certas.add(letra)
            else:
                letras_erradas.add(letra)
                tentativas -= 1
        elif opcao == 'chutar':
            chute = input("Chute a palavra: ").lower()
            if chute == palavra:
                print("Parabéns! Você acertou a palavra.")
                break
            else:
                print("Chute errado!")
                tentativas -= 1
        else:
            print("Opção inválida. Tente novamente.")

    if tentativas == 0:
        print(f"Suas tentativas acabaram! A palavra era '{palavra}'.")

jogo_da_forca()
