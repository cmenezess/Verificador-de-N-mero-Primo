#Faça um programa que receba um número e diga se esse número é primo ou não.
from tkinter import *

def numeros_primos():

    n = int(entrada.get())
    restos_divisao = []
    qtd = 0
    for i in range(1,n+1):
        restos_divisao.append(n % i)
        if n % i == 0:
            qtd += 1

    if qtd == 2:
        texto_resposta.config(text=f"{n} é um número primo. \nRestos da divisão: {restos_divisao}")
    else:
        texto_resposta.config(text=f"{n} não é um número primo. \nRestos da divisão: {restos_divisao}")


#Criando a interface gráfica:
janela = Tk()
#Adicionar o titulo:
janela.title("Verificador de Números Primos")


#Adicionar um texto de orientação:
texto_orientacao = Label(janela, text="Digite um número inteiro:")
texto_orientacao.pack(pady=10)


#Criar uma opção de entrada de texto:
entrada = Entry(janela)
entrada.pack(pady=5)

#Adicionar um botão:
botao = Button(janela, text="Verificar", command=numeros_primos)
botao.pack(pady=5)


#Adicionar um texto contendo as respostas:
texto_resposta = Label(janela, text="")
texto_resposta.pack(pady=10)


#Executar o loop de eventos:
janela.mainloop()