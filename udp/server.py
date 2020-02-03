import socket
import ntcan
import util

#UDP_IP = "127.0.0.1"
UDP_IP = "192.168.0.4"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
hunt_flag = 0

net = 0  # logical CAN Network [0, 255]
RxQS = 2000  # RxQueueSize [0, 10000]
RxTO = 2000  # RxTimeOut in Millisconds
TxQS = 1  # TxQueueSize [0, 10000]
TxTO = 1000  # TxTimeOut in Millseconds
# cifFlags=                              # Flags
cif = ntcan.CIF(net, RxQS, RxTO, TxQS, TxTO)
print(cif)
util.print2lines()

# set baudrate 0 = 1MBaud
# CAN-API-Description
cif.baudrate = 0

# Erzeuge CAN-Messagestruktur
cmsg = ntcan.CMSG()
print(cmsg.msg_lost)
print(cmsg)
# examples for ntcan ----------------------------------------------------------
cif2 = ntcan.CIF(net)
print(cif2)
print(cif2.net)
print(cif2.tx_timeout)
print(cif2.rx_timeout)
print(cif2.features)
util.print2lines()
# set baudrate 0 = 1MBaud
# CAN-API-Description
cif2.baudrate = 0

# Erzeuge CAN-Messagestruktur
cmsg2 = ntcan.CMSG()
print("cmsg lost: %d" % (cmsg2.msg_lost))
print("cmsg2 %s" % (cmsg2))

id = 1
while True:
    data, addr = sock.recvfrom(1024)
    # data,addr = server_socket.recvfrom(1024)
    hunt_flag = 0
    while data[hunt_flag] != 0 and data[hunt_flag+1] != 255 and len(data) - 1 != hunt_flag:
        print(data[hunt_flag])
        hunt_flag += 1

    if hunt_flag == len(data) - 1:
        continue

    cmsg2.canWriteByte(cif2, data[33], data[34], data[35], data[36], data[37], data[38], data[39], data[40], data[41],
                       data[42])
    nOb = 0
    # def utf8len(data):
    nOb = len(data)
    lenght = int(data[0])
    if lenght != nOb:
        print("Message is not correct!")
    print("received message:", data)
    print("received message:", data[0])
    print("received message:", nOb)
