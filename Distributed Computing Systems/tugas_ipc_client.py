# Import lib socket, time and random
import socket
import time
import random

# Initialize object socket TCP IPv4
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to localhost and port 6663
tcp_socket.connect(("127.0.0.1", 6663))

# Looping for censor program
index = 0
while True:

    # Initialize random number
    raw_data = [random.randint(-10,30), random.randint(0,100), random.randint(0,100)]

    # Send message to previous connection
    data = '{"temperature": "'+str(raw_data[0])+'", "humidity_level": "'+str(raw_data[1])+'", "oxygen_level": "'+str(raw_data[2])+'"}'
    tcp_socket.send(data.encode('ascii'))
    print("Censor data for", index, "second(s) to", (index + 1), "second(s) has been sent")

    time.sleep(1)
    index += 1