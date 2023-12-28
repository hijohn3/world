#This Port scanner For ports ending in 000 eg, 1000, 2000, 3000
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, recv TCP packet
#s.settimeout(20) #timeout 2seconds

port = 20621
for portx in range(1, 40):
    try:
        s.connect(('host3.dreamhack.games', port)) #write server
        r = s.recv(4096)
        if 'thread' in r.decode(): #write success to access message
            print(f'[!]SERVICE FOUND! : {port} ~ {r.decode()}')
            s.close()
            break
        else:
            print(f'[*]SCANNING...{port} ~ {r.decode()} ')
            s.close()
    except socket.error as err:
        print(f'[#]PORT ERROR -> {port} : {err}')
    
    port += 1