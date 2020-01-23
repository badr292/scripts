from typing import NamedTuple
import socket
from datetime import datetime
from enum import Enum

UDP_IP = "127.0.0.1"
UDP_PORT = 5005


class PacketType(Enum):
    normal_pack = 1
    quick_pack = 2
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


packet_type = PacketType(2)
packet = Packet(packet_type, r'A0', b'0')
quick_packet = PacketQuick(packet, b'0', datetime.now(), b'8', "0A0201CA", b'0')

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
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
sock.sendto(bytes(quick_packet.packet.flag, "utf-8") + bytes(quick_packet.packet.id) + bytes(quick_packet.f_num) +
            bytes(quick_packet.execute_time.strftime("%H:%M:%S.%f-%b%d%Y"), "utf-8") + bytes(quick_packet.length) +
            bytes(quick_packet.can_frame, "utf-8") + bytes(quick_packet.crc), (UDP_IP, UDP_PORT))
print("From MAC  ")
