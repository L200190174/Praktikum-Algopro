import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50009))
print "program komunikasi tentang server"
while pesan.lower() != "quit":
    pesan = raw_input("command: ")
    s.send(pesan)
    if pesan.lower() == "quit":
        s.close()
        break
    elif pesan.lower() != "quit":
        response = s.recv(1025)
        print "response :", response
s.close()
