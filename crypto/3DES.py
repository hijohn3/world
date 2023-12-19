from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA

def make8string(msg):
    msglen = len(msg)
    padding = ''
    if msglen%8 != 0:
        padding = '0'*(8-msglen%8)
    msg += padding
    return msg

class myDES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:24] #3DES's key is 16bytes or 24bytes

        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:8]
    
    def enc(self, plaintext):
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        plaintext = make8string(plaintext)
        encmsg = des3.encrypt(plaintext.encode())
        return encmsg
    
    def dec(self, ciphertext):
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        decmsg = des3.decrypt(ciphertext)
        return decmsg.decode('utf-8')
    
def main():
    keytext = 'helloworld'
    ivtext = '1234'
    msg = 'python3xdd'

    myCipher = myDES(keytext, ivtext)
    ciphered = myCipher.enc(msg)
    deciphered = myCipher.dec(ciphered)
    print(f'MSG : {msg}')
    print(f'ciphertext : {ciphered}')
    print(f'deciphertext : {deciphered}')

main()