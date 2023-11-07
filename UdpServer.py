from socket import *
import threading

RECEIVING_PORT = 12007
BUFFER_SIZE = 1024


def do_client(sock):
    buffer, clientAdr = sock.recvfrom(BUFFER_SIZE)
    text = str(buffer, 'utf-8')
    print (text)
    sock.sendto(bytes(text,'utf-8'), clientAdr)






server = socket(AF_INET, SOCK_DGRAM)
server.bind( ('', RECEIVING_PORT ) )  # ip adr, port

while True:
    thread = threading.Thread( target = do_client(server) )
    thread.start()