import socket
from PIL import Image, ImageDraw
import qrtools

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'goblok.tech'
port = 2323
qr = qrtools.QR()
s.connect((host, port))
for i in range(21):
    pesan=""
    msg = s.recv(3000)
    print(msg)
    msgs = msg.split("\n")
    for baris in msgs:
        if baris.strip() <> "Bantu aku selesaikan soal di bawah ini dong :" and baris.strip() <> "":
            pesan +=baris+"\n"
    pesan=pesan[:len(pesan)-2]
    im = Image.new('RGB', (1000, 1000),color=(255,255,255))
    draw = ImageDraw.Draw(im)
    pesans = pesan.split("\n")
    y = 10
    for baris in pesans:
        x=0
        for ch in baris:
            if ch == "U":
                draw.rectangle(((15*x,y*30),(15*x+15,y*30+30)), fill=(0,0,0))
            x=x+1
        y=y+1
    im.save('qr.png')
    if i<21:
        qr.decode("qr.png")
        solve = qr.data
        print(solve)
        solv = eval(solve)
        print(solv)
        s.sendall(str(solv)+"\n")
    else:
        s.sendall("\n")
s.close()
