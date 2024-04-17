# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:14:50 2024

@author: ALEX
"""

import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url="https://perspective.usherbrooke.ca/bilan/BMEncyclopedie/BMEncycloListePays.jsp"
options=webdriver.ChromeOptions()
options.add_argument("--headless")
#service=Service(ChromeDriverManager().install())
#driver=webdriver.Chrome(service=service)
driver=webdriver.Chrome(options=options)

driver.get(url)
html=driver.page_source
soup=BeautifulSoup(html,"lxml")
countries=soup.find('section',class_='maingroup')
links=[]