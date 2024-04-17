# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:49:49 2024

@author: HP
"""

# Importation des librairies
import requests
from bs4 import BeautifulSoup
import csv

# Récupération des données à partir d'un lien
url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
response.encoding = "utf-8" # Pour éviter les problèmes d'encodage
if response.status_code == 200 :
    # Récupération du contenu html de la page
    html = response.text
    # Récupération du titre de la page
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.find("p", class_="lead").text.strip())
    # .text pour avoir le texte sans les balises
    # .strip pour enlever les espaces avant et après le texte 
    # On peut utiliser la fonction find_all pour avoir toutes les balises
    # d'un type donné
    
    countries = soup.find_all("div", class_ = "col-md-4 country")
    # Ouvertrure du fichier .csv
    with open("pays.csv", "w", newline = "", encoding = "utf-8") as csvfile :
        writer = csv.writer(csvfile)
        writer.writerow(["Pays", "Capital", "Population", "Superficie (Km²)"])
    
        for country in countries :
            #print(country)
            name = country.find("h3", class_ = "country-name").text.strip()
            capital = country.find("span", class_ = "country-capital").text.strip()
            population = country.find("span", class_ = "country-population").text.strip()
            area = country.find("span", class_ = "country-area").text.strip()
            writer.writerow([name, capital, population, area])
else :
    print("Erreur : " + response.status_code)
    
