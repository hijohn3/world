from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def rsa_enc(msg):
    private_key = RSA.generate(1024)
    public_key = private_key.publickey()
    cipher = PKCS1_OAEP.new(public_key)
    encdata = cipher.encrypt(msg)
    print(encdata)

    cipher = PKCS1_OAEP.new(private_key)
    decdata = cipher.decrypt(encdata)
    print(decdata)

def main():
    msg = 'hello python world!'
    rsa_enc(msg.encode('utf-8'))

if __name__ == '__main__':
    main()