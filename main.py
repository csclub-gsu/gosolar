import requests
from bs4 import BeautifulSoup
import json
import re
# Make a request to the website
response = requests.get('https://www.gosolar.gsu.edu/bprod/twbkwbis.P_ValLogin')

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())
# Find the input field
input = soup.find_all("input")
# Post the username and password to the login form || in campusID and password, put your campus ID and password
post_data = {"sid": "campusID", "PIN": "password"}
cookies = {'TESTID': 'set'}
post = requests.post('https://www.gosolar.gsu.edu/bprod/twbkwbis.P_ValLogin', data=post_data, cookies=cookies)
response_text = post.text


registration_page_response = requests.get('https://registration.gosolar.gsu.edu/StudentRegistrationSsb/ssb/classSearch/classSearch', cookies=cookies)
registration_page_soup = BeautifulSoup(registration_page_response.text, 'lxml')
# registration_page_cookies = registration_page_response.cookies

class_schedule_response = requests.get('https://registration.gosolar.gsu.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search', cookies=cookies)
class_schedule_soup = BeautifulSoup(class_schedule_response.text, 'lxml')
class_schedule_cookies = class_schedule_response.cookies


# This is where I left off
term_post = requests.post('https://registration.gosolar.gsu.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search', data={"term": "202301"}, cookies=class_schedule_cookies)
term_post_text = term_post.text
