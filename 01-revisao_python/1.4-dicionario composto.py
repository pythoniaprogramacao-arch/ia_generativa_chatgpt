funcionarios = {
    101: {
        "nome":"Bruno",
        "cargo": "Dev",
        "Habilidades": ["Python","C##", "Java"]
    },
    102: {
        "nome":"Elionai",
        "cargo": "Sup",
        "Habilidades": ["Analistica","Gestão"]
    },
}

print(funcionarios[101]["cargo"])
print(funcionarios.get(102,{}).get("nome"))

