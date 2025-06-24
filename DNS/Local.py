import socket

host = "127.0.0.1"
client_port = 12345
root_port = 12346
TLD_port = 12349
authoritative_port = 12348
Buffer_Boyutu = 1024

try:
    client_soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Client Soketi oluşturuldu.")
    client_soketi.bind((host,client_port))
    print("Socket {} no'lu porta bağlandı".format(client_port))

    #En fazla 5 bağlantıya izin veriliyor.
    client_soketi.listen(5)
    print("Socket dinleniyor...")
except socket.error as msg:
    print("Hata:",msg)


client,client_addr = client_soketi.accept()
print("Bağlantı talebi oluşturuldu.")
print("İstemciden sorgu bekleniyor...")

client_sorgu = client.recv(Buffer_Boyutu)

print("istemciden sorgu geldi. ", client_sorgu.decode())
print("İStemciden sorgu alındı ve Buffer bosaldı...")
print("ip adresi local'de olmadığı için recursive sorgu başlatılıyor...")

#Root'a giden sorgu

root_soketi = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Root soketi oluşturuldu.")
root_soketi.connect((host,root_port))
print("Root soketine bağlanıldı.")
print("Dns sorgusu:",client_sorgu.decode())
root_soketi.send(client_sorgu)
print("Sorgu Root'a başarılı bir şekilde gönderildi.")
print("Root'dan cevap bekleniyor...")
rootdanGelenCevap = root_soketi.recv(Buffer_Boyutu)
print("Root'dan gelen cevap:", rootdanGelenCevap.decode())
root_soketi.close()

#TLD 'ye giden sorgu

tld_soketi = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("TLD soketi oluşturuldu")
tld_soketi.connect((host, TLD_port))
print("TLD soketine bağlandı.")

print("Dns sorgusu:", client_sorgu.decode())
tld_soketi.send(client_sorgu)
print("Sorgu TLD'ye başarılı bir şekilde gönderildi")
print("TLD'den cevap bekleniyor...")
TLDdenGelenCevap = tld_soketi.recv(Buffer_Boyutu)
print("TLD'den gelen cevap:",TLDdenGelenCevap.decode())
print("TLD'den cevap geldi TLD soketi kapatılıyor...")
tld_soketi.close()

#Authoritive'e giden sorgu

auth_soketi = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Authoritative soketi oluşturuldu.")
auth_soketi.connect((host, authoritative_port))
print("authoritative soketine bağlanıldı.")

print("Dns sorgusu:",client_sorgu.decode())
auth_soketi.send(client_sorgu)
print("Sorgu authoritative'e başarılı bir şekilde gönderildi.")
print("Authoritative'den cevap bekleniyor...")
authGelenCevap = auth_soketi.recv(Buffer_Boyutu)
print("Authoritative'den gelen cevap:",authGelenCevap.decode())
print("Authoritative'den cevap geldi authoritative soketi kapatılıyor...")
auth_soketi.close()

#Client'e giden cevap

client.send(authGelenCevap)
print("Cevap Client'e gönderildi.")
print("baglantı kesildi.")
client.close()
client_soketi.close()
