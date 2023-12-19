import zipfile
from threading import Thread

def crackzip(zfile, passwd):
    try:
        zfile.extractall(path='./locked', pwd=passwd) #unzip
        print(f'ZIP file extracted successfully! PASS=[{passwd.decode()}]')
        return True
    
    except:
        print('Except!')
        pass
    return False

def main():
    dictfile = './dictionary.txt'
    zipfilename = './locked.zip'
    zfile = zipfile.ZipFile(zipfilename, 'r')
    pfile = open(dictfile, 'r')

    for line in pfile.readlines():
        passwd = line.strip('\n')
        t = Thread(target=crackzip, args=(zfile, passwd.encode('utf-8')))
        t.start()

main()