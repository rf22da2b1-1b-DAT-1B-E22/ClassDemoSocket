#
# TCP Server efter bogen + threading + Add protokol
#

from socket import *
from threading import *
# konstant
serverPort = 12001


# metode til at håndtere een client
def handleClient(clientSocket, addr):
    sentence = clientSocket.recv(2048).decode()     # modetager op til 2048 tegn i en sætning og laver byte om til tekst(decode)
    # sentance har formattet add tal tal
    splittetText = sentence.split()                 # splitter sentence på blanktegn/mellemrum/space
    Text=''
    if (splittetText[0].lower() == 'add'):      # find de to tal og læg dem sammen
        talx = int (splittetText[1])
        taly = int (splittetText[2])
        Text = f'{talx} +  {taly} = {(talx+taly)}'
    else:
        Text = f'understøtter ikke metoden {splittetText[0]}'

    clientSocket.send(Text.encode())                #  sender tekst tilbage til clienten og laver tekst om til byte (encode)
    clientSocket.close()                            # lukker forbindelse til klienten


#
# Main program
#
# opretter server objekt
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))              # lader serveren køre på denne maskiner og på port = serverPort
serverSocket.listen(1)                          # sætter serverne reelt til at starte alias lytte efter clienter
print('The server is up and runing on port', serverSocket)

#server loop
while True:
    connectionSocket, addr = serverSocket.accept()
    print('Forbundet til en Client fra adressen', addr)
    Thread(target=handleClient, args=(connectionSocket, addr)).start()

