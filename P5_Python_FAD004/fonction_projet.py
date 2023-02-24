"""
Created on Mon Feb 13 15:31:55 2023
@author: aissatou
"""

import csv
import os
import datetime
import xml.etree.ElementTree as etree
import json

def recupererDonneeCSV(nom_fichier_csv):
    donnee = csv.reader(open(nom_fichier_csv,"r"))
    return donnee


            
def verifierNumero(numero):
    if len(numero)!=7:
        return False
    for i in numero:
        if not ('A'<= i <= 'Z' or '0'<= i <= '9'):
            return False 
    return True

def verifierNom(nom):
    if len(nom)<2:
        return False
    for i in nom:
        if not ('A'<= i <= 'Z' or 'a'<= i <= 'z' or i in ['é','è','ê','ï',' '] ):
            return False 
    return True

def verifierPrenom(prenom):
    if len(prenom)<3:
        return False
    for i in prenom:
        if not ('A'<= i <= 'Z' or 'a'<= i <= 'z' or i in ['é','è','ê','ï',' '] ):
            return False 
    return True

def verifierClasse(classe):
    if len(classe)< 1:
        return ''
    if not ('3' <= classe[0]<='6'):
        return ''
  
    if classe[-1]!='A' and classe[3]!='B':
        return ''
    return classe[0]+"em"+classe[-1]

def verifierNote(note):
    matiere,note1='',''
    liste_notes={}
    notes_devoirs=[]
    if len(note)>1:
        if note[-1]!="]":
            note=note+"]"
    for i in range(len(note)):
        if note[i]=='#' or note[i]==' ':
            continue
        if not ('0'<=note[i]<='9') and note[i] not in [':','|',']',',','.']:
            if note[i] != '[':
                if note[i]== 'ç' or note[i]== 'Ç':
                    matiere+='c'
                else:
                    matiere+=note[i]
                continue
        else :
            if matiere=='':
                continue
        
            if note[i] not in [':','|',']']:
                note1+=note[i]
                continue
            else :
                if note[i]  in  [':','|']:
                    if ',' in note1:
                        note1=note1.replace(',','.')
                    if note1=="":
                        return {}
                    if not (0<=float(note1)<=20) :
                        return {}
                    notes_devoirs.append(note1)  
                    note1=''
                if note[i]==']':
                    matiere=matiere.upper()
                    if matiere not in ["MATH","FRANCAIS","SVT","ANGLAIS","HG","PC"]:
                        return {}
                    else:
                        for j in liste_notes.keys():
                            if matiere == j:
                                return {}
                    if ',' in note1:
                        note1=note1.replace(',','.') 
                    if note1=="":
                        return {}
                    if not (0<=float(note1)<=20) :
                        return {}
                    liste_notes[matiere]=[notes_devoirs,note1]
                    matiere=''
                    note1=''
                    notes_devoirs=[]
    a=0
    for keys in liste_notes.keys():
        a+=1
        if keys not in ["MATH","FRANCAIS","SVT","ANGLAIS","HG","PC"]:
            return {}
    if a != 6 :
        return {}
    return liste_notes
            
def calculerMoyenne(note):
    somme_note,moyenne=0,0
    notes_devoirs=note[0]
    notes_exam=float(note[1])
    
    for i in range(len(notes_devoirs)):
        somme_note+=float(notes_devoirs[i])
        
    moyenne=(((somme_note/len(note[0])) + 2*notes_exam)/3)
    
    
    
    return moyenne

def verifierDate(date):
    date=date.replace(' ','')
    date1=''
    if '-' in date:
        date=date.replace('-','/')
    if ':' in date:
        date=date.replace(':','/')
    date=date.split('/')
    if len(date) != 3:
        return ''
    
    if len(date[2])==4:
        date[2]=date[2][2]+date[2][3]
    if not estEntier(date[0]) or not estEntier(date[1]) or  not estEntier(date[2]):
            return ''   
    try:
        datetest=datetime.datetime(int(date[2]),int(date[1]),int(date[0]))
        data=datetest.strftime("%d /%m /%y")
        date1='/'.join(date)
        return date1
    except :
        return ''

