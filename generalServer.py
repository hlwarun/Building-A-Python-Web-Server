import socket

HOST, PORT = '', 8000

# Creating our own simple socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET refers to the address family ipv4
# SOCK_STREAM refers to connection oriented TCP protocol

# Set the value of the given socket option
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket to given PORT of the HOST
mySocket.bind((HOST, PORT))

# Put the socket to the listening mode
mySocket.listen(1)
print('Listening to the server at Port {} ...'.format(PORT))

# Creating a loop that runs forever util we interrupt it manually
while True:
    # Establishing connection between the server and the client
    client_connection, client_address = mySocket.accept()
    # Receive data from the server
    received_data = client_connection.recv(1024)
    print(received_data.decode('utf-8'))

    http_response = b"""\
    HTTP/1.1 200 OK

    Hello, from the server side!
    """
    # Sending data from string until either all data has been sent or an error occurs
    client_connection.sendall(http_response)
    # Closing connection between the client and the server
    client_connection.close()
