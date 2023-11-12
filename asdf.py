def verificar_palavra(palavra_sorteada, tentativa):
    resultado = indica_posicao(palavra_sorteada, tentativa)
    dicas = []
    for index, val in enumerate(resultado):
        if val == 0:
            dicas.append('\033[34m' + tentativa[index])  # Azul para letra na posição correta
        elif val == 1:
            dicas.append('\033[33m' + tentativa[index])  # Amarelo para letra na palavra, mas na posição errada
        else:
            dicas.append('\033[37m' + tentativa[index])  # Cinza para letra ausente na palavra
    return ' '.join(dicas)

def jogo():
    palavras = filtra(words, 5)
    estado_jogo = inicializa(palavras)
    palavra_sorteada = estado_jogo['sorteada']
    tentativas_restantes = estado_jogo['tentativas']

    continuar_jogando = True

    print("Bem-vindo ao jogo Termo! Tente adivinhar a palavra de 5 letras.")

    while continuar_jogando and tentativas_restantes > 0:
        print(f"\nTentativas restantes: {tentativas_restantes}")
        tentativa = input("Digite uma palavra de 5 letras ou 'desisto' para encerrar o jogo: ").lower()

        if tentativa == 'desisto':
            print(f"A palavra correta era: {palavra_sorteada}")
            break

        if len(tentativa) != estado_jogo['n']:
            print("Por favor, digite uma palavra de 5 letras.")
            continue

        if tentativa == palavra_sorteada:
            print("Parabéns! Você acertou a palavra!")
            break
        else:
            tentativas_restantes -= 1
            resultado = verificar_palavra(palavra_sorteada, tentativa)
            print(f"Palavra incorreta. Dicas: {resultado}")

    if tentativas_restantes == 0:
        print(f"Você perdeu! A palavra correta era: {palavra_sorteada}")

    continuar = input("Deseja jogar novamente? (sim/não): ")
    if continuar.lower() != 'sim':
        continuar_jogando = False

    if continuar_jogando:
        jogo()
    else:
        print("Obrigado por jogar!")

# Iniciar o jogo
jogo()