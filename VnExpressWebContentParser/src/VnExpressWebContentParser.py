##import requests
##from bs4 import BeautifulSoup
##response = requests.get("http://avi.im/stuff/js-or-no-js.html")
##soup = BeautifulSoup(response.text,'html.parser')
##print(soup.find(id="intro-text"))

##from selenium import webdriver
##driver = webdriver.PhantomJS()
##driver.get("http://avi.im/stuff/js-or-no-js.html")
##p_element = driver.find_element_by_id(id_='intro-text')
##print(p_element.text)

import selenium as se
from selenium import webdriver
options = se.webdriver.ChromeOptions()
options.add_argument('headless')
driver = se.webdriver.Chrome(chrome_options=options)
driver.get("http://avi.im/stuff/js-or-no-js.html")
p_element = driver.find_element_by_id(id_='intro-text')
print(p_element.text)
