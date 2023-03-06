#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 08:14:20 2023

@author: aissatou
"""
import csv,json
import xml.etree.ElementTree as etree
import Eleve as E

#ON CREE UNE CLASSE QUI CONVERTIT LES DONNEES CSV VERS LES FORMATS JSON ET XML 
class Conversion:
    
    def __init__(self,fichier,new_type):
        if new_type.upper()=="XML":
            self.fichier=self.transformer_CSV_XML(fichier)
        elif new_type.upper()=="JSON":
            self.fichier=self.transformer_CSV_JSON(fichier)
        else:
            self.fichier=fichier
        
    def get_nouveauFichier(self):
        return self.fichier
      
    def transformer_CSV_XML(self,fichier_csv):
        donnee_csv = csv.reader(open(fichier_csv,"r"))
        donnee=[]
        for i in donnee_csv:
            donnee.append(i)
       
        #Recuperer les entetes
        ligne=0
        balise=[]
        fichierXML="output.xml"
        documentXml = open(fichierXML, 'w')
        documentXml.write('<?xml version="1.0" encoding="ISO-8859-1" ?>' + "\n")
        documentXml.write('<Eleve>' + "\n")
        for i in range(len(donnee[0])):
            balise.append(donnee[0][i].replace(" ", "").replace("é","e"))
            
        for i in range(1,len(donnee)):
            balise_code="\t<"+balise[0]+">"+donnee[i][0]+"</"+balise[0]+">\n"
            balise_numero="\t<"+balise[1]+">"+donnee[i][1]+"</"+balise[1]+">\n"
            balise_nom="\t<"+balise[2]+">"+donnee[i][2]+"</"+balise[2]+">\n"
            balise_prenom="\t<"+balise[3]+">"+donnee[i][3]+"</"+balise[3]+">\n"
            balise_date="\t<"+balise[4]+">"+donnee[i][4]+"</"+balise[4]+">\n"
            balise_classe="\t<"+balise[5]+">"+donnee[i][5]+"</"+balise[5]+">\n"
            balise_note="\t<"+balise[6]+">"+donnee[i][6]+"</"+balise[6]+">\n"
            
            documentXml.write("<Element>\n" + balise_code+balise_numero+balise_nom+balise_prenom+balise_date+balise_classe+balise_note+"</Element> \n")

        documentXml.write('</Eleve>' + "\n")  
        documentXml.close()
        return "output.xml"

    def transformer_CSV_JSON(self,fichier_csv):
        donnee_csv = csv.reader(open(fichier_csv,"r"))
        donnee=[]
        for i in donnee_csv:
            donnee.append(i)
       
        #Recuperer les entetes
        element,cle,liste={},[],[]
        fichierjson="output.json"
        documentJson= open(fichierjson, 'w')
    
        for i in range(len(donnee[0])):
            cle.append(donnee[0][i].replace(" ", ""))
            
        for i in range(1,len(donnee)):
            element[cle[0]]=donnee[i][0]
            element[cle[1]]=donnee[i][1]
            element[cle[2]]=donnee[i][2]
            element[cle[3]]=donnee[i][3]
            element[cle[4]]=donnee[i][4]
            element[cle[5]]=donnee[i][5]
            element[cle[6]]=donnee[i][6]
            liste.append(element) 
            element={}
            
        json.dump(liste, documentJson)
        return "output.json"


#ON CREE UNE CLASSE QUI RECUPERE LES DONNEES DANS LES DIFFERENTS FORMAT DE FICHIERS
class RecupererDonnee():
    
    #On va extraire les donnees suivant le type de fichier (extension)
    def extraireDonnee(self,fichier,extension):
        if extension=='CSV':
            donnee_csv = csv.reader(open(fichier,"r"))
            donnee=[]
            for i in donnee_csv:
               donnee.append(i)
            return donnee
        
        if extension=='JSON':
            donnee,liste_donnee=[],[]
            with open(fichier) as f:
                data = json.load(f)
            for i in data:
                for j in i.values():
                    donnee.append(j)
                liste_donnee.append(donnee)
                donnee=[]
            return liste_donnee
        
        if extension=='XML':
            liste_donnee=[]
            donnee=[]
            tree = etree.parse(fichier)
            root = tree.getroot()
            for element in root:    
                for j in element:
                    donnee.append(str(j.text))
                liste_donnee.append(donnee)
                donnee=[]
            return liste_donnee
    
    
    def __init__(self,fichier):
        try :
            extension=fichier.split('.')[1].upper()
            donnee_brute=self.extraireDonnee(fichier,extension)
            #On transforme les données recuperées en objet Eleve
            liste_eleve=[]
            for i in donnee_brute:
                eleve=E.Eleve(i[0], i[1], i[2], i[3], i[4], i[5],i[6])
                liste_eleve.append(eleve)
            self.donnee=liste_eleve
        except:
            self.donnee=[]
            pass
    
    def get_donnee(self):
        return self.donnee
    
    
class Transformer_Liste_en_Objet():
    
    def __init__(self,liste):
        for i in liste: 
            liste_eleve=[]
            eleve=E.Eleve(i[0], i[1], i[2], i[3], i[4], i[5],i[6])
            liste.append(eleve)
        self.liste_eleve=liste_eleve
        
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    