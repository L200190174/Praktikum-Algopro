import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50001))
s.listen(5)
print "program komunikasi tentang data diri"
data = ""
kamus = {"nama":"Labib Majid",
         "NIM":"L200190174",
         "angkatan":"2019",
         "keluar":"siap!"}
while data.lower() != "keluar":
    komm, addr = s.accept()
    while data.lower() != "keluar":
        data = komm.recv(1024)
        print "printah: ", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("maaf, perintah ini tidak dimengerti")
