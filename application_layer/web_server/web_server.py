# import socket module
from socket import *
import sys  # In order to terminate the program

# Variables
HOST = ""
PORT = 50007

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

while True:
    # Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        # Send one HTTP header line into socket
        connectionSocket.send(
            b"HTTP/1.1 200 OK\r\n"
        )  # \r\n is an additional empty line meaning end of header
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    # Send response message for file not found
    # Fill in start
    # Fill in end
    # Close client socket
    # Fill in start
    # Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
