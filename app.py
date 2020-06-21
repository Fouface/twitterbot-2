import requests
from bs4 import BeautifulSoup
# go to https://www.guerrillamail.com/
# generate a randon email
# generate randon name, randon surname, randon bday
# save to database
# go to signup page -> 
# enter name, email, birthday date
# generate password -> save to database
# next-> next-> sign up->get code from email -> and finish#signing up 
# get an api key

URL= 'https://twitter.com/i/flow/signup'
page= requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')

print(page)
print('')
print(soup)
