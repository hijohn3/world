from socket import *
import struct
import os

def parse_ipheader(data):
    ipheader = struct.unpack('!BBHHHBBH4s4s', data[:20])
    return ipheader

def getDatagramSize(ipheader):
    return str(ipheader[2])

def getProtocol(ipheader):
    protocols = {1:'ICMP', 6:'TCP', 17:'UDP'}
    proto = ipheader[6]
    if proto in protocols:
        return protocols[proto]
    else:
        return 'OHTERS'
    
def getIP(ipheader):
    src_ip = inet_ntoa(ipheader[8])
    dest_ip = inet_ntoa(ipheader[9])
    return (src_ip, dest_ip)

def getIPHeaderLen(ipheader):
    ipheaderlen = ipheader[0] & 0x0f
    ipheaderlen *= 4
    return ipheaderlen

def getTypeCode(icmp):
    icmpheader = struct.unpack('!BB', icmp[:2])
    icmp_type = icmpheader[0]
    icmp_code = icmpheader[1]
    return (icmp_type, icmp_code)

def recvData(sock):
    data = ''
    try:
        data = sock.recvfrom(65565)
    except timeout:
        data = ''
    return data[0]

def sniffing(host):
    if os.name == 'nt':
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP

    sniffer = socket(AF_INET, SOCK_RAW, sock_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    count = 1
    try:
        while True:
            data = recvData(sniffer)
            ipheader = parse_ipheader(data[:20])
            ipheaderlen = getIPHeaderLen(ipheader)
            datagramSize = getDatagramSize(ipheader)
            protocol = getProtocol(ipheader)
            src_ip, dest_ip = getIP(ipheader)
            if protocol == 'ICMP':
                offset = ipheaderlen
                icmp_type, icmp_code = getTypeCode(data[offset:])
                print(f'{src_ip} -> {dest_ip} : Type[{icmp_type}], Code[{icmp_code}]')
            print(f'SNIFFED [{count}] -------------')
            print(f'Datagram Size : {datagramSize}')
            print(f'Protocol : {protocol}')
            print(f'Source IP : {src_ip}')
            print(f'Destination IP : {dest_ip}')
            count += 1
    except KeyboardInterrupt:
        if os.name == 'nt':
            sniffer.ioctl(SIO_RCVALL, RCVALL_OFF)
    
def main():
    host = gethostbyname(gethostname())
    #host = '192.168.0.3'
    print(f'START SNIFFING at {host}')
    sniffing(host)

if __name__ == '__main__':
    main()
