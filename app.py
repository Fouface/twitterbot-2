from selenium import webdriver
import requests, random, string
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


#this function creates a randon string to be the email
def randomword(length):
    letters=    string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


random_email = randomword(8)


driver = webdriver.Chrome(executable_path='/Users/siber/Desktop\chromedriver.exe')
driver.get('https://guerrillamail.com/')
element= driver.find_element_by_id( "inbox-id")
element.click()

# driver.quit()
URL= 'https://twitter.com/i/flow/signup'
page= requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')

