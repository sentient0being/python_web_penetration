'''
#tvp server 
import socket
import threading
 
 
bind_ip="127.0.0.1"
bind_port=9999


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*]Listening on %s:%d" % (bind_ip,bind_port)

def handle_client(client_socket):
	request=client_socket.recv(1024)
	print "[*]Recvived:%s" % request
	client_socket.send("ACK!")
	client_socket.close()
while True:
	client,addr=server.accept()
	print "[*]Accepted connection from:%s:%d" % (addr[0],addr[1])
	client_handler=threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
'''




'''
#udp server 
import socket

bind_ip="127.0.0.1"
bind_port=9999

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind((bind_ip,bind_port))
print "[*]Listening on %s:%d" % (bind_ip,bind_port)

data,addr=server.recvfrom(1024)
print "[*]Accept connection from%s:%d" % (addr[0],addr[1])
print "[*]Received:%s" % data
server.sendto("ACK!",(addr[0],addr[1]))
'''