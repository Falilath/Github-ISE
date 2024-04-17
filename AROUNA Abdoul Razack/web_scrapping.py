# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup
import csv 

### Déclarer une variable url

url="https://www.scrapethissite.com/pages/simple/"

response =  requests.get(url)

## Définir l'encodage du conten web récupéré

response.encoding="utf-8"

## faire une restriction sur l'objet response pour ressortir le code statut 
##revoyer suite à la requette d'extraction du contenu de la page web
if response.status_code == 200 :
    html=response.text
    #print(html)
    ## Extraction des contenu des balise 
    soup = BeautifulSoup(html,"html.parser")
    ## On rajoute .text pour ne par afficher le nom de la balise et rajouter
    ## .strip pour supprimer espace en début et en fin du contenu
    #print(soup.find("title").text)
    ## Extraire la balise "p" mais plus précisément la class "lead"
    print(soup.find('p',class_='lead').text)
    ## Récupération dans une variable country toutes les balises div de class 
    ## col-md-4 country 
    countries =  soup.find_all('div', class_= 'col-md-4 country')
    ## Création\ouverture du fichier csv (w en ecriture, newline, nouvelle ligne)
    with open('pays.csv','w', newline='', encoding='utf-8') as csvfile :
        writer=csv.writer(csvfile)
        writer.writerow(['Pays','Capital','Population','Superficie'])
        ## Récupération des données par pays
        for country in countries : 
            names=country.find('h3',class_='country-name').text.strip()
            capital=country.find('span', class_='country-capital').text.strip()
            population=country.find('span', class_= 'country-population').text.strip()
            area=country.find('span', class_='country-area').text.strip()
            #print(names)
            writer.writerow([names,capital,population,area])
    
    
else :
     print("Error:" + str(response.status_code))
    
## Extraction des contenu des balise 