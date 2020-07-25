import socket

# Server side of the code
# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
# bind in the server side and connect in the client side
s.listen(5)  # !making queue of five clients at the time more than that will be denied


while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hey there!!!", "utf-8"))
    clientsocket.close()
