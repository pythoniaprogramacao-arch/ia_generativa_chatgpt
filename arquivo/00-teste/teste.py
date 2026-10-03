import tkinter as tk

# Criar janela
janela = tk.Tk()
janela.title("❤️ Para Elionai ❤️")
janela.geometry("600x500")
janela.configure(bg="black")

# Criar área de desenho
canvas = tk.Canvas(
    janela,
    width=600,
    height=500,
    bg="black",
    highlightthickness=0
)
canvas.pack()

# Coração
pontos = [
    300, 400,
    100, 220,
    100, 140,
    150, 90,
    220, 90,
    300, 170,
    380, 90,
    450, 90,
    500, 140,
    500, 220
]

canvas.create_polygon(
    pontos,
    fill="red",
    outline="pink",
    width=5,
    smooth=True
)

# Mensagem
canvas.create_text(
    300,
    190,
    text="ELIONAI",
    fill="white",
    font=("Arial", 30, "bold")
)

canvas.create_text(
    300,
    240,
    text="LOVE YOU ❤️",
    fill="white",
    font=("Arial", 26, "bold")
)

# Mensagem abaixo
canvas.create_text(
    300,
    450,
    text="Feito com ❤️ para Elionai",
    fill="pink",
    font=("Arial", 18, "italic")
)

janela.mainloop()