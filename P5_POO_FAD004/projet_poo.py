#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 07:37:58 2023

@author: aissatou
"""

import Eleve as E
import Conversion_Fichier as CF
import Affichage as A
import Separation_Donnee as S
import CreerOutput as CO


#test=V.Validation.verifierNumero()

liste_eleve=[]
#On demande a l'utilisateur le format de données qu'il souhaite exploté
formatDonnee=A.Affichage().choisirFormatEntree()

#On va transformer les données d'origine vers le format souhaité
new_file=CF.Conversion("Donnée.csv",formatDonnee)

#On recupere les donnees qui se trouvent dans le fichier
Donnée=CF.RecupererDonnee(new_file.get_nouveauFichier())
liste_donnee=Donnée.get_donnee()

#On separe les donnees valides des donnees invalides
liste_eleve=S.Separation_Donnee().trierDonnee(liste_donnee)

a=A.Affichage().afficherMenu()
while a!=6:
    
    #Afficher les informations
    if a==1:
        #L'option B==1 permet d'afficher les informations valides 
        b=A.Affichage().afficherSous_Menu1()
        if b==1:
            c=A.Affichage().afficherSous_Menu3()
            #L'option C==1 permet d'afficher les informations personnelles valides 
            if c==1:
                d=A.Affichage().afficherSous_Menu4()
                if d!=4:
                    if d==1:
                        rang=len(liste_eleve[0])
                        print(("deg"))
                    elif d==2:
                        rang=5
                    else :
                        rang=input("Saisir le rang d\'affichage : ")
                        while not rang.isdigit():
                            rang=input("Le rang doit etre un entier")
                        rang=int(rang)
                    a=rang
                    while rang<=len(liste_eleve[0]):
                        A.Affichage().affichageDonneeValide(liste_eleve[0],rang)
                        if d==1:
                            break
                        res=input("Appuyer sur la touche \'Entrer\'pour tabuler. Pour arrêter saisir \'stop\' : ")
                        if res=='stop':
                            break
                        else:
                            if len(liste_eleve[0])==rang:
                                break
                            if len(liste_eleve[0])-rang<a:
                                rang=len(liste_eleve[0])
                            else :
                                rang+=a
                            continue
                    a=A.Affichage().afficherMenu()
                    continue
                else :
                    a=A.Affichage().afficherMenu()
                    continue
            #L'option C==2 permet d'afficher les notes  valides d'un elelve
            elif c==2:
                num=input('Saisir le numéro de l\'étudiant : ')
                while num.isspace():
                    num=input('Le numéro de l\'étudiant ne doit pas etre vide : ')
                A.Affichage().afficherNote(liste_eleve[0], num)
                a=A.Affichage().afficherMenu()
                continue
            elif c==3:
                a=A.Affichage().afficherMenu()
                continue
            
        elif b==2:
            d=A.Affichage().afficherSous_Menu4()
            if d!=3:
                if d==1:
                    rang=len(liste_eleve[1])
                elif d==2:
                    rang=5
                else :
                    rang=input("Saisir le rang d\'affichage : ")
                    while not rang.isdigit():
                        rang=input("Le rang doit etre un entier")
                    rang=int(rang)
                a=rang
                while rang<=len(liste_eleve[1]):
                    A.Affichage().affichageDonneeInvalide(liste_eleve[1],rang)
                    res=input("Appuyer sur n\'importe qu'elle touche pour tabuler. Pour arrêter saisir \'stop\' : ")
                    if res=='stop':
                        break
                    else:
                        if len(liste_eleve[1])==rang:
                            break
                        if len(liste_eleve[1])-rang<a:
                            rang=len(liste_eleve[1])
                        else :
                            rang+=a
                a=A.Affichage().afficherMenu()
                continue
            else :
                a=A.Affichage().afficherMenu()
                continue
         
            
        elif b==3:
            a=A.Affichage().afficherMenu()
            continue
    
    #Rechercher une information par le numéro
    elif a==2:
        num=input('Saisir le numéro de l\'étudiant : ')
        while num.isspace():
            num=input('Le numéro de l\'étudiant ne doit pas etre vide : ')
        resultat=S.Separation_Donnee().rechercherInfo(liste_eleve,num)
        if resultat==[]:
            print("\n\n\t\t\t\tLe numero saisie n\'existe pas !!! ")
        else: 
            A.Affichage().afficherResultatRecherche(resultat)
        a=A.Affichage().afficherMenu()
        continue
      
    #Afficher les cinq premiers éméments
    elif a==3:
        A.Affichage().affichageCinqPremier(liste_eleve[0])
        a=A.Affichage().afficherMenu()
    
    #Ajouter une nouvelle information 
    elif a==4:
        S.Separation_Donnee().ajouterDonnee(liste_eleve[0])
        a=A.Affichage().afficherMenu()
        continue
    
    #Modifier une information invalide 
    elif a==5:
       num=input('Saisir le numéro de l\'étudiant : ')
       while num.isspace():
           num=input('Le numéro de l\'étudiant ne doit pas etre vide : ')
       resultat=S.Separation_Donnee().modifierDonneeInvalide(liste_eleve,num)
       print(resultat[1])
       a=A.Affichage().afficherMenu()
       continue

sortie=A.Affichage().choisirFormatSortie(formatDonnee)
nom_output_valide,nom_output_invalide='',''
if sortie[0]=="CSV":
    nom_output_valide=CO.CreerOutput().creerCSV(liste_eleve[0])
elif sortie[0]=="JSON":
    nom_output_valide=CO.CreerOutput().creerJSON(liste_eleve[0])
elif sortie[0]=="XML":
    nom_output_valide=CO.CreerOutput().creerXML(liste_eleve[0],1)
    
if sortie[1]=="CSV":
    nom_output_invalide=CO.CreerOutput().creerCSV(liste_eleve[1])
elif sortie[1]=="JSON":
    nom_output_invalide=CO.CreerOutput().creerJSON(liste_eleve[1])
elif sortie[1]=="XML":
    nom_output_invalide=CO.CreerOutput().creerXML(liste_eleve[1],2)

print("Les données valides sont enregistrées sur "+nom_output_valide+" et les données invalides sur "+nom_output_invalide)
   
