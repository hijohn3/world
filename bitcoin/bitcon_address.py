import os
import hashlib
from hashlib import sha256 as sha
from base58check import b58encode
from ecdsa import SECP256k1, SigningKey

def ripemd160(x):
    ret = hashlib.new('ripemd160')
    ret.update(x)
    return ret

def generateBitcoinAddress():
    #private key
    privkey = os.urandom(32)
    fullkey = '80' + privkey.hex()

    a = bytes.fromhex(fullkey)
    sha_a = sha(a).digest()
    sha_b = sha(sha_a).hexdigest()
    c = bytes.fromhex(fullkey+sha_b[:8])

    #WIF = Wallet import format 
    WIF = b58encode(c)

    #(1)ECDSA pubkey
    signing_key = ecdsa.SigningKey.from_string(privkey, curve=ecdsa.SECP256k1)
    verifying_key = signing_key.get_verifying_key()
    pubkey = (verifying_key.to_string).hex()

    #(2)
    pubkey = '04' + pubkey

    #(3)
    pub_sha = sha(bytes.fromhex(pubkey)).digest()
    encPubkey = ripemd160(pub_sha).digest()

    #(4)
    encPubkey = b'\x00' + encPubkey

    #(5)
    chunk = sha(sha(encPubkey).digest()).digest()

    #(6)
    checksum = chunk[:4]

    #(7)
    hex_address = encPubkey + checksum

    #(8)
    bitcoinAddress = b58encode(hex_address)

    #print WIF&bitcoin address
    print(f'+++WIF = {WIF.decode()}')
    print(f'+++Bitcoin Address = {bitcoinAddress.decode()}')

generateBitcoinAddress()