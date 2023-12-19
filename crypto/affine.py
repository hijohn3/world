ENC = 0
DEC = 1

def makeDisk(k1, k2):
    enc_disk = {}
    dec_disk = {}

    for i in range(26):
        enc_i = (i*k1+k2)%26
        enc_ascii = enc_i + 65
        enc_disk[chr(i+65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)] = chr((i+65))

    return enc_disk, dec_disk

def affine(msg : str, key1, key2, mode):
    ret = ''

    msg = msg.upper()
    enc_disk, dec_disk = makeDisk(key1, key2)
    
    if mode is ENC:
        disk = enc_disk
    if mode is DEC:
        disk = dec_disk
    
    for c in msg:
        if c in disk:
            ret += disk[c]
    
        else:
            ret += c
    
    return ret

def main():
    plaintext = input()
    k1, k2 = 3, 5 

    print(f'Original:\t{plaintext.upper()}')
    ciphertext = affine(plaintext, k1, k2, ENC)
    print(f'Caesar Cipher : \t{ciphertext}')
    deciphertext = affine(ciphertext, k1, k2, DEC)
    print(f'Deciphered : \t{deciphertext}')

if __name__ == "__main__":
    main()