import socket
import time
# author : maxsen
# provide a unify interface:
# for user , in the user level , provide mySend() and myRecv() to send and receive data.
# for interface , below user level , provide rlSend() and rlRecv() for mySend and myRecv to use.
# they will return a complete buffer to them.
# EOF only be send lonely , else make a error
# sender dont send EOF , if it dosent receive the reciver verify packet fully

sock = None
stride = 9
s_ip_port = ('127.0.0.1',8001)
c_ip_port = ('127.0.0.1',8002)
position = None

def _init(ip,port,role):
    global sock,s_ip_port,c_ip_port,position
    position = role
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
    if role == 'server':
        s_ip_port = (ip,port)
        sock.bind(s_ip_port)

    elif role == 'client':
        c_ip_port = (ip,port)
        sock.bind(c_ip_port)

def _send(cc):
    global sock,s_ip_port,c_ip_port,position
    if position == 'server':
        sock.sendto(cc,c_ip_port)
    elif position == 'client':
        sock.sendto(cc,s_ip_port)
    else:
        print 'send error'


def _recv():
    global sock,s_ip_port,c_ip_port,position
    data = sock.recv(1024)
    return data

def rlSend(content,content_len):
    VfQue = [ 0 for i in range(content_len)]

    # 1. send out first time
    for i in range(content_len):
        # format of the packet , : bit + num + content
        _send(str(1)+str(i)+content[i])

    # 2. set check receive packet , if verify packet receive full , then return
    recv_count = 0
    # while recv_count < content_len:
    while 0 in VfQue:
        start_time = time.time()
        end_time = start_time
        # 3. set time out , check verify packet from receiver.
        while end_time - start_time < 60:
            packet = _recv()
            if len(packet)>=2:
                bit = int(packet[0])
                if bit == 1:
                    num = int(packet[1])
                    VfQue[num] = 1
            recv_count += 1
            # if recv_count == content_len :
            if 0 not in VfQue:
                return
            end_time = time.time()
        # 4. when time is out , then send unreceived-verify packet again
        for i in range(content_len):
            if VfQue[i] == 0:
                _send(str(1)+str(i)+content[i])

    return

def rlRecv():
    pass

def mySend(buf):
    # split string to solid lenth , every time transparent string and length tow parameters to rlSend.
    # when handle over , it return.
    global stride
    itr = int(0)
    len_buf = len(buf)
    while itr < len_buf:
        if itr+stride < len_buf:
            content = buf[itr:itr+stride]
        else:
            content = buf[itr:-1]
        # here , should have a debug to verify the content length
        c_len  = len(content)
        rlSend(content,c_len)
        itr += stride

    # send the EOF packet
    _send('0')
    pass

def myRecv():
    # 1. check whether it is EOF packet , then keep on receive
    # the size of window should be solid , because for send it rely on content_len , but receive dont know the len
    buf = ''
    data = _recv()
    # EOF bit is 0
    while int(data[0]) != 0:
        # 2. when receive num is not satisfied , then keep on ; else , send below to buffer for user
        sign = 0
        recv_count = 0
        RecvPacket = ['' for i in range(stride)]
        # while recv_count < stride:
        # only check wheather have empty position , dont check count
        while '' in RecvPacket:
            num = int(data[1])
            RecvPacket[num] = data[2]
            # verify packet
            _send(str(1)+str(num))
            recv_count += 1

            data = _recv()
            if int(data[0]) == 0:
                sign = 1
                break
        # 3. send full packet to user buffer
        buf += ''.join(RecvPacket)
        if sign == 1:
            break

    return buf


