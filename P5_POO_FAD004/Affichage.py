#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:12:46 2023

@author: aissatou
"""
import Separation_Donnee as S
import os

class Affichage():
    
    def afficherMenu(self):   
        print("\n\n\n\t\t\t******************************      Nettoyage de données      ******************************\n")
        print("\t\t\t\t\t\t\t\t"+"_"*53)
        print("\t\t\t\t\t\t\t\t| {0:50}|".format("                    Menu                         "))
        print("\t\t\t\t\t\t\t\t"+"-"*53)
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 1. Afficher les informations "))
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 2. Rechercher une information par le numéro"))
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 3. Afficher les cinq premiers éméments"))
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 4. Ajouter une nouvelle information"))
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 5. Modifier une information invalide"))
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 6. Quitter"))
        print("\t\t\t\t\t\t\t\t"+"_"*53)
        print("\n")
        a=input("\t\t\t\t\t\t\t\t Choix : ")
        while not a.isdigit():
            a=input("\t\t\t\t\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        while not ('1'<= a <='6'):
            a=input("\t\t\t\t\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        return int(a)

    def afficherSous_Menu1(self):
        print("\n\n\n\t\t\t******************************      Nettoyage de données      ******************************\n")
        print("\t\t\t\t\t\t\t\t"+"_"*53)
        print("\t\t\t\t\t\t\t\t| {0:50}|".format("          Afficher les informations             "))
        print("\t\t\t\t\t\t\t\t"+"-"*53)
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 1. Informations valides "))
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 2. Informations invalides"))
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 3. Retour"))
        print("\t\t\t\t\t\t\t\t"+"_"*53)
        print("\n")
        a=input("\t\t\t\t\t\t\t\t Choix : ")
        while not a.isdigit():
            a=input("\t\t\t\t\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        while not ('1'<= a <='3'):
            a=input("\t\t\t\t\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        return int(a)

    def afficherSous_Menu2(self,Eleve):
        print("\n\n\n\t\t\t******************************      Nettoyage de données      ******************************\n")
        print("\t\t\t\t\t\t\t\t"+"_"*53)
        print("\t\t\t\t|\t\t\t\t {0:50}|".format("          Modifier une information invalide     "))
        print("\t\t\t\t\t\t\t\t"+"-"*53)
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" Choisissez un paramettre : "))
        for i in range(len(Eleve.get_problemes())):
            print("\t\t\t\t\t\t\t\t|  {0:3}. {1:44}|".format(str(i+1),Eleve.get_problemes()[i]))
        print("\t\t\t\t\t\t\t\t|  {0:3}. {1:44}|".format(str(len(Eleve.get_problemes())+1),"Retour"))
       
        
        print("\t\t\t\t\t\t\t\t"+"_"*53)
        print("\n")
        a=input("\t\t\t\t\t\t\t\t Choix : ")
        while not a.isdigit():
            a=input("\t\t\t\t\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        while not ('1'<= a <= str(len(Eleve.get_problemes())+1)):
            a=input("\t\t\t\t\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        return int(a)-1

    def afficherSous_Menu3(self):
        print("\n\n\n\t\t\t******************************      Nettoyage de données      ******************************\n")
        print("\t\t\t\t\t\t\t\t"+"_"*53)
        print("\t\t\t\t\t\t\t\t| {0:50}|".format("          Afficher les informations             "))
        print("\t\t\t\t\t\t\t\t"+"-"*53)
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 1. Afficher les informations personnelles"))
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 2. Afficher les notes d\'un élèvé"))
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 3. Retour"))
        print("\t\t\t\t\t\t\t\t"+"_"*53)
        print("\n")
        a=input("\t\t\t\t\t\t\t\t Choix : ")
        while not a.isdigit():
            a=input("\t\t\t\t\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        while not ('1'<= a <='3'):
            a=input("\t\t\t\t\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        return int(a)

    def afficherSous_Menu4(self):
        print("\n\n\n\t\t\t******************************      Nettoyage de données      ******************************\n")
        print("\t\t\t\t\t\t\t\t"+"_"*53)
        print("\t\t\t\t\t\t\t\t| {0:50}|".format("          options d\'affichage                  "))
        print("\t\t\t\t\t\t\t\t"+"-"*53)
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 1. Afficher toutes les informations"))
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 2. Afficher par rang de 5"))
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 3. Choisir un rang personnalisé"))
        print("\t\t\t\t\t\t\t\t| {0:50}|".format(" 4. Retour"))
        print("\t\t\t\t\t\t\t\t"+"_"*53)
        print("\n")
        a=input("\t\t\t\t\t\t\t\t Choix : ")
        while not a.isdigit():
            a=input("\t\t\t\t\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        while not ('1'<= a <='4'):
            a=input("\t\t\t\t\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        return int(a)
    
    
    def affichageDonneeValide(self,liste_eleve,rang):
        a=0
    
        print("\n\n\n\t\t\t******************************      Nettoyage de données      ******************************\n")
        print("\t\t\t\t Nombres de données valides : ",len(liste_eleve))
        print("\t\t\t\t"+"-"*66)
        print("\t\t\t\t| {0:8} | {1:10} | {2:13} | {3:12} | {4:7} |".format("Numero","Nom","Prénom","Date","Classe"))
        print("\t\t\t\t"+"-"*66)
        for i in range(rang):
            a+=1
            print("\t\t\t\t| {0:8} | {1:10} | {2:13} | {3:12} | {4:7} |".format(liste_eleve[i].get_numero(),liste_eleve[i].get_nom(),liste_eleve[i].get_prenom(),liste_eleve[i].get_date_naissance(),liste_eleve[i].get_classe()))
        print("\t\t\t\t"+"-"*66)
       
    def affichageDonneeInvalide(self,liste_eleve,rang):
        a=0
        print(" Nombres de données valides : ",len(liste_eleve)-1)
        print("-"*171)
        print("| {0:10} | {1:10} |{2:13} |{3:12} |{4:7} |{5:105} |".format("Numero","Nom","Prénom","Date","Classe","Notes"))
        print("-"*171)
        for i in range(1,rang):
            a+=1
            print("| {0:10} | {1:10} |{2:13} |{3:12} |{4:7} |{5:105} |".format(liste_eleve[i].get_numero(),liste_eleve[i].get_nom(),liste_eleve[i].get_prenom(),liste_eleve[i].get_date_naissance(),liste_eleve[i].get_classe(),liste_eleve[i].get_notes()))
        print("-"*171)
        
        
    def affichageCinqPremier(self,liste_eleve):
        index=S.Separation_Donnee().recupererIndex(liste_eleve)
        index=index[:5]
        print("\n\n")
        print("\t\t\t\t* {0:73}*".format("                      Affichage des cinq premiers                      "))
        print("\t\t\t\t"+"-"*73)
        print("\t\t\t\t| {0:8} | {1:10} |{2:13} |{3:12} |{4:7} |{5:8} |".format("Numero","Nom","Prénom","Date","Classe","Moyennes"))
        print("\t\t\t\t"+"-"*73)
        for i in index:
            print("\t\t\t\t| {0:8} | {1:10} |{2:13} |{3:12} |{4:7} |{5:8.2f} |".format(liste_eleve[i].get_numero(),liste_eleve[i].get_nom(),liste_eleve[i].get_prenom(),liste_eleve[i].get_date_naissance(),liste_eleve[i].get_classe(),liste_eleve[i].get_moyenne()))
        print("\t\t\t\t"+"-"*73)  
    
    
    def afficherNote(self,liste_eleve,numero):
        donnee,liste_cle,liste_format=[],[],""
        for eleve in liste_eleve:
            if numero==eleve.get_numero():
                donnee=eleve
                break
        if donnee==[]:
            return False
        notes=eleve.get_notes()
        a=0
        print('-'*(23*(len(notes)+1)+1))
        print("| {0:20} ".format("Numero"),end="")
        for i in notes.keys():    
            print("| {0:20} ".format(i),end="")
        print("|")
        print('-'*(23*(len(notes)+1)+1))
        print("| {0:20} ".format(numero),end="")
        for i in notes.values():      
            print("| {0:20} ".format(str(i).replace("[","").replace("],"," :").replace("'","").replace("]","")),end="")
        print("|")
        print('-'*(23*(len(notes)+1)+1))
    
    def afficherProblemes(self,liste_eleve,numero):
        donnee,liste_cle,liste_format=[],[],""
        for eleve in liste_eleve:
            if numero==eleve.get_numero():
                donnee=eleve
                break
        if donnee==[]:
            return False,"Le numero saisie n\'appartient pas aux données invalides"
        problemes=donnee.get_problemes()
        print("\t"+"-"*140)
        print("\t| {0:13} | {1:120} |".format("Champs","Raisons d\'invalidité"))
        print("\t"+"-"*140)
        for i in range(len(problemes)):
            print("\t| {0:13} | {1:120} |".format(problemes[i][0],str(problemes[i][1]).replace(",","").replace("[","").replace("(","").replace("'","").replace('"',"").replace(")","").replace("]","")))
        print("\t"+"-"*140)
    
    
    def afficherResultatRecherche(self,ResultatRecherche):
       eleve=ResultatRecherche[0]
       if ResultatRecherche[1]=='valide':
           print("\t\t\t * Informations personelles de l\'éléve : les données sont valides")
           print('\t\t\t'+'-'*83)
           print("\t\t\t| {0:16} | {1:15} |{2:20} |{3:12} |{4:7} |".format("Numero","Nom","Prénom","Date","Classe"))
           print('\t\t\t'+'-'*83)
           print("\t\t\t| {0:16} | {1:15} |{2:20} |{3:12} |{4:7} |".format(eleve.get_numero(),eleve.get_nom(),eleve.get_prenom(),eleve.get_date_naissance(),eleve.get_classe()))
           print('\t\t\t'+'-'*83)
           print("\n")
           print("* Notes de l\'éléve ")
           print('-'*(23*(len(eleve.get_notes()))))
           for i in eleve.get_notes().keys():    
               print("| {0:20} ".format(i),end="")
           print("|")
           print('-'*(23*(len(eleve.get_notes()))+1))
       
           for i in eleve.get_notes().values():      
               print("| {0:20} ".format(str(i).replace("[","").replace("],"," :").replace("'","").replace("]","")),end="")
           print("|")
           print('-'*(23*(len(eleve.get_notes()))+1))
           
       elif ResultatRecherche[1]=='invalide':
           print("* Informations personelles de l\'éléve : les données sont invalides")
           print('-'*196)
           print("| {0:16} | {1:15} |{2:20} |{3:12} |{4:7} |{5:111} |".format("Numero","Nom","Prénom","Date","Classe","Notes"))
           print('-'*196)
           print("| {0:16} | {1:15} |{2:20} |{3:12} |{4:7} |{5:111} |".format(eleve.get_numero(),eleve.get_nom(),eleve.get_prenom(),eleve.get_date_naissance(),eleve.get_classe(),str(eleve.get_notes())))
           print('-'*196)
           problemes=eleve.get_problemes()
           print("\t"+"Problèmes rencontrés :")
           print("\t"+"-"*140)
           print("\t| {0:13} | {1:120} |".format("Champs","Raisons d\'invalidité"))
           print("\t"+"-"*140)
           for i in range(len(problemes)):
               print("\t| {0:13} | {1:120} |".format(problemes[i][0],str(problemes[i][1]).replace(",","").replace("[","").replace("(","").replace("'","").replace('"',"").replace(")","").replace("]","")))
           print("\t"+"-"*140)
    
    def choisirFormatEntree(self):
        os.system('clear')
        print("\t\t\t\t"+"_"*53)
        print("\t\t\t\t| {0:50}|".format("   Choisir votre format de donnée en entrée    "))
        print("\t\t\t\t"+"-"*53)
        print("\t\t\t\t| {0:50}|".format(" 1. Fichier CSV "))
        print("\t\t\t\t| {0:50}|".format(" 2. Ficher JSON"))
        print("\t\t\t\t| {0:50}|".format(" 3. Fichier XML"))
        print("\t\t\t\t"+"_"*53)
        print("\n")
        a=input("\t\t\t\t Choix : ")
        while not a.isdigit():
            a=input("\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        while not ('1'<= a <='3'):
            a=input("\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        liste_format=["CSV","JSON","XML"]
        return liste_format[int(a)-1]
    
    def choisirFormatSortie(self,entree):
        liste_format=["CSV","JSON","XML"]
        new_liste=[]
        os.system('clear')
        print("\t\t\t\t"+"_"*53)
        print("\t\t\t\t| {0:50}|".format(" Choisir le format de sortie des données valides"))
        print("\t\t\t\t"+"-"*53)
        c=1
        for i in range(len(liste_format)):
            if liste_format[i]!= entree:
                print("\t\t\t\t| {0:1} . {1:46}|".format(c,"Fichier "+liste_format[i]))
                new_liste.append(liste_format[i])
                c+=1
        print("\t\t\t\t"+"_"*53)
        print("\t\t\t\t"+" PS: Les données invalides vont être dans le format non choisi ")
        a=input("\t\t\t\tChoix : ")
        while not a.isdigit():
            a=input("\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        while not ('1'<= a <='2'):
            a=input("\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
        a=int(a)
        autre=0
        if a==1:
            autre==2
        else:
            autre==1
        
        return new_liste[a-1],new_liste[autre-1]