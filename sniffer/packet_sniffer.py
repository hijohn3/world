from socket import *
import os

def sniffing(host):
    if os.name == 'nt':
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP

    sniffer = socket(AF_INET, SOCK_RAW, sock_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
    if os.name == 'nt':
        sniffer.ioctl(SIO_RCVALL, RCVALL_ON)
        packet = sniffer.recvfrom(65565)
        print(packet)
    
    if os.name == 'nt':
        sniffer.ioctl(SIO_RCVALL, RCVALL_OFF)
    
def main():
    #host = gethostbyname(gethostname())
    host = '10.0.2.15'
    print(f'START SNIFFING at {host}')
    sniffing(host)

if __name__ == '__main__':
    main()