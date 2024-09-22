import socket
import os

HOST_IP = "192.168.1.28" # my PC static ip address
PORT = 443 # the port that allows devices to share data
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST_IP, PORT))

def start_client():
    print("== WELCOME TO MY TCP CLIENT AND SERVER PROJECT ==")
    print("enter (exit) to break the connection")

    # input to get the operation the client want
    enter_operation = input("choose operation please (file sharing | texting): ")
    if enter_operation == "texting":
        handle_texting()
    elif enter_operation == "file sharing":
        handle_file_sharing()

def handle_file_sharing():
    file_name = input("enter file name to open (i.e text.txt): ")

    # while the length of file_name provided by the user is zero, ask for file_name again
    while len(file_name) == 0:
        file_name = input("enter file name to open (i.e text.txt): ")

    # if the file does not exists ask the client to try again
    while not os.path.exists(file_name):
        enter_file_name_again = input(file_name + "was not found, try again (i.e text.txt): ")

    # if the file exists, open it and read the data inside it
    if os.path.exists(file_name):
        print(file_name + " found")
        open_file = open(file_name, "r")
        read_data = open_file.read()
        client_socket.send("text.txt".encode())
        client_socket.send(read_data.encode())

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