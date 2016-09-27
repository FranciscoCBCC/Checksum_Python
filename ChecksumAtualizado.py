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
    mostraChecksum['text'] = 'Checksum: ',soma
    
    
def validarMensagem():
    #stringValida = input(str("Entre com sua mensagem para verificacao: "))
    #somaValida = int(input("Digite o checksum: "))
    stringValida = entradaMsg.get()
    somaValida = int(entradaChecksum.get())
    
    soma_aux = conta(stringValida) #stringValida
    if somaValida != soma_aux:
        #print("Messagem diferentes")
        resultadoValidacao['text'] = 'Mensagens diferentes'
    else:
        #print("Messagem iguais")
        resultadoValidacao['text'] = 'Mensagens iguais'

def sair():
        print ("Saindo ...")
        sys.exit(0)
        #janela.main_quit() 



janela = Tk() #Instancia uma janela
janela.title("Calcular Checksum")
janela.geometry("300x350") 

topo = Label(janela, text='Checksum')
topo["font"] = ("Verdana", "15", "bold")
topo.pack()

    #Botão De calcular checksum
#frame1 = Frame(janela) #Cria um frame na janela
#frame1.pack() #Exibe o frame
tituloCx1 = Label(janela, text='Digite a mensagem para calcular o checksum')
tituloCx1["font"] = ("Verdana", "8", "italic", "bold")
tituloCx1.pack()
entrada = Entry(janela)
entrada["width"]=40
entrada.pack()
botao = Button(janela, text = "Calcular", command = entradaMensagem) 
botao['width'] = 10 #Define a largura do botão
#botao.bind("", entradaMensagem) #Cria um event dando uma ação ao botão
botao.pack() #Exibe o botão
mostraChecksum = Label(janela, text='Checksum')
mostraChecksum["font"] = ("Verdana", "8", "italic", "bold")
mostraChecksum.pack()
espaco = Label(janela, text='___________________________________________________________')
espaco.pack()
    #
    
    #Botão de validar mensagem
tituloCx2 = Label(janela, text='Digite a mensagem para validá-la')
tituloCx2["font"] = ("Verdana", "8", "italic", "bold")
tituloCx2.pack()
entradaMsg = Entry(janela) #Caixa de entrada da mensagem para validar
entradaMsg["width"]=40
entradaMsg.pack()
tituloCx3 = Label(janela, text='Digite o checksum para validar a mensagem')
tituloCx3["font"] = ("Verdana", "8", "italic", "bold")
tituloCx3.pack()
entradaChecksum = Entry(janela) #Caixa de entrada da checksum para validar a mensagem
entradaChecksum.pack()
botaoValidar = Button(janela, text = "Validar Mensagem", command = validarMensagem) 
botaoValidar['width'] = 20
botaoValidar.pack()
    #
resultadoValidacao = Label(janela, text='Resultado da Validação')
resultadoValidacao["font"] = ("Verdana", "8", "italic", "bold")
resultadoValidacao.pack()

espaco1 = Label(janela, text='___________________________________________________________')
espaco1.pack()

alunos = Label(janela, text='Alunos:\nFrancisco Carrera Nascimento Junior\nRenan Thiago da Silva Rosa\nCleidson da Silva Malcher')
alunos["font"] = ("Verdana", "8", "italic", "bold")
alunos.pack()
janela.mainloop() #Loop da janela principal