def estEntier(nombre):
    for i in nombre:
        if i==' ':
            continue
        if '0'<= i <= '9':
            continue
        else :
            return False
    return True
                
def verifierDonnee(donnee):
    probleme=[]
    date,classe='',''
    note=[]
    isValide=True
    for i in range(len(donnee)):
        if i==1:
            if not verifierNumero(donnee[1]):
                probleme.append("Numero")
                isValide=False  
        if i==2:
            if not verifierNom(donnee[2]):
                probleme.append("Nom")
                isValide=False 
        if i==3:
            if not verifierPrenom(donnee[3]):
                probleme.append("Prenom")
                isValide=False  
        if i==4:
            date=verifierDate(donnee[4])
            if date=='' or date==[]:
                probleme.append("Date")
                isValide=False
            donnee[4]=date
        if i==5:
            classe=verifierClasse(donnee[5])
            if classe=='' :
                probleme.append("Classe")
                isValide=False 
            donnee[5]=classe
        if i==6:
            note=verifierNote(donnee[6])
            if note==[] or note=={}:
                probleme.append("Note")
                isValide=False
    return isValide,date,classe,note,probleme
    
def trierDonnee(liste_donnee):
    donnee_valide,donnee_invalide=[],[]  
    for donnee in liste_donnee:
        result=verifierDonnee(donnee)
        isValide=result[0]       
        if isValide:
            donnee_valide.append([donnee[0],donnee[1],donnee[2],donnee[3],result[1],result[2],result[3]])
        else:
            donnee_invalide.append([donnee[0],donnee[1],donnee[2],donnee[3],donnee[4],donnee[5],donnee[6],result[4]])
    return donnee_valide,donnee_invalide

def ajouterDonnee(donnee,donnee_valide):
    result=verifierDonnee(donnee)
    isValide=result[0]       
    if isValide:
        donnee_valide.append([donnee[0],donnee[1],donnee[2],donnee[3],result[1],result[2],result[3]])
        return True
    else:
        return False,result[4]
    
