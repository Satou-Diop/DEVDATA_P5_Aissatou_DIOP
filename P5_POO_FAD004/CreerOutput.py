#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 08:14:20 2023

@author: aissatou
"""
import csv,json
import xml.etree.ElementTree as etree
import Eleve as E

class CreerOutput():
    
    def creerXML(self,liste_eleve,option):
        fichierXML="resultat.xml"
        documentXml = open(fichierXML, 'w')
        documentXml.write('<?xml version="1.0" encoding="ISO-8859-1" ?>' + "\n")
        documentXml.write('<Eleve>' + "\n")
        balise=["Code","Numero","Nom","Prenom","Date_Naissance","Classe","Notes"]
        for i in range(len(liste_eleve)):
            balise_code="\t<"+balise[0]+">"+liste_eleve[i].get_code()+"</"+balise[0]+">\n"
            balise_numero="\t<"+balise[1]+">"+liste_eleve[i].get_numero()+"</"+balise[1]+">\n"
            balise_nom="\t<"+balise[2]+">"+liste_eleve[i].get_nom()+"</"+balise[2]+">\n"
            balise_prenom="\t<"+balise[3]+">"+liste_eleve[i].get_prenom()+"</"+balise[3]+">\n"
            balise_date="\t<"+balise[4]+">"+liste_eleve[i].get_date_naissance()+"</"+balise[4]+">\n"
            balise_classe="\t<"+balise[5]+">"+liste_eleve[i].get_classe()+"</"+balise[5]+">\n"
            if option==1:
                balise_note="\t<"+balise[6]+">\n"
                for key,values in liste_eleve[i].get_notes().items():
                    for j in values[0]:
                        note="\t\t<note matiere='"+key+"' type_note='devoir'> "+j+ "</note>\n"
                        balise_note+=note
                    note="\t\t<note matiere='"+key+"' type_note='exam'> "+values[1]+ "</note>\n"    
                    balise_note+=note
                balise_note+="</"+balise[6]+">\n"
            else:
                balise_note="\t<"+balise[6]+">"+str(liste_eleve[i].get_notes())+"</"+balise[6]+">\n"    
            documentXml.write('<Element>\n' + balise_code+balise_numero+balise_nom+balise_prenom+balise_date+balise_classe+balise_note+"</Element> \n")
            
        documentXml.write('</Eleve>' + "\n")  
        documentXml.close()
        
        return 'resulat.xml'
        
    def creerCSV(self,liste_eleve):
        with open('resultat.csv',"w") as result :
            writer=csv.writer(result)
            #Definir les entetes
            entete=["Code","Numero","Nom","Prenom","Date_Naissance","Classe","Notes"]
            writer.writerow((entete[0],entete[1],entete[2],entete[3],entete[4],entete[5],entete[6]))
            for eleve in liste_eleve:
                writer.writerow((eleve.get_code(),eleve.get_numero(),eleve.get_nom(),eleve.get_prenom(),eleve.get_date_naissance(),eleve.get_classe(),eleve.get_notes()))
        return 'resulat.csv'

    def creerJSON(self,liste_eleve):
        cle=["Code","Numero","Nom","Prenom","Date_Naissance","Classe","Notes"]
        #Recuperer les entetes
        element,liste={},[]
        documentJson= open("resulat.json", 'w')
            
        for i in range(len(liste_eleve)):
            element[cle[0]]=liste_eleve[i].get_code()
            element[cle[1]]=liste_eleve[i].get_numero()
            element[cle[2]]=liste_eleve[i].get_nom()
            element[cle[3]]=liste_eleve[i].get_prenom()
            element[cle[4]]=liste_eleve[i].get_date_naissance()
            element[cle[5]]=liste_eleve[i].get_classe()
            element[cle[6]]=liste_eleve[i].get_notes()
            liste.append(element) 
            element={}
            
        json.dump(liste, documentJson)
        return 'resulat.json'