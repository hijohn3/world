from urllib.request import urlopen, Request
import re
import sys

user_agent = 'Mozilla/5.0\(compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0)like Gecko'
href_links = []

def getLinks(doc, home, parent):
    global href_links
    href_pattern = [r'href=\S+"', r'href=\S+ ', r'href=\S+\'']
    tmp_urls = []

    for n in range(len(href_pattern)):
        tmp_urls += re.findall(href_pattern[n], doc, re.I)
    
    for url in tmp_urls:
        url = url.strip()
        url = url.replace('\'', '"')
        if url[-1] is ' ' or url.find('"') is -1:
            url = url.split('=')[1]
        else:
            url = url.split('"')[1]

        if len(url) is 0:
            continue

        if url.find('https://') is -1:
            if url[0] == '/':
                url = home + url
            elif url[:2] == './':
                url = 'https://' + parent + url[1:]
            else:
                url = 'https://' + parent + '/' + url
        
        if url in href_links:
            continue
    
        if './html' not in url:
            href_links.append(url)
            continue

        runCrawler(home, url)

def readHtml(url):
    try:
        req = Request(url)
        req.add_header('User-Agent', user_agent)
        with urlopen(req) as h:
            doc = h.read()
    except Exception as e:
        print(f'ERROR : {url}')
        print(e)
        return None
    return doc.decode()

def runCrawler(home, url):
    global href_links
    href_links.append(url)
    print(f'GETTiNG ALL LINKS in [{url}]')
    try:
        doc = readHtml(url)
        if doc is None:
            return

        tmp = url.split('/')
        parent = '/'.join(tmp[2:-1])
        if parent:
            getLinks(doc, home, parent)
        else:
            getLinks(doc, home, home)
    except KeyboardInterrupt:
        print('Terminated by User..saving craled links')
        finalize()
        sys.exit(0)
    return 

def finalize():
    with open('crawled_links.txt', 'w+') as f:
        for href_link in href_links:
            f.write(href_link+'\n')
    print(f'+++ CRAWLED TOTAL href_links: [{len(href_links)}]')

def main():
    targeturl = 'https://www.google.co.kr'
    home = 'https://' + targeturl.split('/')[2]
    print(f'+++ WEB LINK CRAWLER START > [{targeturl}]')
    runCrawler(home, targeturl)
    finalize()
main()