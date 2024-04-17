# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  

#RECUPERER LES DONNEE DE LA PAGE AVEC SELENIUM
url = "https://perspective.usherbrooke.ca/bilan/BMEncyclopedie/BMEncycloListePays.jsp"
service= Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)
driver.get(url)
html= driver.page_source
#print(html)

soup= BeautifulSoup(html,"html.parser")
countries = soup.find ('section',class_='maingroup')
#for country in countries.find_all('li') :
#    link= 'https://perspective.usherbrooke.ca'+country.find('a').get('href').strip()
#    print(link)

country= countries.find('li')
link= 'https://perspective.usherbrooke.ca'+ country.find('a').get('href').strip()
driver.get(link)
page_html= driver.page_source
print(page_html)

soup1=BeautifulSoup(page_html,'html.parser')
print(soup1)
source = soup1.find ('div',id='lienContainer2x')
print(source)
link2=source.find('a').get('href')
print(link2)