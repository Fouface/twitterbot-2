import requests
from bs4 import BeautifulSoup
URL= 'https://www.agazeta.com.br/'
page= requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')

print(page)
print('')
print(search)
