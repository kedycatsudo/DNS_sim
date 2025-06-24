import socket
host = "127.0.0.1"
port = 12346
Buffer_Boyutu = 1024
cevap = " TLD'ye yönlendiriliyor..."
cevapbyte = cevap.encode("utf-8")

try:
    local_soketi = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Local soketi oluşturuldu.")
    local_soketi.bind((host,port))
    print("Socket {} no'lu porta bağlandı".format(port))

    local_soketi.listen(5)
    print("Socket dinleniyor...")
except socket.error as msg:
    print("Hata:",msg)

local , local_addr = local_soketi.accept()
print("Bağlantı talebi oluşturuldu.")
print("Local'den sorgu bekleniyor...")

local_sorgu = local.recv(Buffer_Boyutu)

print("Local'den sorgu geldi." ,local_sorgu.decode())
print("Local'den sorgu alındı ve Buffer bosaldı...")
local.send(cevapbyte)
print("Cevap gönderildi, bağlantı kesildi.")
local.close()
local_soketi.close()
