#1.Concatenação simples de variáveis de texto
nome = "Maria"
sobrenome = "da Silva"
nome_completo = nome + " " + sobrenome

print("Nome completo: ", nome_completo )

#2.Concatenação combinando texto com número
idade = 32
mensagem = "Olá, meu nome é " + nome_completo + " e eu tenho " + str(idade) + " anos"

print(mensagem)

#3. Números inseridos pelo usuário
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1+nota_2+nota_3) / 3

print("A média das notas é: ", media)
print(f"A média das notas é: {media:.2f}")
print(f"A média das notas é: {round(media,2)}")