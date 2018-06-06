# -*- coding: utf-8 -*-
# Author : maxsen
# start time: 2018-5-22

import socket

# 1 byte as a unit
# every time send 1 byte

class MyReliableUDP:
    ip = None
    port = None
    # solid length for slidewindow ,when the content of slidewindow has been completed send ,then it refill again
    SlideWindow = 64
    SlideWindowStart = 0
    SlideWindowEnd = 64
    SendQue = [ 0 for i in range(1023)]
    RecvIdQue = [ -1 for i in range(127)]
    RecvId = None
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        pass

    def initialSendQueue():
        pass

    def setSlideWindow(self):
        if self.SlideWindow

        pass



    def checkState(self,stride):
        # check if there are still no send packet.
        # the slide window is a changeble and gradully mining entity size
        # 2018.5.29 define the size of slidewindow is solid


        # fake code
        set time out
        while not recv out:
            packet = self.mySocketRecv()
            RecvId,RecvContent = parsePacket(packet)

            update the SendQue
















        if self.setSlideWindow() == 0:
            return 0

        SendProbe = self.SlideWindowStart
        #Stride = 0
        while SendProbe != self.SlideWindowEnd:
            #Stride += 1
            if self.SendQue[SendProbe] == 0:
                # we should move the font of slide window ,if front of packets has been send.
                self.SlideWindowStart += Stride
                self.SlideWindow = self.SlideWindowEnd - self.SlideWindowStart

                return SendProbe
            SendProbe += 1

        # can not update the font of slidewindow , when send it out . because ,it may failed to send.
        return 0
        pass

    def mySocketSend(self,SendId):
        pass



    def send(self,str):
        # first , send all the sendque of packet at one time .
        # then , according to the recved packet to update the sendque.
        # then ,send the failed packet again.

        initialSendQueue()

        # fake code 
        stride = 0
        while stride < str.length():
            for SendId in range(self.SlideWindowStart,self.SlideWindowEnd):
                if SendId+stride < str.length()：
                    self.mySocketSend(SendId+stride,str[SendId+stride])
                self.mySocketSend(SendId+stride,'ENDFOF')

            # check time out ,then send unreached packet
            # return a unreached packet list
            ReSendIdList = self.checkState(stride)
            while ReSendIdList is not None:
                for SendId in ReSendIdList:
                    if SendId+stride < str.length()：
                        self.mySocketSend(SendId+stride,str[SendId+stride])
                    self.mySocketSend(SendId+stride,'ENDFOF')
            
                ReSendIdList = self.checkState(stride)

            stride += self.SlideWindowEnd - self.SlideWindowStart

        pass

    def initialRecvQueue():
        pass
    def verifyPacket():
        pass

    def recv(self,buf):
        initialRecvQueue()

        # fake code
        while not recv out:
            packet = self.mySocketRecv()
            RecvId,RecvContent = parsePacket(packet)

            #fake code
            if RecvId without send :
                fill in RecvId
                self.verifyPacket(RecvId)

            buf+=RecvContent


        return buf
        pass

