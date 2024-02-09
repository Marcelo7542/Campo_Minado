from tkinter import *
import random
from tkinter import messagebox


def jogo():
    # Criando a janela principal
    window = Tk()
    window.title("Campo Minado")

    
    # Função para lidar com o clique em um botão
    def clique_botao(event):
        botao = event.widget
        linha, coluna = botao.grid_info()["row"], botao.grid_info()["column"]
        if grade[linha][coluna] == -1:
            botao.config(text="*", bg="red")  # Mostra a imagem da bomba acima do texto
            if messagebox.askokcancel(title="Fail", message="Do you want to play again?"):
                window.destroy()
                jogo()
            else:
                window.destroy()
        elif grade[linha][coluna] == 0:
            atualizar_botao_zero(linha, coluna)
        else:
            botao.config(text=str(grade[linha][coluna]), bg="white")  # Mostra o número de minas vizinhas

    # Função para atualizar os botões ao redor do botão com valor zero
    def atualizar_botao_zero(linha, coluna):
        if grade[linha][coluna] == 0:
            botao = botoes[linha][coluna]
            botao.config(text=str(grade[linha][coluna]), bg="white")  # Mostra o número zero no botão
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    ni, nj = linha + dx, coluna + dy
                    if 0 <= ni < 12 and 0 <= nj < 12 and grade[ni][nj] == 0 and not visited[ni][nj]:
                        visited[ni][nj] = True
                        atualizar_botao_zero(ni, nj)

    # Criando e configurando os botões
    botoes = [[None] * 12 for _ in range(12)]
    visited = [[False] * 12 for _ in range(12)]
    grade = [[0] * 12 for _ in range(12)]
    minas = random.sample(range(144), 20)  # 20 minas aleatórias
    for mina in minas:
        linha, coluna = mina // 12, mina % 12
        grade[linha][coluna] = -1

    for i in range(12):
        for j in range(12):
            botao = Button(window, width=2, height=1, bg="gray", activebackground="light gray")
            botao.grid(row=i, column=j)
            botao.bind("<Button-1>", clique_botao)  # Associa a função clique_botao ao evento de clique esquerdo
            botoes[i][j] = botao

    # Calculando o número de minas vizinhas para cada botão
    for i in range(12):
        for j in range(12):
            if grade[i][j] == -1:
                continue  # Ignora os botões com minas
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 12 and 0 <= nj < 12 and grade[ni][nj] == -1:
                        grade[i][j] += 1

    # Mantendo a janela aberta
    window.mainloop()

jogo()
