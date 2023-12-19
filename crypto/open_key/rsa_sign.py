from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA

def readPEM(pemfile):
    h = open(pemfile, 'r')
    key = RSA.import_key(h.read())
    h.close()
    return key

def rsa_sign(msg):
    private_key = readPEM('privatekey.pem')
    public_key = private_key.publickey()
    h = SHA.new(msg)
    signature = pkcs1_15.new(private_key).sign(h)
    return public_key, signature

def rsa_verify(msg, public_key, signature):
    h = SHA.new(msg)

    try:
        pkcs1_15.new(public_key).verify(h, signature)
        print('Authentic')
    except Exception as e:
        print(e)
        print('NOT Authentic')

def main():
    msg = 'My name is Luden'
    public_key, signature = rsa_sign(msg.encode('utf-8'))
    rsa_verify(msg.encode('utf-8'), public_key, signature)
main()