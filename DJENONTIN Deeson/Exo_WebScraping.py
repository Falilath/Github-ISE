# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 07:43:49 2024

@author: ALEX
"""
import requests
from bs4 import BeautifulSoup
import csv

url="https://www.scrapethissite.com/pages/simple/"
reponse=requests.get(url)
reponse.encoding="utf-8"
if reponse.status_code==200:
    html=reponse.text
    soup=BeautifulSoup(html,"html.parser")
    #print(soup.find('p',class_='lead').text)
    # les balises div
    countries=soup.find_all('div',class_='col-md-4 country')
    #Ouverture du fichier csv (w en écriture,newline, rien à la fin de la ligne)
    with open("pays.csv","w",newline='',encoding="utf-8") as csvfile:
        #
        writer=csv.writer(csvfile)
        #L'en-tête du fichier
        writer.writerow(["Pays","Capitale","Population","Superficie_(km2)"])
        for country in countries :
            #print(country)
            name=country.find('h3',class_='country-name').text.strip()
            capital=country.find('span',class_='country-capital').text.strip()
            population=country.find('span',class_='country-population').text.strip()
            area=country.find('span',class_='country-area').text.strip()
            writer.writerow([name,capital,population,area])
            #print(name)
            #print(capital)
else:
    print("Error:"+reponse.status_code)
print(countries)
