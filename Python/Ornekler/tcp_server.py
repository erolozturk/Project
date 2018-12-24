import socket

s = socket.socket()
host = '192.168.0.105' # server ip'si
port = 9999
s.bind((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  c.send('0xFF 0xFF 0x00 0xE8 0x03 0xE8 0x03')
  c.close()
