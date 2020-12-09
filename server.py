#!/usr/bin/python3

import socket
import sys
import os

mac_address = os.environ["WOL_TARGET_MAC"]
if mac_address is None or mac_address == "":
    mac_address = input("WoL target mac address: ")
password = os.environ["WOL_PASSWORD"]
if password is None or password == "":
    password = input("WoL activation password: ")

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Usage : ./server.py <arg1:server ip:this system IP 192.168.1.6> <arg2:server port:4444 >")
    exit(1)

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (ip, port)
s.bind(server_address)
print("Do Ctrl+c to exit the program !!")

while True:
    print("####### Server is listening #######")
    data, address = s.recvfrom(4096)
    print("\n\n 2. Server received: ", data.decode('utf-8'), "\n\n")
    if password in str(data):
        os.system(f"wakeonlan {mac_address}")
        send_data = "Wakeup initiated..."
    else:
        send_data = f"Incorrect password ({data})"
    s.sendto(send_data.encode('utf-8'), address)
    print("\n\n 1. Server sent : ", send_data,"\n\n")
