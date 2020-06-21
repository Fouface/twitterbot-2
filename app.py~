from selenium import webdriver
import requests, random, string
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


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

#opens webdriver
driver = webdriver.Chrome(executable_path='/Users/siber/Desktop\chromedriver.exe')

#go to gerrillia webapp
driver.get('https://guerrillamail.com/')

# find and click on button to create a new email
element= driver.find_element_by_id( "inbox-id")
element.click()

# create a email with the random email
input = driver.find_element_by_xpath('//*[@id="inbox-id"]/input').send_keys('cheese')
set = driver.find_element_by_xpath('//*[@id="inbox-id"]/button[1]')
set.click()


# opens the list of names
names= open("names.txt","r")
number_of_lines = 0

# gets the number of names in the file
for line in names:
    line = line.strip("\n")
    number_of_lines += 1
names.close()

#generates a randon full name
def randon_name():
    names= open("names.txt","r")
    numb = random.randint(1, number_of_lines)
    numb2 = random.randint(1, number_of_lines)
    
    lines = names.readlines()
    username = lines[numb]+lines[numb2]
    
    # replaces the \n with a space
    username = username.replace('\n',' ')
    names.close()
    return username

full_name = randon_name()
data = open("data.txt","w")
data.write(full_name+' '+random_email)
data.close()
# driver.quit()



