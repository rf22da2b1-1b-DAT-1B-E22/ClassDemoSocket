from socket import *
import threading

# metode
def handleOneClient(connectionSocket, address):
    print ('Adresse ', addr)

    data = csock.recv(2048)
    sentence = data.decode()
    upperCaseSentence = sentence.upper()

    datatilbage = upperCaseSentence.encode()
    connectionSocket.send(datatilbage)

    connectionSocket.close()
 

# Sætter nogle variable 
serverport = 7

serverSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM => TCP
serverSocket.bind(('',serverport))
serverSocket.listen(1)
print ('server is ready to work for you')

while 1:
    csock, addr = serverSocket.accept() #venter hårdt på der er en klient der kobler op til serveren
    threading.Thread(target=handleOneClient, args=(csock,addr)).start()
    