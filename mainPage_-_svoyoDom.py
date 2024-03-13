import requests
from bs4 import BeautifulSoup

url = 'https://svoydom.kz/project/1/1061833/'
page = requests.get(url)
print('pageStatus:', page.status_code)

allInfo = list()
filterInfo = list()

soup = BeautifulSoup(page.text, "html.parser")



allInfo = soup.findAll(class_='favorites-items')
for data in allInfo:
    if data.find('ul', class_='favorite-info-list') is not None:
        filterInfo.append(data.text)

print(filterInfo)