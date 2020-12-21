#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: 'zfb'
# time: 2020-10-26 20:08
# ref_url: https://www.runoob.com/python/python-socket.html

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

import json
import time

def data_process(data):
    print("function data_process is starting process data: {}".format(data))
    tx = json.loads(data)
    for key, value in tx.items():
        print('{}:{}'.format(key, value))
    time.sleep(2)
    print("function data_process ends!")

def server_func():
    '''server program

    The server listens a TCP connection and receives data
    
    Note: This code replies nothing, but it can be modified to implement this feature
    '''
    buff_size = 1024
    host = '127.0.0.1'
    port = 8000
    # connection-oriented TCP  (SOCK_STREAM)
    # transaction-oriented UDP (SOCK_DGRAM)
    server = socket(AF_INET, SOCK_STREAM)
    # bind the ip and port
    server.bind((host, port))
    # start listening: five connections can be queued (not required)
    server.listen(5)
    while True:
        # waiting for connection
        conn, addr = server.accept()
        # print(conn, addr)
        while True:
            try:
                # receiving data
                data = conn.recv(buff_size).decode('utf-8')
                if not data:
                    break
                print('server recive: ', data)
                # start data processing thread
                thread_data_process = Thread(target=data_process, args=(data, ))
                # non-blocking thread
                thread_data_process.setDaemon(True)
                thread_data_process.start()
            except ConnectionResetError as e:
                print('Close a connection that is busy!')
                break
    conn.close()

thread_server = Thread(target=server_func)
# block the main thread to ensure that the server can be alive all the time 
# (to prevent this thread from exiting because the main thread exits)
thread_server.setDaemon(False)
print('start server')
thread_server.start()

print('main thread exits')
