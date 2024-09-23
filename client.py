import socket
import os

HOST_IP = "192.168.1.28" # my PC static ip address
PORT = 443 # the port that allows devices to share data
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST_IP, PORT))

def start_client():
    print("== WELCOME TO MY TCP CLIENT AND SERVER PROJECT ==")
    print("enter (exit) to break the connection")

    handle_texting()

def handle_texting():
    while True:
        send_data  = input("client: ") # enter data
        if send_data == "exit":
            break
        while len(send_data) < 1:
            send_data  = input("client: ") # enter data
        client_socket.send(send_data.encode()) # send data
        data = client_socket.recv(1024).decode() # recive data from the other side
        if not data:
            break # break the loop and close the connection
        print(f"Server: {data}")
    client_socket.close() # close the connection
    print("Connection closed.")

if __name__ == "__main__": # This block ensures that start_client() (or any code within it) will only be executed when you run the script directly.
    start_client()