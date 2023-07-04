#importando as libs
import customtkinter
from tkinter import * 
import numpy as np
import matplotlib.pyplot as plt

#alterando a tematica do sistema
customtkinter.set_appearance_mode ("dark")
customtkinter.set_default_color_theme("green") # outro thema dark-blue

#criando a janela
janela= customtkinter.CTk()

#definindo tamanho da janela
janela.geometry("700x400")

#definindo o titulo do sistema
janela.title("Sistema de Equações")

#trocando o icone do sistema
janela.iconbitmap("icone.ico")

#impedindo reajuste da janela evitando que o usuario quebre a janela 
janela.resizable(False, False)

#definindo uma ação para o botão executar 
def clique():
   
    #pegando os dados digitados e colocando na vareavel Equacao1 e 2 
    Equacao1 = equacao1.get()
    Equacao2 = equacao2.get()

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

# escrevendo na janela 
texto = customtkinter.CTkLabel(janela, text="Bem vindo", font=("Arial", 30))

#colocando texto na janela e passando a distancia dos itens 
texto.pack(padx=10, pady=40)

#criando campo para captar os dados
equacao1 = customtkinter.CTkEntry(janela, placeholder_text="Digite a equação X",width=(200))
equacao1.pack(padx=10, pady=10)

equacao2 = customtkinter.CTkEntry(janela, placeholder_text="Digite a equação Y", width=(200))
equacao2.pack(padx=10, pady=10)

#colocando um botão 
botao = customtkinter.CTkButton(janela, text="Resolver", command=clique, width=(200))
botao.pack(padx=10, pady=10)

#rodando a janela
janela.mainloop()