import sys
from tkinter import *


def conta(string):
    soma=0
    for i in range(len(string)):
        soma = soma + (i * ord(string[i]))
    return soma

def entradaMensagem():
    #string = input(str("Entre com sua mensagem: "))
    string = entrada.get()
    soma = conta (string)
    #print("Checksum: ",soma)
    lb['text'] = 'Checksum: ',soma
    
    
def validarMensagem():
    #stringValida = input(str("Entre com sua mensagem para verificacao: "))
    #somaValida = int(input("Digite o checksum: "))
    stringValida = entradaMsg.get()
    somaValida = int(entradaChecksum.get())
    
    soma_aux = conta(stringValida) #stringValida
    if somaValida != soma_aux:
        #print("Messagem diferentes")
        lb1['text'] = 'Mensagem diferente'
    else:
        #print("Messagem iguais")
        lb1['text'] = 'Mensagem igual'

def sair():
        print ("Saindo ...")
        sys.exit(0)
        #janela.main_quit() 



janela = Tk() #Instancia uma janela
janela.title("Calcular Checksum")
janela.geometry("200x200") 

    #Botão De calcular cchecksum
#frame1 = Frame(janela) #Cria um frame na janela
#frame1.pack() #Exibe o frame
entrada = Entry(janela)
entrada.pack()
botao = Button(janela, text = "Calcular", command = entradaMensagem) 
botao['width'] = 10 #Define a largura do botão
#botao.bind("", entradaMensagem) #Cria um event dando uma ação ao botão
botao.pack() #Exibe oo botão
    #
    #Botão de validar mensagem
entradaMsg = Entry(janela)
entradaMsg.pack()
entradaChecksum = Entry(janela)
entradaChecksum.pack()
botaoValidar = Button(janela, text = "Validar Mensagem", command = validarMensagem) 
botaoValidar['width'] = 50
botaoValidar.pack()
    #

lb = Label(janela, text='Checksum')
lb.pack()
lb1 = Label(janela, text='Validação')
lb1.pack()

janela.mainloop() #Loop da janela principal
