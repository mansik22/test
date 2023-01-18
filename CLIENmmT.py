import socket

udp_ip_address="192.168.1.30"
UDP_PORT_NO=652
MESSAGE="mansi"
clientSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

clientSock.sendto((MESSAGE.encode()),(udp_ip_address,UDP_PORT_NO))
