from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA

class myAES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:16]

        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:16]

    def makeEnabled(self, plaintext):
        fillersize : int = 0
        textsize = len(plaintext)
        if textsize%16 != 0:
            fillersize = 16-textsize%16
        
        filler = '0'*fillersize
        header = str(fillersize)
        gap = 16-len(header)
        header += '#'*gap

        return header+plaintext+filler
    
    def enc(self, plaintext):
        plaintext = self.makeEnabled(plaintext)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        encmsg = aes.encrypt(plaintext.encode())
        return encmsg
    
    def dec(self, ciphertext):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        decmsg = aes.decrypt(ciphertext)

        header = decmsg[:16].decode()
        fillersize = int(header.split('#')[0])
        if fillersize != 0:
            decmsg = decmsg[16:-fillersize]
        else:
            decsmg = decmsg[16:]
        return decmsg.decode()

def main():
    keytext = 'helloworld'
    ivtext = '1234'
    makeaes = myAES(keytext=keytext, ivtext=ivtext)

    plaintext:str = input()
    print(f'msg -> {plaintext}')
    encrypt = makeaes.enc(plaintext=plaintext)
    print(f'Encrypt -> {encrypt}')
    decrypt = makeaes.dec(ciphertext=encrypt)
    print(f'Decrypt -> {decrypt}')

if __name__ == '__main__':
    main()