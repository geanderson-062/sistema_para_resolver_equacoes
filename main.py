# Importando as libs
import customtkinter
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox

# Alterando a temática do sistema
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")  # Outro tema dark-blue

# Criando a janela
janela = customtkinter.CTk()

# Definindo tamanho da janela
janela.geometry("700x400")

# Definindo o título do sistema
janela.title("Sistema de Equações")

# Trocando o ícone do sistema
janela.iconbitmap("./assets/icone.ico")

# Impedindo reajuste da janela evitando que o usuário quebre a janela
janela.resizable(False, False)

# Definindo uma ação para o botão executar
def clique():

    # Pegando os dados digitados e colocando na variável Equacao1 e 2
    Equacao1 = equacao1.get()
    Equacao2 = equacao2.get()

    # caso nada seja digitado no sistema faça isso
    if (Equacao1 == "") and (Equacao2 == ""):
        messagebox.showerror("Erro", "Digite equações valida para X e Y .")
        return
    
    # caso nada seja digitado no campo equação X faça isso
    if (Equacao1 == "") :  
        messagebox.showerror("Erro", "Digite uma Equação valida para X .")
        return
    
    # caso nada seja digitado no campo equação Y faça isso
    if (Equacao2 == ""):
        messagebox.showerror("Erro", "Digite uma Equação valida para Y .")
        return
    
    # se tudo tiver certo execute o calculo e o grafico
    else:

        # Gerar valores para o eixo x
        x = np.linspace(-10, 10, 100)

        # Calcular os valores correspondentes no eixo x para a primeira equação
        y1 = eval(Equacao1)

        # Calcular os valores correspondentes no eixo y para a segunda equação
        y2 = eval(Equacao2)

        # Plotar o gráfico das equações
        plt.plot(x, y1, label="X")
        plt.plot(x, y2, label="Y")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Gráfico das Equações")
        plt.grid(True)
        plt.legend()
        plt.show()

# Escrevendo na janela
texto = customtkinter.CTkLabel(janela, text="Bem vindo", font=("Arial", 30))

# Colocando texto na janela e passando a distância dos itens
texto.pack(padx=10, pady=40)

# Criando campos para captar os dados

# campo equação X
equacao1 = customtkinter.CTkEntry(janela, placeholder_text="Digite a equação X", width=(200))
equacao1.pack(padx=10, pady=10)

# campo equação Y
equacao2 = customtkinter.CTkEntry(janela, placeholder_text="Digite a equação Y", width=(200))
equacao2.pack(padx=10, pady=10)

# Colocando um botão para enviar os dados
botao = customtkinter.CTkButton(janela, text="Resolver", command=clique, width=(200))
botao.pack(padx=10, pady=10)

# Rodando a janela
janela.mainloop()
