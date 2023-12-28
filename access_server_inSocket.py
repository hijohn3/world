#This Port scanner For ports ending in 000 eg, 1000, 2000, 3000
import socket

RHOST = 'host3.dreamhack.games'
RPORT = 8694

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, recv TCP packet
s.connect((RHOST, RPORT))

data = s.recv(1024)
print(f'Received : {data}')