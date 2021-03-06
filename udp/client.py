from typing import NamedTuple
import socket
from datetime import datetime
from enum import Enum
import zlib

#UDP_IP = "127.0.0.1"
UDP_IP = "192.168.0.2"
UDP_PORT = 5005


class PacketType(Enum):
    quick_pack = 1
    normal_pack = 2
    req_frame_num = 3
    ack_pack = 4


class Packet(NamedTuple):
    p_type: PacketType
    flag: bin
    id: bin


class PacketNormal(NamedTuple):
    packet: Packet
    num_can_frames: int
    f_num: int
    execute_time: datetime.time
    length: int
    can_frame: str
    crc: int


class PacketQuick(NamedTuple):
    packet: Packet
    f_num: bin
    execute_time: datetime
    length: bin
    can_frame: bin
    crc: bin


class ReqFrameNum(NamedTuple):
    packet: Packet
    f_num: int


class AckPacket(NamedTuple):
    packet: Packet


def send_quick_packet():
    print("Quick packet process")
    packet_type1 = PacketType(2)
    packet1 = Packet(packet_type1, bytearray(b'\x00\xFF'), bytearray(b'\x00\x01'))
    quick_packet1 = PacketQuick(packet1, bytearray(b'\x00\x00'), datetime.now(), bytearray(b'\x00\x08'),
                                bytearray(b'\xCA\x08\x01\x02\x03\x04\x05\x06\x07\x08'), bytearray(b'\x00\x00'))
    message1 = quick_packet1.packet.flag + quick_packet1.packet.id + quick_packet1.f_num + \
               quick_packet1.execute_time.strftime("%H:%M:%S.%f-%b%d%Y").encode("utf-8") + \
               quick_packet1.length + quick_packet1.can_frame + quick_packet1.crc
    data = quick_packet1.packet.flag + quick_packet1.packet.id + quick_packet1.f_num + \
           quick_packet1.execute_time.strftime("%H:%M:%S.%f-%b%d%Y").encode("utf-8") + \
           quick_packet1.length + quick_packet1.can_frame
    checksum = zlib.crc32(data)
    print(checksum)
    data = data + checksum.to_bytes(9, byteorder='little')
    data = bytes(data)
    print(data)
    message1 = bytes(message1)
    print(message1)
    sock.sendto(data, (UDP_IP, UDP_PORT))


def send_normalpacket():
    return



# packet_type = PacketType(2)
# packet = Packet(packet_type, r'A0', b'1')
# quick_packet = PacketQuick(packet, b'0', datetime.now(), b'8', "0A0201CA", b'0')

MESSAGE = "Hello, World!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)
print(int("a0", 16))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
# sock.sendto(bytearray([0x00, 0x01, 0xFF, 0xFF, 0xFF]), (UDP_IP, UDP_PORT))
# sock.sendto(bytearray([0x00, 0x01, 0xFF, 0xFF, 0xFF]) + bytes(MESSAGE, "utf-8")+ bytearray([0xFF]),(UDP_IP, UDP_PORT))

# MESSAGE = (bytes(quick_packet.packet.flag, "utf-8") + bytes(quick_packet.packet.id, "utf-8") +
#           bytes(quick_packet.f_num, "utf-8") +
#           bytes(quick_packet.execute_time.strftime("%H:%M:%S.%f - %b %d %Y"), "utf-8") +
#           bytes(quick_packet.length, "utf-8") + bytes(quick_packet.can_frame, "utf-8") +
#           bytes(quick_packet.crc, "utf-8"))

# MESSAGE = quick_packet.packet.flag + quick_packet.packet.id + quick_packet.f_num + \
#          quick_packet.execute_time.strftime("%H:%M:%S.%f - %b %d %Y") + quick_packet.length + \
#          quick_packet.can_frame + quick_packet.crc

print(MESSAGE)
# sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
# sock.sendto(bytes(quick_packet.packet.flag, "utf-8") + bytes(quick_packet.packet.id) + bytes(quick_packet.f_num) +
#            bytes(quick_packet.execute_time.strftime("%H:%M:%S.%f-%b%d%Y"), "utf-8") + bytes(quick_packet.length) +
#            bytes(quick_packet.can_frame, "utf-8") + bytes(quick_packet.crc), (UDP_IP, UDP_PORT))
print("From MAC     ")
empty_bytes = bytes(4)
print(type(empty_bytes))
print(empty_bytes)
# Cast bytes to bytearray
mutable_bytes = bytearray(b'\x00\x0F')

# Bytearray allows modification
mutable_bytes[0] = 255
mutable_bytes.append(255)
print(mutable_bytes)

# Cast bytearray back to bytes
immutable_bytes = bytes(mutable_bytes)
print(immutable_bytes)

menu = input("Enter 1 to continue or 0 to exit: ")
while int(menu) != 0:
    print("&&&&&&&& CAN Test Menu $$$$$$$$$")
    print("1- Send Quick packet")
    print("2- Send Normal Packet")
    print("0 - Exit")
    if int(menu) == 1:
        send_quick_packet()
    elif int(menu) == 2:
        send_normalpacket()
    else:
        menu = 0
    menu = input("Enter 1 to continue or 0 to exit: ")
