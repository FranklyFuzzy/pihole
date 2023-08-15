import requests
from bs4 import BeautifulSoup

url = 'https://firebog.net/'
response = requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')

urls = []

for li in soup.find_all('li', {'class': 'bdTick'}):
    if 'http' in li.text:
        #print(li.text.split(':', 1)[1])
        urls.append(li.text.split(':', 1)[1])
        
print(*urls)
