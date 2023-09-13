from socket import *

# Sætter nogle variable 
servername = 'localhost'
serverport = 7

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servername,serverport))

sentence = input('Indtast linje: ')
data = sentence.encode()
clientSocket.send(data)

#modtager svar
datatilbage = clientSocket.recv(2048)
sentenceTilbage = datatilbage.decode()

print ('Modtaget tekst ', sentenceTilbage)
clientSocket.close()