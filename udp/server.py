import socket 
UDP_IP = "127.0.0.1"
UDP_PORT = 5005 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
   
while True:
	data,addr = sock.recvfrom(1024)
	#data,addr = server_socket.recvfrom(1024)
	nOb = 0
	#def utf8len(data):
	nOb= len(data)
	lenght= int(data[0]) 
	if lenght != nOb:
		print ("Message is not correct!")
	print ("received message:", data)
	print ("received message:", data[0])
	print ("received message:", nOb)