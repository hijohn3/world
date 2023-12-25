from urllib.request import urlopen, Request
from urllib.error import URLError
from urllib.parse import quote
from queue import Queue
from threading import Thread

user_agent = 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'

def webScanner(q : Queue, targethost, exts):
    while not q.empty():
        scanlist = []
        toscan = q.get()
        if '.' in toscan: #File
            scanlist.append(str(toscan))
            for ext in exts:
                scanlist.append('%s%s' %(toscan, ext))
        else: #DIR
            scanlist.append(str(toscan)+'/')
        
        for toscan in scanlist:
            url = '%s/%s' %(targethost, quote(toscan))
            try:
                req = Request(url)
                req.add_header('User-Agent', user_agent)
                res = urlopen(req)
                if len(res.read()):
                    print(f'[{res.code}] : {url}')
                res.close()
            except URLError as e:
                pass
    
def main():
    targethost = 'https://172.21.70.227'
    wordlist = './all.txt'
    exts = ['~', '~1', '.back', '.bak', '.old', '.orig', '_backup']
    q = Queue()

    with open(wordlist, 'rt') as f:
        words = f.readlines()

    for word in words:
        word = word.rstrip()
        q.put(word)
    
    print(f'+++[{targethost}] SCANNING START')
    for i in range(50):
        t = Thread(target = webScanner, args=(q, targethost, exts))
        t.start()

if __name__ == '__main__':
    main()