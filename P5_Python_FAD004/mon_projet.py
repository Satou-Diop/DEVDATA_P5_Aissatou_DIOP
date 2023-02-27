"""
@author: Aissatou DIOP
"""
from mes_fonction import *
import os

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
    
    #Afficher les informations
    if a==1:
        #L'option B==1 permet d'afficher les informations valides 
        b=afficherSous_Menu1()
        if b==1:
            c=afficherSous_Menu3()
            #L'option C==1 permet d'afficher les informations personnelles valides 
            if c==1:
                d=afficherSous_Menu4()
                if d!=4:
                    if d==1:
                        rang=len(liste[0])
                        print(("deg"))
                    elif d==2:
                        rang=5
                    else :
                        rang=input("Saisir le rang d\'affichage : ")
                        while not rang.isdigit():
                            rang=input("Le rang doit etre un entier")
                        rang=int(rang)
                    a=rang
                    while rang<=len(liste[0]):
                        affichageDonneeValide(liste[0],rang)
                        if d==1:
                            break
                        res=input("Appuyer sur la touche \'Entrer\'pour tabuler. Pour arrêter saisir \'stop\' : ")
                        if res=='stop':
                            break
                        else:
                            if len(liste[0])==rang:
                                break
                            if len(liste[0])-rang<a:
                                rang=len(liste[0])
                            else :
                                rang+=a
                            continue
                    a=afficherMenu()
                    continue
                else :
                    a=afficherMenu()
                    continue
            #L'option C==2 permet d'afficher les notes  valides d'un elelve
            elif c==2:
                num=input('Saisir le numéro de l\'étudiant : ')
                while num.isspace():
                    num=input('Le numéro de l\'étudiant ne doit pas etre vide : ')
                afficherNote(liste[0], num)
                a=afficherMenu()
                continue
            elif c==3:
                a=afficherMenu()
                continue
            
        elif b==2:
            d=afficherSous_Menu4()
            if d!=3:
                if d==1:
                    rang=len(liste[1])
                elif d==2:
                    rang=5
                else :
                    rang=input("Saisir le rang d\'affichage : ")
                    while not rang.isdigit():
                        rang=input("Le rang doit etre un entier")
                    rang=int(rang)
                a=rang
                while rang<=len(liste[1]):
                    affichageDonneeInvalide(liste[1],rang)
                    res=input("Appuyer sur n\'importe qu'elle touche pour tabuler. Pour arrêter saisir \'stop\' : ")
                    if res=='stop':
                        break
                    else:
                        if len(liste[1])==rang:
                            break
                        if len(liste[1])-rang<a:
                            rang=len(liste[1])
                        else :
                            rang+=a
                a=afficherMenu()
                continue
            else :
                a=afficherMenu()
                continue
         
            
        elif b==3:
            a=afficherMenu()
            continue
    
    #Rechercher une information par le numéro
    elif a==2:
        num=input('Saisir le numéro de l\'étudiant : ')
        while num.isspace():
            num=input('Le numéro de l\'étudiant ne doit pas etre vide : ')
        resultat=rechercherInfo(liste,num)
        if resultat==[]:
            print("\n\n\t\t\t\tLe numero saisie n\'existe pas !!! ")
        else: 
            afficherResultatRecherche(resultat)
        a=afficherMenu()
        continue
      
    #Afficher les cinq premiers éméments
    elif a==3:
        affichageCinqPremier(liste[0])
        a=afficherMenu()
    
    #Ajouter une nouvelle information 
    elif a==4:
        ajouterDonnee(liste[0])
        a=afficherMenu()
        continue
    
    #Modifier une information invalide 
    elif a==5:
       num=input('Saisir le numéro de l\'étudiant : ')
       while num.isspace():
           num=input('Le numéro de l\'étudiant ne doit pas etre vide : ')
       resultat=modifierDonneeInvalide(liste,num)
       print(resultat[1])
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
   