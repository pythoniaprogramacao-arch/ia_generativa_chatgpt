"""
Jogo Matemático - Aprenda Fazendo Contas!
Feito para ajudar crianças a praticar soma, subtração,
multiplicação e divisão de forma divertida.
"""

import random


def gerar_pergunta(nivel):
    """
    Gera uma pergunta matemática de acordo com o nível escolhido.
    Nível 1: números pequenos (1 a 10), soma e subtração
    Nível 2: números médios (1 a 20), soma, subtração e multiplicação
    Nível 3: números maiores (1 a 50) e as 4 operações
    """
    if nivel == 1:
        operacoes = ["+", "-"]
        a = random.randint(1, 10)
        b = random.randint(1, 10)
    elif nivel == 2:
        operacoes = ["+", "-", "x"]
        a = random.randint(1, 20)
        b = random.randint(1, 12)
    else:
        operacoes = ["+", "-", "x", "/"]
        a = random.randint(1, 50)
        b = random.randint(1, 12)

    operacao = random.choice(operacoes)

    # Garante que a subtração não dê número negativo
    if operacao == "-" and b > a:
        a, b = b, a

    # Garante que a divisão dê resultado exato (sem decimais)
    if operacao == "/":
        b = random.randint(1, 10)
        resultado = random.randint(1, 10)
        a = b * resultado

    if operacao == "+":
        resposta_certa = a + b
    elif operacao == "-":
        resposta_certa = a - b
    elif operacao == "x":
        resposta_certa = a * b
    else:
        resposta_certa = a // b

    pergunta = f"{a} {operacao} {b} = ?"
    return pergunta, resposta_certa


def escolher_nivel():
    print("Escolha o nível:")
    print("1 - Fácil (números de 1 a 10, soma e subtração)")
    print("2 - Médio (números de 1 a 20, + soma multiplicação)")
    print("3 - Difícil (números de 1 a 50, todas as operações)")

    while True:
        escolha = input("Digite 1, 2 ou 3: ").strip()
        if escolha in ["1", "2", "3"]:
            return int(escolha)
        print("Opção inválida, tente novamente.")


def jogar():
    print("=" * 40)
    print(" JOGO MATEMÁTICO - VAMOS PRATICAR CONTAS! ")
    print("=" * 40)

    nivel = escolher_nivel()

    while True:
        try:
            total_perguntas = int(input("\nQuantas perguntas você quer responder? "))
            if total_perguntas > 0:
                break
            print("Digite um número maior que zero.")
        except ValueError:
            print("Digite um número válido.")

    acertos = 0
    erros = 0

    print("\nVamos começar! Boa sorte! 🍀\n")

    for numero_pergunta in range(1, total_perguntas + 1):
        pergunta, resposta_certa = gerar_pergunta(nivel)
        print(f"Pergunta {numero_pergunta}/{total_perguntas}: {pergunta}")

        while True:
            try:
                resposta_aluno = int(input("Sua resposta: "))
                break
            except ValueError:
                print("Por favor, digite apenas números.")

        if resposta_aluno == resposta_certa:
            print("✅ Isso mesmo! Muito bem!\n")
            acertos += 1
        else:
            print(f"❌ Quase! A resposta certa era {resposta_certa}.\n")
            erros += 1

    # Resultado final
    print("=" * 40)
    print(" RESULTADO FINAL ")
    print("=" * 40)
    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")

    porcentagem = (acertos / total_perguntas) * 100
    print(f"Aproveitamento: {porcentagem:.0f}%")

    if porcentagem == 100:
        print("🏆 Perfeito! Você acertou tudo!")
    elif porcentagem >= 70:
        print("🌟 Muito bem! Continue praticando!")
    elif porcentagem >= 50:
        print("👍 Bom trabalho, mas dá pra melhorar!")
    else:
        print("💪 Não desista, a prática leva à perfeição!")


def jogar_novamente():
    resposta = input("\nQuer jogar de novo? (s/n): ").strip().lower()
    return resposta == "s"


if __name__ == "__main__":
    continuar = True
    while continuar:
        jogar()
        continuar = jogar_novamente()

    print("\nObrigado por jogar! Até a próxima! 👋")