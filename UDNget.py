import requests
import lxml
from bs4 import BeautifulSoup

r = requests.get('https://udn.com/rssfeed/news/2/6638?ch=news')#發送get請求
r.encoding = 'utf-8'#轉換編碼
soup = BeautifulSoup(r.text)#結構化

if(r.status_code == requests.codes.ok):
    print('連線正常')
    print()
    i=1
    error = 0
    for soup in soup.find_all('p'):
        strsoup = str(soup)
        if(i == 20):
            print('完畢')
        else:
            print('今日頭條 第'+str(i)+'條:')
            print()
            print('    ',strsoup.strip('<p></p>'))
            print()
            i+=1
