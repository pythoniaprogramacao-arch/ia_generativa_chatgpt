"""
Jogo de Lógica - Desafie sua Mente!
Feito para ajudar crianças a desenvolver raciocínio lógico
com desafios de sequências, padrões e adivinhação.
"""

import random


def desafio_sequencia():
    """Gera uma sequência numérica e pede o próximo número."""
    tipo = random.choice(["soma", "dobro", "impar_par"])

    if tipo == "soma":
        passo = random.randint(2, 5)
        inicio = random.randint(1, 10)
        sequencia = [inicio + passo * i for i in range(4)]
        resposta = sequencia[-1] + passo
        dica = f"Cada número aumenta {passo}."
    elif tipo == "dobro":
        inicio = random.randint(1, 5)
        sequencia = [inicio * (2 ** i) for i in range(4)]
        resposta = sequencia[-1] * 2
        dica = "Cada número é o dobro do anterior."
    else:
        inicio = random.randint(1, 10)
        sequencia = [inicio + i * 2 for i in range(4)]
        resposta = sequencia[-1] + 2
        dica = "Repare no intervalo entre os números."

    pergunta = f"Qual é o próximo número da sequência? {', '.join(map(str, sequencia))}, ?"
    return pergunta, resposta, dica


def desafio_intruso():
    """Pede para encontrar o número que não pertence ao grupo."""
    tipo = random.choice(["pares", "impares", "multiplos_5"])

    if tipo == "pares":
        numeros = [random.randint(1, 20) * 2 for _ in range(4)]
        intruso = random.randint(1, 20) * 2 + 1
        dica = "Os outros números são todos pares."
    elif tipo == "impares":
        numeros = [random.randint(1, 20) * 2 + 1 for _ in range(4)]
        intruso = random.randint(1, 20) * 2
        dica = "Os outros números são todos ímpares."
    else:
        numeros = [random.randint(1, 10) * 5 for _ in range(4)]
        intruso = random.randint(1, 50)
        while intruso % 5 == 0:
            intruso = random.randint(1, 50)
        dica = "Os outros números são todos múltiplos de 5."

    todos = numeros + [intruso]
    random.shuffle(todos)
    pergunta = f"Qual número não combina com os outros? {', '.join(map(str, todos))}"
    return pergunta, intruso, dica


def desafio_adivinhacao():
    """Jogo de adivinhar o número secreto com dicas de maior/menor."""
    numero_secreto = random.randint(1, 50)
    print("\n🔍 Vou pensar em um número entre 1 e 50. Tente adivinhar!")

    tentativas = 0
    max_tentativas = 7

    while tentativas < max_tentativas:
        try:
            palpite = int(input(f"Tentativa {tentativas + 1}/{max_tentativas}: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        tentativas += 1

        if palpite == numero_secreto:
            print(f"🎉 Isso mesmo! O número era {numero_secreto}!")
            return True
        elif palpite < numero_secreto:
            print("📈 É maior que isso!")
        else:
            print("📉 É menor que isso!")

    print(f"😅 Suas tentativas acabaram. O número era {numero_secreto}.")
    return False


def jogar_rodada_desafios(quantidade):
    """Alterna entre desafios de sequência e de intruso."""
    acertos = 0

    for i in range(1, quantidade + 1):
        tipo_desafio = random.choice(["sequencia", "intruso"])

        if tipo_desafio == "sequencia":
            pergunta, resposta, dica = desafio_sequencia()
        else:
            pergunta, resposta, dica = desafio_intruso()

        print(f"\nDesafio {i}/{quantidade}")
        print(pergunta)

        quer_dica = input("Quer uma dica? (s/n): ").strip().lower()
        if quer_dica == "s":
            print(f"💡 Dica: {dica}")

        while True:
            try:
                resposta_jogador = int(input("Sua resposta: "))
                break
            except ValueError:
                print("Digite apenas números.")

        if resposta_jogador == resposta:
            print("✅ Correto! Muito bem!")
            acertos += 1
        else:
            print(f"❌ Não foi dessa vez. A resposta certa era {resposta}.")

    return acertos


def menu_principal():
    print("=" * 45)
    print("        JOGO DE LÓGICA - DESAFIE SUA MENTE!")
    print("=" * 45)
    print("1 - Descubra o padrão (sequências e intrusos)")
    print("2 - Adivinhe o número secreto")
    print("3 - Sair")


def main():
    while True:
        menu_principal()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            while True:
                try:
                    quantidade = int(input("Quantos desafios você quer? "))
                    if quantidade > 0:
                        break
                    print("Digite um número maior que zero.")
                except ValueError:
                    print("Digite um número válido.")

            acertos = jogar_rodada_desafios(quantidade)
            print(f"\n🏁 Você acertou {acertos} de {quantidade} desafios!")

        elif opcao == "2":
            jogar_rodada_desafios_disponivel = True
            continuar_adivinhando = True
            while continuar_adivinhando:
                desafio_adivinhacao()
                resposta = input("\nQuer jogar de novo? (s/n): ").strip().lower()
                continuar_adivinhando = resposta == "s"

        elif opcao == "3":
            print("\nAté a próxima, continue exercitando a lógica! 🧠✨")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()