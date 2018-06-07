# a-reliable-transport-protocol-based-on-udp
a reliable transport protocol based on udp


    I achieved a reliable protocol based on udp. I provide a unifiyed interface as mySend
and myRecv function for user. they are rely on rlSend and rlRecv , which were made with
socket. 
    It is a simple demo for using. the format of packet is defined as 'len + num + content'.
At this time it only support one byte translate . And it can update later for lots of bytes
every time . 
    I design a solid window to send and recv . for the receiver , it will send verify packet
when it received the sender's packet immediatly . for the sender , it will set a time
out to send unverify packet again.
    example:  t_client.py is a client node , and t_server.py is a server node. the library
are made in test.py
