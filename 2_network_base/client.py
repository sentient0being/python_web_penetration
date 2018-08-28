'''
#tcp client:
import socket

target_host="127.0.0.1"
target_port=9999

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))

client.send("GET /HTTP/1.1\r\nHost:baidu.com\r\n\r\n")
response=client.recv(1024)

print response
'''



'''
#udp client 
import socket 

target_host="127.0.0.1"
target_port=9999

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#client.connect((target_host,target_port))

client.sendto("udp is so fast",(target_host,target_port))
data,addr=client.recvfrom(1024)
print data
'''