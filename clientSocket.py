# In the more traditional sense of client and server,
# you wouldnt actually have the client and server on the same machine.
#  If you wanted to have two programs talking to eachother locally,
# you could do this, but typically your client will more likely connect to some external
# server, using its public IP address, not socket.gethostname().
# You will pass the string of the IP instead.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))


full_msg = ""
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)
