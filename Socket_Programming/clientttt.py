import socket

host = "192.168.29.225"
port = 5100

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while True:
    command = input("Enter your command: ")
    if command =='EXIT':
        s.send(str.encode(command))
        break
    elif command =='KILL':
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print("reply: ",reply.decode('utf-8'))

s.close()
