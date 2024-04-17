# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import csv
country=""

url = "https://www.scrapethissite.com/pages/simple/"
reponse = requests.get(url)
reponse.encoding ="utf-8"

if reponse.status_code==200:
    html= reponse.text
    soup= BeautifulSoup(html,"html.parser")
    countries = soup.find_all ('div',class_='col-md-4 country')
    #strip() pour enlever les espaces sur le titre
    #find() renvoie la premiere balise
    #find_all() pour afficher toutes les balises en utilisant une boucle après
    
    #OUVERTURE DU FICHIER CSV
    with open("Pays.csv","w",newline='',encoding='utf-8') as csvfile:
        #w mode de lecture ecriture
        #newline pour a la fin de chaque ligne
        writer = csv.writer(csvfile)
        writer.writerow(['Pays','Capitale','Population','Superficie'])
        
        #PARCOURIR LE FICHIER
        for country in countries:
            name = country.find('h3',class_='country-name').text.strip()
            capital = country.find('span',class_='country-capital').text.strip()
            population = country.find('span',class_='country-population').text.strip()
            area =country.find('span',class_='country-area').text.strip()
            writer.writerow([name,capital,population,area])

else:
    print ("erreur:"+ reponse.status_code)

