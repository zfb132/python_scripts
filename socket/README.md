# socket
Establish a simple TCP connection, send and receive data between the client and the server  

## server-module.py
Listen TCP connection on the certain ip and port  
Receive data from client and show them
**Note**:  
block the main thread to ensure that the server can be alive all the time

## client-module.py
Establish a TCP connection and send data  
**Note**:  
If it is a gui project such as pyqt, it should be set to non-blocking, otherwise it can be set as blocking thread
