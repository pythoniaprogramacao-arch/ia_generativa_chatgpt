funcionarios = {
    101: {
        "nome": "Carlos",
        "cargo": "desenvolvedor",
        "habilidades": ["Python","C##","Java"]
    },
    102: {
        "nome": "Mariana",
        "cargo": "gerente de projetos",
        "habilidades": ["Scrum","Gestão"]
    }
}

print(funcionarios[101]["cargo"])
print(funcionarios.get(103,{}).get("nome","Fucionário não encontrado"))