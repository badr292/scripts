import socket
import ntcan

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
hunt_flag = 0
while True:
    data, addr = sock.recvfrom(1024)
    # data,addr = server_socket.recvfrom(1024)

    while data[hunt_flag] != b'\x00\xFF' and hunt_flag != 1024:
        hunt_flag+=1

    if hunt_flag == 1024:
       continue
    if data[hunt_flag] == b'\x00\xFF':
        print("Receive Quick packet")
    nOb = 0
    # def utf8len(data):
    nOb = len(data)
    lenght = int(data[0])
    if lenght != nOb:
        print("Message is not correct!")
    print("received message:", data)
    print("received message:", data[0])
    print("received message:", nOb)
