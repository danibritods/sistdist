from tkinter import *
from tkinter.ttk import *
import tkinter.font as font
import socket
import _thread as thread

class ChatClient(Frame):
  
  def __init__(self, root):
    Frame.__init__(self, root)
    self.root = root
    self.gui()

    self.serverSoc = None
    self.serverStatus = 0
    self.buffsize = 1024
    self.allClients = {}
    self.counter = 0
  
  def gui(self):

    self.root.title("Chat APP P2P - Sistemas Distribuidos")
    ScreenSizeX = self.root.winfo_screenwidth()
    ScreenSizeY = self.root.winfo_screenheight()
    self.FrameSizeX  = 1240
    self.FrameSizeY  = 680
    FramePosX   = (ScreenSizeX - self.FrameSizeX)/2
    FramePosY   = (ScreenSizeY - self.FrameSizeY)/2
    self.root.geometry("%sx%s+400+300" % (self.FrameSizeX,self.FrameSizeY))
    self.root.resizable(width=False, height=False)
    self.root.configure(bg='#363636')
    
    padX = 20
    padY = 20
    s = Style()
    s.configure('My.TFrame', background='#363636')

    parentFrame = Frame(self.root, style='My.TFrame')
    parentFrame.grid(padx=padX, pady=padY, stick=E+W+N+S)
    myFont = font.Font(family='Courier', size=15, weight='bold')

    ipGroup = Frame(parentFrame, style='My.TFrame')
    serverLabel = Label(ipGroup, text="Definir servidor: ")
    serverLabel['font']=myFont
    self.nameVar = StringVar()
    self.nameVar.set("ServerName")
    nameField = Entry(ipGroup, width=10, textvariable=self.nameVar)
    self.serverIPVar = StringVar()
    self.serverIPVar.set("xx.xx.xx.xxx")
    serverIPField = Entry(ipGroup, width=15, textvariable=self.serverIPVar)
    self.serverPortVar = StringVar()
    self.serverPortVar.set("xxxx")
    serverPortField = Entry(ipGroup, width=5, textvariable=self.serverPortVar)
    serverSetButton = Button(ipGroup, text="Definir", width=10, command=self.acaoDefinirServidor)
    addClientLabel = Label(ipGroup, text="Adicionar amigo: ")
    addClientLabel['font']=myFont
    self.clientIPVar = StringVar()
    self.clientIPVar.set("xx.xx.xx.xxx")
    clientIPField = Entry(ipGroup, width=15, textvariable=self.clientIPVar)
    self.clientPortVar = StringVar()
    self.clientPortVar.set("xxxx")
    clientPortField = Entry(ipGroup, width=5, textvariable=self.clientPortVar)
    clientSetButton = Button(ipGroup, text="Adicionar", width=10, command=self.acaoAdicionarCliente)
    serverLabel.grid(row=1, column=0,padx=10)
    nameField.grid(row=1, column=1)
    serverIPField.grid(row=1, column=2)
    serverPortField.grid(row=1, column=3)
    serverSetButton.grid(row=1, column=4, padx=5, pady=20)
    addClientLabel.grid(row=0, column=0)
    clientIPField.grid(row=0, column=2)
    clientPortField.grid(row=0, column=3)
    clientSetButton.grid(row=0, column=4, padx=5)

    stepByStep1 = Label(parentFrame, text="Primeiro, defina o seu servidor servidor (todos integrantes precisam seguir esse passo)")
    stepByStep2 = Label(parentFrame, text="Segundo, coloque o ip de quem voce quer comunicar na opção de 'adicionar amigo' ")
    stepByStep3 = Label(parentFrame, text="Terceiro, envie a mensagem e seja feliz!")
    stepByStep1.grid(row=2, column=0)
    stepByStep2.grid(row=3, column=0)
    stepByStep3.grid(row=4, column=0)
    
    readChatGroup = Frame(parentFrame, style='My.TFrame')
    self.receivedChats = Text(readChatGroup, bg="#87CEFA", width=60, height=30, state=DISABLED)
    self.friends = Listbox(readChatGroup, bg="#87CEFA", width=30, height=30)
    self.receivedChats.grid(row=0, column=0, sticky=W+N+S, padx = (0,10))
    self.friends.grid(row=0, column=1, sticky=E+N+S)

    writeChatGroup = Frame(parentFrame, style='My.TFrame')
    self.chatVar = StringVar()
    self.chatField = Entry(writeChatGroup, width=80, textvariable=self.chatVar)
    sendChatButton = Button(writeChatGroup, text="Send", width=10, command=self.acaoEnviarMensagem)
    self.chatField.grid(row=0, column=0, sticky=W)
    sendChatButton.grid(row=0, column=1, padx=5)

    self.statusLabel = Label(parentFrame)

    bottomLabel = Label(parentFrame, text="Grupo: Daniel Brito, Joao Vitor Fernandes e Joao Vittor Pinto")
    
    ipGroup.grid(row=0, column=0)
    readChatGroup.grid(row=0, column=1)
    writeChatGroup.grid(row=1, column=1, pady=10)
    self.statusLabel.grid(row=5, column=0,pady=10)
    bottomLabel.grid(row=6, column=0, pady=10)
    
  def acaoDefinirServidor(self):
    if self.serverSoc != None:
        self.serverSoc.close()
        self.serverSoc = None
        self.serverStatus = 0
    serveraddr = (self.serverIPVar.get().replace(' ',''), int(self.serverPortVar.get().replace(' ','')))
    try:
        self.serverSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSoc.bind(serveraddr)
        self.serverSoc.listen(5)
        self.setStatus("Servidor listado em %s:%s" % serveraddr)
        thread.start_new_thread(self.listaClientes,())
        self.serverStatus = 1
        self.name = self.nameVar.get().replace(' ','')
        if self.name == '':
            self.name = "%s:%s" % serveraddr
    except:
        self.setStatus("Deu erro na preparacao do servidor!")
    
  def listaClientes(self):
    while 1:
      clientsoc, clientaddr = self.serverSoc.accept()
      self.setStatus("Cliente conectado de %s:%s" % clientaddr)
      self.adicionarCliente(clientsoc, clientaddr)
      thread.start_new_thread(self.gerenciadorMensagensCliente, (clientsoc, clientaddr))
    self.serverSoc.close()
  
  def acaoAdicionarCliente(self):
    if self.serverStatus == 0:
      self.setStatus("Primeiro defina o servidor!")
      return
    clientaddr = (self.clientIPVar.get().replace(' ',''), int(self.clientPortVar.get().replace(' ','')))
    try:
        clientsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsoc.connect(clientaddr)
        self.setStatus("Connected to client on %s:%s" % clientaddr)
        self.adicionarCliente(clientsoc, clientaddr)
        thread.start_new_thread(self.gerenciadorMensagensCliente, (clientsoc, clientaddr))
    except:
        self.setStatus("Erro em tentar conectar ao amigo")

  def gerenciadorMensagensCliente(self, clientsoc, clientaddr):
    while 1:
      try:
        data = clientsoc.recv(self.buffsize)
        if not data:
            break
        data.decode()

        self.adicionarChat("%s:%s" % clientaddr, data.decode())
      except:
          break
    #self.removerCliente(clientsoc, clientaddr)
    #clientsoc.close()
    #self.setStatus("Client disconnected from %s:%s" % clientaddr)
  
  def acaoEnviarMensagem(self):
    if self.serverStatus == 0:
      self.setStatus("Primeiro defina o servidor!")
      return
    #msg = self.chatVar.get().replace(' ','')
    if msg == '':
        return
    self.adicionarChat("Voce", msg)

    for client in self.allClients.keys():
      client.send(msg.encode())
  
  def adicionarChat(self, client, msg):
    self.receivedChats.config(state=NORMAL)
    self.receivedChats.insert("end",client+": "+msg+"\n")
    self.receivedChats.config(state=DISABLED)
  
  def adicionarCliente(self, clientsoc, clientaddr):
    self.allClients[clientsoc]=self.counter
    self.counter += 1
    self.friends.insert(self.counter,"%s:%s" % clientaddr)
  
  def removerCliente(self, clientsoc, clientaddr):
      print (self.allClients)
      self.friends.delete(self.allClients[clientsoc])
      del self.allClients[clientsoc]
      print (self.allClients)
  
  def setStatus(self, msg):
    self.statusLabel.config(text=msg)
    print (msg)
      
def main():  
  root = Tk()
  app = ChatClient(root)
  root.mainloop()  

if __name__ == '__main__':
  main()  