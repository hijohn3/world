from hashlib import sha256 as SHA
SIZE = 1024 * 256

def getFileHash(filename):
    sha = SHA()
    h = open(filename, 'rb')
    content = h.read(SIZE)
    while content:
        sha.update(content)
        content = h.read(SIZE)
    h.close()

    hashval = sha.digest()
    return hashval

def hashCheck(file1, file2):
    hashval1 = getFileHash(file1)
    hashval2 = getFileHash(file2)

    if hashval1 == hashval2:
        print('Two Files are Same')
    else:
        print('Two Files are Different')
    
def main():
    file1 = 'file1'
    file2 = 'file2'
    hashCheck(file1, file2)

main()