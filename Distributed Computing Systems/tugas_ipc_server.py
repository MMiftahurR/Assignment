# Import lib socket, threading and json
import socket
import threading
import json


# Thread
def handle_thread(conn):
    index = 0
    while True:
        try:
            # Read data from client
            censor_data = conn.recv(100)

            # Process data
            censor_data = censor_data.decode('ascii')
            censor_data = json.loads(censor_data)
            print("=>Censor data for", index, "second(s) to", (index+1),"second(s)")
            print("Temperature]t\t:", censor_data["temperature"], "`C")
            print("Humidity Level\t:", censor_data["humidity_level"], "%")
            print("Oxygen Level\t:", censor_data["oxygen_level"], "%")

            # Divider
            print("==========================================================")
        except (socket.error):
            # Disconnected with client
            conn.close()

            print("Disconnected with client")

            # Divider
            print("==========================================================")
            break
        index += 1

# Initialize object socket TCP IPv4
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to all interface and port 6663
tcp_socket.bind(('0.0.0.0', 6663))

# Max listen to 1 connection
tcp_socket.listen(1)

# Looping for server service
print("Preparing...")
print("==========================================================")
while True:

    # Establish connection
    preconn, client_address = tcp_socket.accept()

    # Start new thread
    t = threading.Thread(target=handle_thread, args=(preconn,))
    t.start()