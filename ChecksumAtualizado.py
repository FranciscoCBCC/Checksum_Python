import sys
from tkinter import *


def conta(string):
    soma=0
    for i in range(len(string)):
        soma = soma + (i * ord(string[i]))
    return soma

def entradaMensagem():
    string = input(str("Entre com sua mensagem: "))
    soma = conta (string)
    print("Checksum: ",soma)
    
def validarMensagem():
    stringValida = input(str("Entre com sua mensagem para verificacao: "))
    somaValida = int(input("Digite o checksum: "))
    soma_aux = conta(stringValida)
    if somaValida != soma_aux:
        print("Messagem diferentes")
    else:
        print("Messagem iguais")

def sair():
        print ("Saindo ...")
        sys.exit(0)


janela = Tk() #Instancia uma janela
janela.title("Checksum")
frame1 = Frame(janela) #Cria um frame na janela
frame1.pack() #Exibe o frame
entrada = Entry(janela)
entrada.pack()
botao = Button(frame1, text = "Calcular", command = entradaMensagem) #Cria um botão no frame 1
botao['width'] = 10 #Define a largura do botão
#botao.bind("", entradaMensagem) #Cria um event dando uma ação ao botão
botao.pack() #Exibe oo botão


frame2 = Frame(janela) #Cria um frame na janela
frame2.pack() #Exibe o frame
botao2 = Button(frame2, text = "Validar", command = validarMensagem) #Cria um botão no frame 1
botao2['width'] = 10 #Define a largura do botão
#botao.bind("", entradaMensagem) #Cria um event dando uma ação ao botão
botao2.pack() #Exibe oo botão
frame3 = Frame(janela) #Cria um frame na janela
frame3.pack() #Exibe o frame
botao3 = Button(frame3, text = "Sair", command = sair) #Cria um botão no frame 1
botao3['width'] = 10 #Define a largura do botão
#botao.bind("", entradaMensagem) #Cria um event dando uma ação ao botão
botao3.pack() #Exibe oo botão
janela.mainloop() #Loop da janela principal


        
