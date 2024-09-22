# socket.socket() in Python is a method from the socket module used to create a new socket object.
# A socket acts as an endpoint for sending and receiving data between two machines over a network.
# The socket() function initializes a new socket, and it requires specifying the address family, socket type, and protocol (proto OR Protocol: Usually set to 0 to automatically select the protocol for the given family and type.).

# AF_INET is an (A)ddress (F)amily that is used to designate the type of addresses that your socket can communicate with 
# (in this case, Internet Protocol v4 addresses). When you create a socket, you have to specify its address family
# and then you can only use addresses of that type with the socket.

# TCP (SOCK_STREAM) is a connection-based protocol. 
# The connection is established and the two parties have a conversation
# until the connection is terminated by one of the parties or by a network error.
# TCP almost always uses (SOCK_STREAM) and UDP uses (SOCK_DGRAM).

# bind() is used to bind or (connect) the socket to a specific address and port on the host machine.
# This is done so that the socket can listen for incoming connection requests on that specific address and port.
# For example, in a server application, the socket can be bound to the localhost (localhost is your own PC, don't try to hack it XD) address (127.0. 0.1 -> this is the localhost ip address) and port 8000.

# .listen() enables a server to accept connections from other devices. It makes the server a “listening” socket

# .accept() blocks execution and waits for incoming connection. When a client connects, it returns a new socket object representing the connection and a tuple holding the address of the client. 
# The tuple will contain (host, port) for IPv4 connections
# One thing that’s imperative to understand is that you now have a new socket object from .accept() it's important because it’s the socket that you’ll use to communicate with the client.
# It’s not the same as the listening socket that the server is using to accept new connections (keep that in mind)

# .connect() is used on the client side to connect to the server on specific ip address and port?

import socket

HOST_IP = "192.168.1.28" # my PC static ip address

PORT = 443 # the port that allows devices to share data

BUFFER_SIZE = 4096 # receive 4096 bytes each time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST_IP, PORT))

server_socket.listen(1) # currently accepting one connection "more on the way"

def start_server():


    print(f"Server started on HOST_IP on port number {PORT}. Waiting for client connection")

    conn, adrr = server_socket.accept()

    print(f"Connection established with HOST_IP")
    
    while True:

        data = conn.recv(BUFFER_SIZE).decode() # recive data and decode it

        if data == "text":
            # Handle text communication
            handle_text(conn)
        elif data == "share file":
            # Handle file receiving
            handle_file(conn)
        else:
            print("Invalid operation received. Closing connection.")
            break

    conn.close() # close the connection

    print("Connection closed.")

def handle_text(conn):
    while True:
        data = conn.recv(BUFFER_SIZE).decode()
        if not data:
            break
        print(f"client: {data}")

        send_data = input("server: ")

        while len(send_data) < 1:
            send_data = input("server: ")

        conn.send(send_data)

def handle_file(conn):
    recived = conn.recv(BUFFER_SIZE).decode()
    file_name, file_size = recived.spit(",")
    file_name = file_name.strip()
    file_size = int(file_size.strip())

    print(f"Receiving file: {file_name} of size {file_size} bytes")

    with open(file_name, "wb") as f:
        total_received = 0
        while total_received < file_size:
            bytes_read = conn.recv(BUFFER_SIZE).decode()
            if not bytes_read:
                break

            f.write(bytes_read)
            total_received += bytes_read
            print(f"Received {total_received} of {file_size} bytes")

        print(f"File {file_name} received successfully.")

if __name__ == "__main__": # This block ensures that start_server() (or any code within it) will only be executed when you run the script directly.
    
    start_server()
