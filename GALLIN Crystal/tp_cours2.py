# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:52:34 2024

@author: HP
"""
## requests permet de faire des requètes post
import requests
## beautifulsoup pour extraire le contenu d'une balise
from bs4 import BeautifulSoup
import csv

## Déclarer une variable url
url= "https://www.scrapethissite.com/pages/simple/"
reponse=requests.get(url)
reponse.encoding="utf-8"
if reponse.status_code==200:
    html=reponse.text
    soup=BeautifulSoup(html,"html.parser")
    countries=soup.find_all("div",class_='col-md-4 country')
    ## ouverture du fichier csv (w en ecriture newline)
    with open('pays.csv',"w",newline='',encoding="utf-8") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(["Pays","Capital","population","Superficie"])
        for country in countries:
            name= country.find('h3',class_='country-name').text.strip()
            capital=country.find('span',class_='country-capital').text.strip()
            population=country.find('span',class_='country-population').text.strip()
            area=country.find('span',class_='country-area').text.strip()
            writer.writerow([name,capital,population,area])
            
    #print(soup.find("p",class_="lead").text)
    #print(soup.find("title").text.strip())
    #print(html)
else:
    print("Error:"+reponse.status_code)

## Extraction du titre (text pour juste le contenu et strip pour effacer les espaces de début et de fin)
## find_all() pour sélectionner plusieurs balises
