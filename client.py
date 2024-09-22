import socket
import os

HOST_IP = "192.168.1.28" # my PC static ip address

PORT = 443 # the port that allows devices to share data

BUFFER_SIZE = 4096 # send 4096 bytes each time step

def start_client():

    print("== WELCOME TO MY TCP CLIENT AND SERVER PROJECT ==")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((HOST_IP, PORT))

    print("enter (exit) to break the connection")

    choose_operation = input("Choose operation (file share | text): ")


    if choose_operation == "file share":


        file_name = input("enter the file name: ")

        while len(file_name) < 1 or not os.path.exists(file_name):
            file_name = input("enter valid file name: ")

        file_size = os.path.getsize(file_name)
        client_socket.send(f"{file_name},{file_size}".encode())

        with open(file_name, "rb") as f:

            while True:

                bytes_read = f.read(BUFFER_SIZE)

                if not bytes_read:
                    break

                client_socket.sendall(bytes_read)

        print(f"File {file_name} sent successfully.")
        client_socket.close()
        print("Connection closed.")

    elif choose_operation == "text":


        while True:

            send_data = input("client: ") # enter data

            if send_data == "exit":

                break

            while len(send_data) < 1:

                send_data  = input("client: ") # enter valid data

            client_socket.send(send_data.encode()) # send data

            data = client_socket.recv(1024).decode() # recive data from the other side

            if not data:

                break # break the loop and close the connection

            print(f"Server: {data}")

    client_socket.close() # close the connection

    print("Connection closed.")

if __name__ == "__main__": # This block ensures that start_client() (or any code within it) will only be executed when you run the script directly.

    start_client()