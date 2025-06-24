import socket

host = "127.0.0.1"
port = 12345
localeGonderilecekSorgu  = "pau.edu.tr"
byte = localeGonderilecekSorgu.encode("utf-8")

istemciSoketi = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("İstemci soketi oluşturuldu.")

Buffer_Boyutu = 1024
istemciSoketi.connect((host,port))
print("İstemci soketine bağlanıldı.")

print("Dns sorgusu:",localeGonderilecekSorgu)
istemciSoketi.send(byte)
print("Sorgu Local'e başarılı bir şekilde gönderildi.")
print("Local'den Cevap belleniyor...")
localdenGelenCevap = istemciSoketi.recv(Buffer_Boyutu)
print("Local'den gelen cevap:",localdenGelenCevap.decode())

print("Local'den cevap geldi soket kapatılıyor...")

istemciSoketi.close()