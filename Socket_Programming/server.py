import socket
host = ''
port = 5100

storedValue = "Yo, what's up?"

def setupServer():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket has been created..")
    try:
        s.bind((host,port))
    except socket.error as msg:
        print("Error: ",msg)
    print("Socket bind complete")
    return s

def setupConnection():
    s.listen(1) 
    conn,address=s.accept()
    print("Connected to ",address[0],":"+str(address[1]))
    return conn

def GET(storedValue):
    reply = storedValue
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply

def dataTransfer(conn):
    while True:
        data=conn.recv(1024)
        data=data.decode('utf-8')
        dataMessage=data.split(' ',1)
        command =dataMessage[0]
        if command == 'GET':
            reply=GET("Hello")
        elif command == 'REPEAT':
            reply=REPEAT(dataMessage)
        elif command == 'EXIT':
            print("Our client has left us :( ")
            break
        elif command == 'KILL':
            print("Our server is shutting down..")
            s.close()
            break
        else:
            reply="Unknown Command"
        conn.sendall(str.encode(reply))
        print("Data has been sent :) ")
    conn.close()

s=setupServer()
while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        s.close()
        break

