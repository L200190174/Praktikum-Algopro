import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50002))
s.listen(5)
print "server siap"
perintah =''
a=0
t=0
s=0,5 #setengah
while perintah !='keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        item = komm.recv(1024).lower().split("=")
        perintah = item [0]
        if perintah == 'keluar':
            komm.send('done')
            s.close()
            break
        print "pesan",perintah
        if len(item)==2:
            if perintah =='alas':
                a=int(item[1])
                komm.send('alas disimpan')
            elif perintah =='tinggi':
                a=int(item[1])
                komm.send('tinggi disimpan')
            elif perintah =='setengah':
                a=int(item[1])
                komm.send('setengah disimpan')
            else:
                komm.send(response)
        elif perintah == 'hitung':
            L=float(s*a*t)
            response ='luas segitiga dengan setengah {} tinggi {} adalah {}'.format(s,a,t,L)
            komm.send(response)
        else:
            komm.send('pesan tidak diketahui')
            
