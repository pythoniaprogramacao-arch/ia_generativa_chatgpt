import csv

dados_tabela = [
    ["Nome","Cargo","Idade"],
    ["Calos","Desenvolvedor",28],
    ["Ana Souza","Engenheira de Dados",32],
    ["Mariana Santos","Gerente de Projetos",41],
    ["Lucas Oliveira","Estagiário",21]
]

with open("08.2-funcionarios.csv","w",encoding="utf-8",newline="") as arquivo_csv:
    escrever = csv.writer(arquivo_csv)
    escrever.writerows(dados_tabela)
