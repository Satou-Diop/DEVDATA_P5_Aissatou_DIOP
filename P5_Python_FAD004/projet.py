#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 07:38:53 2023

@author: aissatou
"""
from fonction_projet import *
import os
#donnee=recupererDonneeCSV("Donnée.csv")

entree=choisirFormatEntree()
if entree==1:
    donnee=recupererDonneeCSV("Donnée.csv")
elif entree==2:
    donnee=recupererDonneeXLM(transformer_CSV_XML("Donnée.csv"))
elif entree==3:
    donnee=recupererDonneeJSON(transformer_CSV_JSON("Donnée.csv"))
    
liste=trierDonnee(donnee)
os.system('clear')
a=afficherMenu()

while a!=6:
    
    if a==1:
        b=afficherSous_Menu1()
        if b==1:
            c=afficherSous_Menu3()
            if c==1:
                d=afficherSous_Menu4()
                if d!=3:
                    if d==1:
                        rang=5
                    else :
                            rang=input("Saisir le rang d\'affichage : ")
                            while not estEntier(rang):
                                rang=input("Le rang doit etre un entier")
                            rang=int(rang)
                    a=rang
                    while rang<len(liste[0]):
                        affichageDonneeValide1(liste[0],rang)
                        res=input("Appuyer sur la touche \'Entrer\'pour tabuler. Pour arrêter saisir \'stop\' : ")
                        if res=='stop':
                            break
                        else:
                            rang+=a
                            continue
                    a=afficherMenu()
                    continue
                else :
                    a=afficherMenu()
                    continue
            elif c==2:
                d=afficherSous_Menu4()
                if d!=3:
                    if d==1:
                        rang=5
                    else :
                        rang=input("Saisir le rang d\'affichage")
                    a=rang
                    while rang<len(liste[1]):    
                        affichageDonneeValide2(liste[0],rang)
                        res=input("ppuyer sur la touche \'Entrer\'pour tabuler. Pour arrêter saisir \'stop\' : ")
                        if res=='stop':
                            break
                        else:
                            rang+=a
                            continue
                    a=afficherMenu()
                    continue
                else :
                    a=afficherMenu()
                    continue
            elif c==3:
                a=afficherMenu()
                continue
            
        elif b==2:
            d=afficherSous_Menu4()
            if d!=3:
                if d==1:
                    rang=5
                else :
                    rang=input("Saisir le rang d\'affichage : ")
                    while not estEntier(rang):
                        rang=input("Le rang doit etre un entier")
                    rang=int(rang)
                a=rang
                while rang<len(liste[0]):
                    affichageDonneeInvalide(liste[1],rang)
                    res=input("Appuyer sur n\'importe qu'elle touche pour tabuler. Pour arrêter saisir \'stop\' : ")
                    if res=='stop':
                        break
                    else:
                        rang+=a
                        continue
                a=afficherMenu()
                continue
            else :
                a=afficherMenu()
                continue
         
            
        elif b==3:
            a=afficherMenu()
            continue
            
    elif a==2:
        num=input('Saisir le numéro de l\'étudiant : ')
        while num=='':
            num=input('\t\t\t\tLe numéro de l\'étudiant ne doit pas etre vide : ')
        resultat=rechercherInfo(liste[0],liste[1],num)
        if resultat==[]:
            print("\n\n\t\t\t\tLe numero saisie n\'existe pas !!! ")
        else: 
            afficherDonnee(resultat)
        a=afficherMenu()
        continue
           
    elif a==3:
        affichagePremier(liste[0])
        a=afficherMenu()
           
    elif a==4:
        liste_info=['le code : ','le numéro : ','le nom : ','le prenom : ','la date de naissance suivant le format jj/mm/aa : ','la classe : ','les notes : ']
        new_donnee=[]
        print('Veuillez saisir')
        for i in range(0,len(liste_info)):
            new_d=input(liste_info[i])
            new_donnee.append(new_d)
        result=ajouterDonnee(new_donnee,liste[0])
        if result[0] :
            print('Les donnees ont ete ajoutéés!')
        else :
            print("Il y\'a eu erreur lors de l\'ajout sur les données : ",end="")
            for i in result[1]:
                print(i,end=" ")
            print('\n')
        a=afficherMenu()
        continue
    
    elif a==5:
       num=input('Saisir le numéro de l\'étudiant : ')
       while num=='':
           num=input('Le numéro de l\'étudiant ne doit pas etre vide : ')
       resultat=rechercherInfo(liste[1],liste[1],num)
       if resultat==[]:
           print("Le numero saisie n\'appartient pas aux informations invalides ! ")
           a=afficherMenu()
           continue
       indice=afficherSous_Menu2(resultat)
       if indice+1==len(resultat[7])+1:
           a=afficherMenu()
           continue
       new_val=input('Saisir la nouvelle valeur : ')
       while new_val=='':
           new_val=input('La nouvelle valeur ne doit pas etre vide : ')
       res=modifierInfo(liste[1],num,indice,new_val)
       if res:
           print('Les donnees ont ete modifiées!')
           print(new_val,indice)
       else :
           print("Il y\'a eu erreur lors de la modifications des données : ")
       a=afficherMenu()
       continue
           
    
sortie=choisirFormatSortie(entree)
nom_output_valide,nom_output_invalide='',''
if sortie[0]=="CSV":
    nom_output_valide=creerCSV(liste[0])
elif sortie[0]=="JSON":
    nom_output_valide=creerJSON(liste[0])
elif sortie[0]=="XML":
    nom_output_valide=creerXML(liste[0],1)
    
if sortie[1]=="CSV":
    nom_output_invalide=creerCSV(liste[1])
elif sortie[1]=="JSON":
    nom_output_invalide=creerJSON(liste[1])
elif sortie[1]=="XML":
    nom_output_invalide=creerXML(liste[1],2)

print("Les données valides sont enregistrées sur "+nom_output_valide+" et les données invalides sur "+nom_output_invalide)
    
