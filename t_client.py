import socket
import test as myudp

def realClient():
    ip = '127.0.0.1'
    port = 8081
    ip_port = (ip,port)
    c_ip_port = (ip,8082)

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
    sock.bind(c_ip_port)

    sock.sendto('hello',ip_port)

    data = sock.recv(1024)
    print data

def translate_file(path):
    f = open(path,'rb')
    myudp.mySend(f.read())
    f.close()

def myClient():
    myudp._init('127.0.0.1',8002,'client')

    data = 'sssssssssssssssdddddddddddddddddddfffffffff657586858475475858ffffssssssss'
    myudp.mySend(data)

    # translate_file('C:\\reverse.pdf')

if __name__ == '__main__':
    myClient()
