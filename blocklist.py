import requests
from bs4 import BeautifulSoup

url = 'https://firebog.net/'
response = requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')

for li in soup.find_all('li', {'class': 'bdTick'}):
    if 'http' in li.text:
        #print(li.text.split(':', 1)[1])
        output1 = (li.text.split(':', 1)[1])
        output = output1.replace("/n"," ")
        print(output, sep=' ')
