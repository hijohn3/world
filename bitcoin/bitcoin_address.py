import hashlib
from ecdsa import SECP256k1, SigningKey
from base58check import b58encode

def get_private_key(hex_String):
    return bytes.fromhex(hex_String.zfill(64))

def get_public_key(private_key):
    return (bytes.fromhex('04')+SigningKey.from_string(private_key, curve=SECP256k1).verifying_key.to_string())

def get_public_address(public_key):
    address = hashlib.sha256(public_key).digest()

    h = hashlib.new('ripemd160') 
    print(h)#hashlib unsupported hash type ripemd160
    h.update(address)
    address = h.digest()

    return address

if __name__ == "__main__":
    private_key = get_private_key("FEEDB0BDEADBEEF")
    public_key = get_public_key(private_key)
    public_address = get_public_address(public_key)
    bitcoin_address = b58encode('00'+public_address)
    print(bitcoin_address)