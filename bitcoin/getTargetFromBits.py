from hashlib import sha256 as sha
import codecs

#return bits to hex value
def decodeBitcoinVal(bits):
    decode_hex = codecs.getdecoder('hex_codec')
    binn = decode_hex(bits)[0]
    ret = codecs.encode(binn[::-1], 'hex_codec')
    return ret

def getTarget(bits):
    bits = decodeBitcoinVal(bits)
    bits = int(bits, 16)
    print(f'Bits = {hex(bits)[2:]}')
    bit1 = bits >> 4*6 #detach first bytes
    base = bits & 0x00ffffff #detach [1:] bytes
    sft = (bit1 - 0x3)*8
    target = base << sft
    print(f'Target = {hex(target)[2:]}')

Bits = 'f2b9441a'
getTarget(Bits)