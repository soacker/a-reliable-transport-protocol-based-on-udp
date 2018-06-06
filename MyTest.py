# -*- coding: utf-8 -*-
import my_reliable_udp


def main(ip,port):
    mp = my_reliable_udp.MyReliableUDP(ip, port)
    while 1:
        str = raw_input()
        if str != '':
            mp.send(str)
        r_str = mp.recv()
        while r_str:
            print r_str
            r_str = mp.recv()


    pass



if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 80
    main(ip,port)

