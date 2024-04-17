# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# IMPORTATION DES BIBLIOTHEQUES
import requests
from bs4 import BeautifulSoup
import csv

# DECLARTION DE LA VARIABLE URL
url="https://www.scrapethissite.com/pages/simple/"

response=requests.get(url)      # nous retourne le site web
response.encoding="utf-8"       # pour éviter les problèmes d'encodage
if response.status_code==200:
    html=response.text
    soup=BeautifulSoup(html, "html.parser")
    #print(soup.find("p", class_="lead").text.strip())
    #countries=soup.find("div", class_="col-md-4 country")
    countries=soup.find_all("div", class_="col-md-4 country")
    # OUVERTURE DU FICHIER CSV POUR RECUPERER LES DONNEES
    with open("Pays.csv", "w", newline="", encoding="utf-8") as csvfile :
        writer = csv.writer(csvfile)
        writer.writerow(["Pays", "Capitale", "Population", "Superficie"])
        for country in countries:
            #print (country)
            nom=country.find("h3", class_="country-name").text.strip()
            capitale=country.find("span", class_="country-capital").text.strip()
            population=country.find("span", class_="country-population").text.strip()
            superficie=country.find("span", class_="country-area").text.strip()
            writer.writerow([nom, capitale, population, superficie])
            #print(nom)
else:
    print("Erreur:"+response.status_code)
