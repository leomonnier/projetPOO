#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:34:52 2021

@author: leomon sebnoel
"""
#!pip install requests
#!pip install bs4
#!pip install PyPDF2

import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader
import io

class Ressource:
    def __init__(self,url):
        o= requests.get(url)
        t= o.headers.get('content-type')
        if 'pdf' in t:
            self.type="PDF"
        elif 'html' in t:
            self.type="HTML"
        if self.type=="HTML":
            text= BeautifulSoup(o.text, 'lxml')  #lxml pour eviter un message d'erreur
            self.text= text.text
        elif self.type=="PDF":
            pdf= PdfFileReader(io.BytesIO(o.content)) #recupère les informations du pdf
            numpage=pdf.getNumPages()                 #nombre de pages
            page_content=""                           #on créée une string avec le nombre de pages
            for i in range(numpage):
                page = pdf.getPage(i)
                page_content += page.extractText()
            self.text=page_content


    def __str__(self):
        return self
    
#une_ressource = Ressource("https://math.univ-angers.fr/documents/exercices_terminale_septembre_2014.pdf")
#print(une_ressource.text)    # renvoie "HTML"

class Collecte:                  #on prends une liste d'url et on sort une liste de content de ressource
    def __init__(self,listurl):
        self.listurl=listurl
    
    def run(self):
        L=[]
        for i in self.listurl:
            res=Ressource(i)
            L.append(res.text)
        self.content=L
        
    def __str__(self):
        return self
    
    

class Traitement :
    def __init__(self):
        self
    
    def load(self,liste):
        self.liste=liste
        
    def run(self):
        L=[]
        n=len(self.liste)
        for i in range(n):
            text = self.liste[i]
            words=''
            for char in text: #on enlève tout les points et les espaces.
                if char.isalnum():
                    words += char
                else:
                    words += ' '
            L.append(len(words.split()))  #transforme words en liste de mots, taille de la liste de tous les mots du texte (nombre vu comme des mots)
        self.resp= L
        
    def show(self):
        print(self.resp)
    
    def __str__(self):
        return self  
        
    
    
class Prisme:
    def __init__(self):
        self 
 """
 prisme récupère des urls et doit effectuer un traitements
 donc on crée une Collecte des éléments on fait tourner
 url --> texte
 on applique Traitement
 texte --> Nbr Mots
 
"""
   
    def run(self,liste):
        une_ressource = Collecte(liste)
        une_ressource.run()
        Trait=Traitement()
        Trait.load(une_ressource.content)
        Trait.run()
        self.res=Trait.resp
        
    def show(self):
        print(self.res)
    
    def __str__(self):
        return self  
        

#un_prisme = Prisme()     
#un_prisme.run(["https://math.univ-angers.fr","https://math.univ-angers.fr/documents/exercices_terminale_septembre_2014.pdf"])      # lance le traitement sur des ressources web référencées dans un_fichier
#un_prisme.show()
    

        
#une_ressource = Collecte(["https://math.univ-angers.fr","https://math.univ-angers.fr/documents/exercices_terminale_septembre_2014.pdf"])
#une_ressource.run()
#print(une_ressource.content)
#file = open("monfichier.txt", "w") 
#file.write(une_ressource.content[0]) 
#file.close()

            
#Trait=Traitement()
#Trait.load(une_ressource.content)
#Trait.run()
#Trait.show()
