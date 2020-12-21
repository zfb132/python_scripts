#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: 'zfb'
# time: 2020-10-26 20:23
# ref_url: https://www.runoob.com/python/python-socket.html

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import json

def client_func(param):
    '''client program

    The client establishes a TCP connection and sends data

    
    Note: This code does not receive replying data from server, but it can be modified to do this
    '''
    print("client starts to send data.")
    host = '127.0.0.1'
    port = 8000
    # connection-oriented TCP  (SOCK_STREAM)
    # transaction-oriented UDP (SOCK_DGRAM)
    client = socket(AF_INET, SOCK_STREAM)
    # establish a connection that connects to the host port
    client.connect((host, port))
    msg = json.dumps(param)
    # send a message: the type of data should be bytes in python3
    client.send(msg.encode('utf-8'))
    client.close()
    print("client sent data successfully!")

def on_btn_clicked(arg):
    '''open a thread to execute socket connection

    establish a TCP connection with the server, close immediately after sending data, and block the main thread (to prevent this thread from exiting because the main thread exits)

    for the pyqt project, it should be set as a non-blocking process (because the main thread is a gui thread, it cannot be blocked and will not automatically exit)
    '''
    print("on_btn_clicked started.")
    import datetime
    param = {
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%s"),
        "file_name": arg,
        "os_version": "Linux LAPTOP-DFPGS13G 4.19.104-microsoft-standard",
        # test chinese character
        "note": "我是客户端"
    }
    thread_data_process = Thread(target=client_func, args=(param, ))
    # blocking thread (if it is a gui project such as pyqt, it should be set to non-blocking)
    thread_data_process.setDaemon(False)
    thread_data_process.start()
    print("on_btn_clicked finished!")

if __name__ == "__main__":
    print("program started")
    import sys
    # argv[0] is the script file name
    on_btn_clicked(sys.argv[0])
    print("program finished!")