def afficherMenu():   
    print("\t\t\t\t"+"_"*53)
    print("\t\t\t\t| {0:50}|".format("                    Menu                         "))
    print("\t\t\t\t"+"-"*53)
    print("\t\t\t\t| {0:50}|".format(" 1. Afficher les informations "))
    print("\t\t\t\t| {0:50}|".format(" 2. Rechercher une information par le numéro"))
    print("\t\t\t\t| {0:50}|".format(" 3. Afficher les cinq premiers éméments"))
    print("\t\t\t\t| {0:50}|".format(" 4. Ajouter une nouvelle information"))
    print("\t\t\t\t| {0:50}|".format(" 5. Modifier une information invalide"))
    print("\t\t\t\t| {0:50}|".format(" 6. Quitter"))
    print("\t\t\t\t"+"_"*53)
    print("\n")
    a=input("\t\t\t\t Choix : ")
    
    while not ('1'<= a <='6'):
        a=input("\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
    return int(a)

def afficherSous_Menu1():
    os.system('clear')
    print("\t\t\t\t"+"_"*53)
    print("\t\t\t\t| {0:50}|".format("          Afficher les informations             "))
    print("\t\t\t\t"+"-"*53)
    print("\t\t\t\t| {0:50}|".format(" 1. Informations valides "))
    print("\t\t\t\t| {0:50}|".format(" 2. Informations invalides"))
    print("\t\t\t\t| {0:50}|".format(" 3. Retour"))
    print("\t\t\t\t"+"_"*53)
    print("\n")
    a=input("\t\t\t\t Choix : ")
    
    while not ('1'<= a <='3'):
        a=input("\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
    return int(a)

def choisirFormatEntree():
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
    
    while not ('1'<= a <='3'):
        a=input("\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
    return int(a)

def choisirFormatSortie(entree):
    indice=entree-1
    
    liste_format=["CSV","JSON","XML"]
    new_liste=[]
    os.system('clear')
    print("\t\t\t\t"+"_"*53)
    print("\t\t\t\t| {0:50}|".format(" Choisir le format de sortie des données valides"))
    print("\t\t\t\t"+"-"*53)
    c=1
    for i in range(len(liste_format)):
        if i != indice:
            print("\t\t\t\t| {0:1} . {1:46}|".format(c,"Fichier "+liste_format[i]))
            new_liste.append(liste_format[i])
            c+=1
    print("\t\t\t\t"+"_"*53)
    print("\t\t\t\t"+" PS: Les données invalides vont être dans le format non choisi ")
    a=input("\t\t\t\tChoix : ")
    
    while not ('1'<= a <='2'):
        a=input("\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
    a=int(a)
    autre=0
    if a==1:
        autre==2
    else:
        autre==1
    
    return new_liste[a-1],new_liste[autre-1]
 

def afficherSous_Menu3():
    os.system('clear')
    print("\t\t\t\t"+"_"*53)
    print("\t\t\t\t| {0:50}|".format("          Afficher les informations             "))
    print("\t\t\t\t"+"-"*53)
    print("\t\t\t\t| {0:50}|".format(" 1. Afficher les informations personnelles"))
    print("\t\t\t\t| {0:50}|".format(" 2. Afficher les notes"))
    print("\t\t\t\t| {0:50}|".format(" 3. Retour"))
    print("\t\t\t\t"+"_"*53)
    print("\n")
    a=input("\t\t\t\t Choix : ")
    
    while not ('1'<= a <='3'):
        a=input("\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
    return int(a)

def afficherSous_Menu4():
    os.system('clear')
    print("\t\t\t\t"+"_"*53)
    print("\t\t\t\t| {0:50}|".format("          options d\'affichage                  "))
    print("\t\t\t\t"+"-"*53)
    print("\t\t\t\t| {0:50}|".format(" 1. Afficher par rang de 5"))
    print("\t\t\t\t| {0:50}|".format(" 2. Choisir un rang personnalisé"))
    print("\t\t\t\t| {0:50}|".format(" 3. Retour"))
    print("\t\t\t\t"+"_"*53)
    print("\n")
    a=input("\t\t\t\t Choix : ")
    
    while not ('1'<= a <='3'):
        a=input("\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
    return int(a)

def afficherSous_Menu2(resultat):
    os.system('clear')
    print("\t\t\t\t"+"_"*53)
    print("\t\t\t\t| {0:50}|".format("          Modifier une information invalide     "))
    print("\t\t\t\t"+"-"*53)
    print("\t\t\t\t| {0:50}|".format(" Choisissez un paramettre : "))
    for i in range(len(resultat[7])):
        print("\t\t\t\t|  {0:3}. {1:44}|".format(str(i+1),resultat[7][i]))
    print("\t\t\t\t|  {0:3}. {1:44}|".format(str(len(resultat[7])+1),"Retour"))
   
    
    print("\t\t\t\t"+"_"*53)
    print("\n")
    a=input("\t\t\t\t Choix : ")
    
    while not ('1'<= a <= str(len(resultat[7])+1)):
        a=input("\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
    return int(a)-1

def colorerNote(note):
    chaine_note="D:"
    notes_devoirs=note[0]
    for i in range(len(notes_devoirs)):
        chaine_note+=notes_devoirs[i]+"|"
        
    chaine_note+="E:"+note[1]
    
    moy=str(calculerMoyenne(note))
    if len(moy)>5:
        moy=moy[:5]
        
    chaine_note+="->"+moy
  
    return chaine_note


def returnMoyenne(donnee):
  return donnee[6]

def recupererIndex(donnee_valide):
    liste_moyenne={}
    liste_index,liste=[],[]
    a=0
    for donnee in donnee_valide:
        moyenne=calculerMoyenne(donnee[6]["MATH"])+calculerMoyenne(donnee[6]["PC"])+calculerMoyenne(donnee[6]["HG"])+calculerMoyenne(donnee[6]["FRANCAIS"])+calculerMoyenne(donnee[6]["ANGLAIS"])+calculerMoyenne(donnee[6]["SVT"])
        moyenne=moyenne/6
        liste_moyenne[a]=moyenne
        liste.append([donnee[0],donnee[1],donnee[2],donnee[3],donnee[4],donnee[5],moyenne])
        a+=1 
    liste_moyenne = dict(sorted(liste_moyenne.items(), key=lambda item:item[1],reverse=True))
   
    for i,j in liste_moyenne.items():
        liste_index.append(i)
    return liste_index,liste
    
def affichagePremier(donnee_valide):
    os.system('clear')
    liste_donnee=recupererIndex(donnee_valide)
    index=liste_donnee[0]
    index=index[:5]
    donnee=liste_donnee[1]
    print("\n\n")
    print("\t\t\t\t* {0:73}*".format("                      Affichage des cinq premiers                      "))
    print("\t\t\t\t"+"-"*73)
    print("\t\t\t\t| {0:8} | {1:10} |{2:13} |{3:12} |{4:7} |{5:8} |".format("Numero","Nom","Prénom","Date","Classe","Notes"))
    print("\t\t\t\t"+"-"*73)
    for i in index:
        print("\t\t\t\t| {0:8} | {1:10} |{2:13} |{3:12} |{4:7} |{5:8.2f} |".format(donnee[i][1],donnee[i][2],donnee[i][3],donnee[i][4],donnee[i][5],donnee[i][6]))
    print("\t\t\t\t"+"-"*73)  
    
def affichageDonneeValide1(donnee_valide,rang):
    os.system('clear')
    a=0
    print("\t\t\t\t Nombres de données valides : ",len(donnee_valide))
    print("\t\t\t\t"+"-"*63)
    print("\t\t\t\t| {0:8} | {1:10} |{2:13} |{3:12} |{4:7} |".format("Numero","Nom","Prénom","Date","Classe"))
    print("\t\t\t\t"+"-"*63)
    for i in range(rang):
        a+=1
        print("\t\t\t\t| {0:8} | {1:10} |{2:13} |{3:12} |{4:7} |".format(donnee_valide[i][1],donnee_valide[i][2],donnee_valide[i][3],donnee_valide[i][4],donnee_valide[i][5]))
    print("\t\t\t\t"+"-"*63)
    

def affichageDonneeValide2(donnee_valide,rang):
    os.system('clear')
    a=0
    print("| {0:8} |{1:33} | {2:33} | {3:33}| {4:33}| {5:33}| {6:33}|".format("Numero","Math","PC","HG","Francais","Anglais","SVT"))
    for i in range(rang):
        a+=1
        print("| {0:8} |{1:30} | {2:30} | {3:30}| {4:30}| {5:33}| {6:33}|".format(donnee_valide[i][1],colorerNote(donnee_valide[i][6]["MATH"]),colorerNote(donnee_valide[i][6]["PC"]),colorerNote(donnee_valide[i][6]["HG"]),colorerNote(donnee_valide[i][6]["FRANCAIS"]),colorerNote(donnee_valide[i][6]["ANGLAIS"]),colorerNote(donnee_valide[i][6]["SVT"])))


def creerXML(donnee_valide,option):
    fichierXML="resultat.xml"
    documentXml = open(fichierXML, 'w')
    documentXml.write('<?xml version="1.0" encoding="ISO-8859-1" ?>' + "\n")
    documentXml.write('<Eleve>' + "\n")
    balise=["Code","Numero","Nom","Prenom","Date_Naissance","Classe","Notes"]
    for i in range(len(donnee_valide)):
        balise_code="\t<"+balise[0]+">"+donnee_valide[i][0]+"</"+balise[0]+">\n"
        balise_numero="\t<"+balise[1]+">"+donnee_valide[i][1]+"</"+balise[1]+">\n"
        balise_nom="\t<"+balise[2]+">"+donnee_valide[i][2]+"</"+balise[2]+">\n"
        balise_prenom="\t<"+balise[3]+">"+donnee_valide[i][3]+"</"+balise[3]+">\n"
        balise_date="\t<"+balise[4]+">"+donnee_valide[i][4]+"</"+balise[4]+">\n"
        balise_classe="\t<"+balise[5]+">"+donnee_valide[i][5]+"</"+balise[5]+">\n"
        if option==1:
            balise_note="\t<"+balise[6]+">\n"
            for key,values in donnee_valide[i][6].items():
                for j in values[0]:
                    note="\t\t<note matiere='"+key+"' type_note='devoir'> "+j+ "</note>\n"
                    balise_note+=note
                note="\t\t<note matiere='"+key+"' type_note='exam'> "+values[1]+ "</note>\n"    
                balise_note+=note
            balise_note+="</"+balise[6]+">\n"
        else:
            balise_note="\t<"+balise[6]+">"+donnee_valide[i][6]+"</"+balise[6]+">\n"    
        documentXml.write('<Element>\n' + balise_code+balise_numero+balise_nom+balise_prenom+balise_date+balise_classe+balise_note+"</Element> \n")
        
    documentXml.write('</Eleve>' + "\n")  
    documentXml.close()
    
    return 'resulat.xml'
    
def creerCSV(donnee_valide):
    with open('resultat.csv',"w") as result :
        writer=csv.writer(result)
        #Definir les entetes
        entete=["Code","Numero","Nom","Prenom","Date_Naissance","Classe","Notes"]
        writer.writerow((entete[1],entete[2],entete[3],entete[4],entete[5],entete[6]))
        for i in donnee_valide:
            writer.writerow((i[1],i[2],i[3],i[4],i[5],i[6]))
    return 'resulat.csv'

def creerJSON(donnee):
    cle=["Code","Numero","Nom","Prenom","Date_Naissance","Classe","Notes"]
    #Recuperer les entetes
    element,liste={},[]
    documentJson= open("resulat.json", 'w')
        
    for i in range(len(donnee)):
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
    return 'resulat.json'

    
def transformer_CSV_XML(fichier_csv):
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
    
def transformer_CSV_JSON(fichier_csv):
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

def recupererDonneeJson(fichierjson):
    donnee,liste_donnee=[],[]
    with open(fichierjson) as f:
        data = json.load(f)
    for i in data:
        for j in i.values():
            donnee.append(j)
        liste_donnee.append(donnee)
        donnee=[]
    return liste_donnee

def recupererDonneeXLM(fichierxml):
    liste_donnee=[]
    donnee=[]
    tree = etree.parse(fichierxml)
    root = tree.getroot()
    for element in root:    
        for j in element:
            donnee.append(str(j.text))
        liste_donnee.append(donnee)
        donnee=[]
    return liste_donnee
   

def affichageDonneeInvalide(donnee_invalide,rang):
    os.system('clear')
    print("| {0:16} | {1:15} |{2:20} |{3:12} |{4:7} |{5:111} |{6:55} |".format("Numero","Nom","Prénom","Date","Classe","Notes","Problèmes"))
    for i in range(1,rang):
        print("| {0:16} | {1:15} |{2:20} |{3:12} |{4:7} |{5:111} |{6:55} |".format(donnee_invalide[i][1],donnee_invalide[i][2],donnee_invalide[i][3],donnee_invalide[i][4],donnee_invalide[i][5],donnee_invalide[i][6],str(donnee_invalide[i][7])))
       
def modifierInfo(donnee,numero,indice,valeur):
    existe=False
    ind=0
    for i in range(len(donnee)):
        if donnee[i][1]==numero:
            existe=True
            ind=i
    if not existe:
        return False

    print(donnee[ind][indice])
    donnee[ind][indice]=valeur
    print(donnee[ind][indice])
    return True

           
def rechercherInfo(donnee1,donnee2,numero):
    os.system('clear')
    for i in range(len(donnee1)):
        if donnee1[i][1]==numero:
            return donnee1[i] 
    for i in range(len(donnee2)):
        if donnee2[i][1]==numero:
            return donnee2[i] 
    return []

def afficherDonnee(donnee):
    print("| {0:16} | {1:15} |{2:20} |{3:12} |{4:7} |{5:111} |".format("Numero","Nom","Prénom","Date","Classe","Notes"))
    print("| {0:16} | {1:15} |{2:20} |{3:12} |{4:7} |{5:111} |".format(donnee[1],donnee[2],donnee[3],donnee[4],donnee[5],str(donnee[6])))
