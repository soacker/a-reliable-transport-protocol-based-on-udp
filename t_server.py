import socket
import test as myudp

def realServer():
    ip = '127.0.0.1'
    port = 8081
    ip_port = (ip,port)

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
    sock.bind(ip_port)

    data = sock.recv(1024)
    print data
    c_ip_port = (ip,8082)
    sock.sendto('thank you ',c_ip_port)

def myServer():
    myudp._init('127.0.0.1',8001,'server')
    data = myudp.myRecv()
    print data
    pass


if __name__ == '__main__':
    myServer()

