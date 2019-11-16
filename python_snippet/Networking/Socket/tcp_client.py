import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"  # server address
port = 9999  # server port
s.connect((host, port))
# print s.recv(1024) # dabu: code is wrong place in book
while True:
    message = raw_input("> ")
    r = s.send(message)
    print "send byts: %s" % r
    print s.recv(1024)  # dabu: add code here
    if message == "quit":
        break
s.close()
