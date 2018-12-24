import socket               

def Main():
    s = socket.socket()        
    host = '192.168.1.100:'# server ip'si
    port = 9999 
    s.connect((host, port))
    mesaj=s.recv(1024)
    print mesaj
    s.close()

if __name__ == '__main__':
    Main()

