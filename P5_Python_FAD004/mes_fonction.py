"""
@author: Aissatou DIOP
"""
import csv
import os
import datetime
import xml.etree.ElementTree as etree
import json

#TRANSFORMATION DES FICHIERS VERS LES FORMATS DEMANDÉES
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

#FINTRANSFORMATION DES FICHIERS VERS LES FORMATS DEMANDÉES

######################################################

#PARTIE TRAITEMENT DES DIFFERENTS TYPES DE FICHIERS
def recupererDonneeCSV(nom_fichier_csv):
    donnee_csv = csv.reader(open(nom_fichier_csv,"r"))
    donnee=[]
    for i in donnee_csv:
       donnee.append(i)
    return donnee

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

#FIN PARTIE TRAITEMENT DES DIFFERENTS TYPES DE FICHIERS

######################################################

#PARTIE AFFICHAGE DES DIFFERENTS MENUS
def afficherMenu():   
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

def afficherSous_Menu1():
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

def afficherSous_Menu2(resultat):
    print("\n\n\n\t\t\t******************************      Nettoyage de données      ******************************\n")
    print("\t\t\t\t\t\t\t\t"+"_"*53)
    print("\t\t\t\t|\t\t\t\t {0:50}|".format("          Modifier une information invalide     "))
    print("\t\t\t\t\t\t\t\t"+"-"*53)
    print("\t\t\t\t\t\t\t\t| {0:50}|".format(" Choisissez un paramettre : "))
    for i in range(len(resultat[7])):
        print("\t\t\t\t\t\t\t\t|  {0:3}. {1:44}|".format(str(i+1),resultat[7][i]))
    print("\t\t\t\t\t\t\t\t|  {0:3}. {1:44}|".format(str(len(resultat[7])+1),"Retour"))
   
    
    print("\t\t\t\t\t\t\t\t"+"_"*53)
    print("\n")
    a=input("\t\t\t\t\t\t\t\t Choix : ")
    while not a.isdigit():
        a=input("\t\t\t\t\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
    while not ('1'<= a <= str(len(resultat[7])+1)):
        a=input("\t\t\t\t\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
    return int(a)-1

def afficherSous_Menu3():
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

def afficherSous_Menu4():
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

#FIN DE LA PARTIE DES DIFFERENTS MENUS

######################################################

#FONCTIONS DE VÉRIFICATION  DES DONNÉES

def verifierNumero(numero):
    if len(numero)!=7 :
        return False,'Ne contient pas 7 caracteres'
    if not numero.isalnum():
        return False,'Contient des caracteres spéciaux'
    if not numero.isupper():
        return False,'Contient des caracteres en minuscules'
    return True,''

def verifierClasse(classe):
    #Enlever la premiere espace
    classe=classe.replace(" ","")
    if len(classe)< 1:
        return False,'Classe non reinseignée'
    if not ('3' <= classe[0]<='6'):
        return False,'Classe ne se situe pas entre l\'intervalle 6em - 3em'
    if classe[-1] not in ['A','B','a','b']:
        return False,'Classe ne se situe pas entre l\'intervalle A et B'
    return True,classe[0]+"em"+classe[-1]

def verifierNoms(nom,minimum):
    if len(nom)==0:
        return False,'Vide'
    if len(nom)<minimum:
        return False,'N\'atteint pas pas le nombre de caractères requis '
    if not nom.replace(" ","").isalpha():
       return False,'Contient des caractères non autorisés'
    return True,''

def verifierDate(date):
    if len(date)==0:
        return False,'Date vide'
    date=date.lstrip()
    for i in [' ',',',';',':','/','-','_']:
        if i in date:
            date=date.replace(i,'/')
    date=date.split('/')
    if len(date) != 3:
        return False,'La date doit etre composée de trois éléments'
    
    if len(date[2])==4:
        date[2]=date[2][2]+date[2][3]
        
    if not date[0].isnumeric() or not date[1].isnumeric() or  not date[2].isnumeric():
            return False,'La date contient des caracteres non numeriques'   
    try:
        datetest=datetime.datetime(int(date[2]),int(date[1]),int(date[0]))
        data=datetest.strftime("%d /%m /%y")
        date1='/'.join(date)
        return True,date1
    except :
        return False,'La date saisie est incorrecte' 

def decomposerNote(chaine):
	chaine=chaine.replace(" ","")
	liste_matiere=chaine.split("#")
	resultats=[]
	for note in liste_matiere:
		#Verifier les notes vides
		if len(note)>1:
			#Séparer les matieres et les notes
			note=note.split("[")
			if len(note)>1:
				matiere=note[0].upper()
				if 'Ç' in matiere:
					matiere=matiere.replace("Ç","C")
				#Séparer les notes de devoirs et ceux d'examens
				liste=(note[1]).split(":")
				#Voir si on a des notes de devoirs et d'examens
				if len(liste)>1:
					note_devoir=liste[0].split("|")
					note_exams=liste[1].replace("]","")
					resultats.append([matiere,note_devoir,note_exams])
	return resultats 

def verifierNote(notes):
	problemes,dico_note,dico_note2=[],{},{}
	liste_matiere=set()
    
	if len(notes)<1:
		return False,'Notes vides'  	
	for i in range(len(notes)):
		estValide=True
		if notes[i][0] not in ["MATH","FRANCAIS","SVT","ANGLAIS","HG","PC","SCIENCE_PHYSIQUE"]:
			texte="Erreur sur l\'intitulé de la matière \'"+notes[i][0]+"\' ."
			problemes.append(texte)	
		if notes[i][0] not in liste_matiere:
			liste_matiere.add(notes[i][0])
		else:
			texte="La matière \'"+notes[i][0]+"\' est dupliquée"
			problemes.append(texte)	
			continue
		
		for j in range(len(notes[i][1])):
			if "," in notes[i][1][j]:
				notes[i][1][j]=notes[i][1][j].replace(",",".")	
			try:
				if not 0<=float(notes[i][1][j])<=20:
					texte="La note de devoirs \'",notes[i][1][j],"\' en "+notes[i][0]+" n\'est pas compris entre 0 et 20."
					problemes.append(texte)	
			except:
				texte="La note \'"+notes[i][1][j]+"\' en \'"+notes[i][0]+"\' est incorrecte ."
				problemes.append(texte)
		if "," in notes[i][2]:
				notes[i][2]=notes[i][2].replace(",",".")	
		try:
		
			if not 0<=float(notes[i][2])<=20:
				texte="La note d\'examen \'",notes[i][2],"\' en "+notes[i][0]+" n\'est pas compris entre 0 et 20."
				problemes.append(texte)	
		except:
			texte="La note \'"+notes[i][2]+"\' en \'"+notes[i][0]+"\' est incorrecte ."
			problemes.append(texte)
	if problemes==[]:
		for i in notes:
			dico_note[i[0]]=[i[1],i[2]]
		return True,dico_note
	else :
		return False,problemes



#FIN FONCTIONS DE VÉRIFICATION  DES DONNÉES

######################################################

#PARTIE TRAITEMENT  DES DONNÉES
def verifierDonnee(donnee):
    probleme,note=[],[]
    date,classe='',''
    isValide=True
    for i in range(len(donnee)):
        if i==1:
            resultat=verifierNumero(donnee[1])
            if not resultat[0]:
                probleme.append(["Numero",resultat[1]])
                isValide=False  
        if i==2:
            resultat=verifierNoms(donnee[2],1)
            if not resultat[0]:
                probleme.append(["Nom",resultat[1]])
                isValide=False 
        if i==3:
            resultat=verifierNoms(donnee[3],2)
            if not resultat[0]:
                probleme.append(["Prenom",resultat[1]])
                isValide=False  
        if i==4:
            resultat=verifierDate(donnee[4])
            if not resultat[0]:
                probleme.append(["Date",resultat[1]])
                isValide=False 
            date=resultat[1]
        if i==5:
            resultat=verifierClasse(donnee[5])
            if not resultat[0]:
                probleme.append(["Classe",resultat[1]])
                isValide=False 
            classe=resultat[1]
        if i==6:
            resultat=verifierNote(decomposerNote(donnee[6]))
            if not resultat[0]:
                probleme.append(["Note",resultat[1]])
                isValide=False
            note=resultat[1] 
    return isValide,date,classe,note,probleme	

def trierDonnee(liste_donnee):  
    donnee_valide,donnee_invalide=[],[]  
    for donnee in liste_donnee:
        result=verifierDonnee(donnee)
        isValide=result[0]       
        if isValide:
            donnee_valide.append([donnee[0],donnee[1],donnee[2],donnee[3],result[1],result[2],result[3]])
        else:
            donnee_invalide.append([donnee[0],donnee[1],donnee[2],donnee[3],donnee[4],donnee[5],donnee[6].replace(" ",""),result[4]])
    return donnee_valide,donnee_invalide

def calculerMoyenne(note):
    somme_note,moyenne=0,0
    notes_devoirs=note[0]
    notes_exam=float(note[1])
    
    for i in range(len(notes_devoirs)):
        somme_note+=float(notes_devoirs[i])
        
    moyenne=(((somme_note/len(note[0])) + 2*notes_exam)/3) 
    return moyenne

def recupererIndex(donnee_valide):
    liste_moyenne={}
    liste_index,liste=[],[]
    a=0
    moyenne=0
    for donnee in donnee_valide:
	moyenne=0
        for cle in donnee[6].keys():
            moyenne+=calculerMoyenne(donnee[6][cle])
        moyenne=moyenne/len(donnee)
        liste_moyenne[a]=(moyenne)
        liste.append([donnee[0],donnee[1],donnee[2],donnee[3],donnee[4],donnee[5],moyenne])
        a+=1 
    liste_moyenne = dict(sorted(liste_moyenne.items(), key=lambda item:item[1],reverse=True))
   
    for i,j in liste_moyenne.items():
        liste_index.append(i)
    return liste_index,liste
           
def rechercherInfo(donnee,numero):
    #On recherche l element dans le données valides
    for i in range(len(donnee[0])):
        if donnee[0][i][1]==numero:
            return donnee[0][i],'valide'
    #On recherche l element dans le données invalides
    for i in range(len(donnee[1])):
        if donnee[1][i][1]==numero:
            return donnee[1][i],'invalide'
    return []

#FINPARTIE TRAITEMENT DES DONNÉES

######################################################

#PARTIE AFFICHAGE DES RESULTATS APRES TRAITEMENT

def affichageDonneeValide(donnee_valide,rang):
    a=0
    os.system('clear')
    print("\n\n\n\t\t\t******************************      Nettoyage de données      ******************************\n")
    print("\t\t\t\t Nombres de données valides : ",len(donnee_valide))
    print("\t\t\t\t"+"-"*66)
    print("\t\t\t\t| {0:8} | {1:10} | {2:13} | {3:12} | {4:7} |".format("Numero","Nom","Prénom","Date","Classe"))
    print("\t\t\t\t"+"-"*66)
    for i in range(rang):
        a+=1
        print("\t\t\t\t| {0:8} | {1:10} | {2:13} | {3:12} | {4:7} |".format(donnee_valide[i][1],donnee_valide[i][2],donnee_valide[i][3],donnee_valide[i][4],donnee_valide[i][5]))
    print("\t\t\t\t"+"-"*66)
   
def affichageDonneeInvalide(donnee_valide,rang):
    a=0
    print(" Nombres de données valides : ",len(donnee_valide)-1)
    print("-"*171)
    print("| {0:10} | {1:10} |{2:13} |{3:12} |{4:7} |{5:105} |".format("Numero","Nom","Prénom","Date","Classe","Notes"))
    print("-"*171)
    for i in range(1,rang):
        a+=1
        print("| {0:10} | {1:10} |{2:13} |{3:12} |{4:7} |{5:105} |".format(donnee_valide[i][1],donnee_valide[i][2],donnee_valide[i][3],donnee_valide[i][4],donnee_valide[i][5],donnee_valide[i][6]))
    print("-"*171)
    
def affichageCinqPremier(donnee_valide):
    liste_donnee=recupererIndex(donnee_valide)
    index=liste_donnee[0]
    index=index[:5]
    donnee=liste_donnee[1]
    print("\n\n")
    print("\t\t\t\t* {0:73}*".format("                      Affichage des cinq premiers                      "))
    print("\t\t\t\t"+"-"*73)
    print("\t\t\t\t| {0:8} | {1:10} |{2:13} |{3:12} |{4:7} |{5:8} |".format("Numero","Nom","Prénom","Date","Classe","Moyennes"))
    print("\t\t\t\t"+"-"*73)
    for i in index:
        print("\t\t\t\t| {0:8} | {1:10} |{2:13} |{3:12} |{4:7} |{5:8.2f} |".format(donnee[i][1],donnee[i][2],donnee[i][3],donnee[i][4],donnee[i][5],donnee[i][6]))
    print("\t\t\t\t"+"-"*73)  

def afficherNote(donnee_valide,numero):
    donnee,liste_cle,liste_format=[],[],""
    for i in donnee_valide:
        if numero==i[1]:
            donnee=i
            break
    if donnee==[]:
        return False
    notes=donnee[6]
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

def afficherProblemes(donnee_invalide,numero):
    donnee,liste_cle,liste_format=[],[],""
    for i in donnee_invalide:
        if numero==i[1]:
            donnee=i
            break
    if donnee==[]:
        return False,"Le numero saisie n\'appartient pas aux données invalides"
    problemes=donnee[7]
    print("\t"+"-"*140)
    print("\t| {0:13} | {1:120} |".format("Champs","Raisons d\'invalidité"))
    print("\t"+"-"*140)
    for i in range(len(problemes)):
        print("\t| {0:13} | {1:120} |".format(problemes[i][0],str(problemes[i][1]).replace(",","").replace("[","").replace("(","").replace("'","").replace('"',"").replace(")","").replace("]","")))
    print("\t"+"-"*140)
    
def afficherResultatRecherche(ResultatRecherche):
    donnee=ResultatRecherche[0]
    if ResultatRecherche[1]=='valide':
        print("\t\t\t * Informations personelles de l\'éléve : les données sont valides")
        print('\t\t\t'+'-'*83)
        print("\t\t\t| {0:16} | {1:15} |{2:20} |{3:12} |{4:7} |".format("Numero","Nom","Prénom","Date","Classe"))
        print('\t\t\t'+'-'*83)
        print("\t\t\t| {0:16} | {1:15} |{2:20} |{3:12} |{4:7} |".format(donnee[1],donnee[2],donnee[3],donnee[4],donnee[5]))
        print('\t\t\t'+'-'*83)
        print("\n")
        print("* Notes de l\'éléve ")
        print('-'*(23*(len(donnee[6]))))
        for i in donnee[6].keys():    
            print("| {0:20} ".format(i),end="")
        print("|")
        print('-'*(23*(len(donnee[6]))+1))
    
        for i in donnee[6].values():      
            print("| {0:20} ".format(str(i).replace("[","").replace("],"," :").replace("'","").replace("]","")),end="")
        print("|")
        print('-'*(23*(len(donnee[6]))+1))
        
    elif ResultatRecherche[1]=='invalide':
        print("* Informations personelles de l\'éléve : les données sont invalides")
        print('-'*196)
        print("| {0:16} | {1:15} |{2:20} |{3:12} |{4:7} |{5:111} |".format("Numero","Nom","Prénom","Date","Classe","Notes"))
        print('-'*196)
        print("| {0:16} | {1:15} |{2:20} |{3:12} |{4:7} |{5:111} |".format(donnee[1],donnee[2],donnee[3],donnee[4],donnee[5],str(donnee[6])))
        print('-'*196)
        problemes=donnee[7]
        print("\t"+"Problèmes rencontrés :")
        print("\t"+"-"*140)
        print("\t| {0:13} | {1:120} |".format("Champs","Raisons d\'invalidité"))
        print("\t"+"-"*140)
        for i in range(len(problemes)):
            print("\t| {0:13} | {1:120} |".format(problemes[i][0],str(problemes[i][1]).replace(",","").replace("[","").replace("(","").replace("'","").replace('"',"").replace(")","").replace("]","")))
        print("\t"+"-"*140)

#FINPARTIE AFFICHAGE   DES RESULTATS APRES TRAITEMENT

######################################################

#PARTIE AJOUT ET MODIFICATIONS DES DONNÉES 
def ajouterDonnee(donnee_valide):
    num,nom,prenom,date,classe,note='','','','','',''
    verifierDonnee=[]
    num=input('Saisir un numero contenant 7 caracteres majuscule et/ou numeriques : ')
    verifierDonnee=verifierNumero(num)
    while not verifierDonnee[0]:
        print(verifierDonnee[1])
        num=input('Saisir un numero contenant 7 caracteres majuscule et/ou numeriques : ')
        verifierDonnee=verifierNumero(num)
   
    nom=input('Saisir un nom contenant minimum 2 caracteres : ')
    verifierDonnee=verifierNoms(nom,2)
    while not verifierDonnee[0]:
        print(verifierDonnee[1])
        nom=input('Saisir un nom contenant minimum 2 caracteres : ')
        verifierDonnee==verifierNoms(nom,2)
        
    prenom=input('Saisir un prénom contenant minimum 3 caracteres : ')
    verifierDonnee=verifierNoms(prenom,3)
    while not verifierDonnee[0]:
        print(verifierDonnee[1])
        prenom=input('Saisir un prénom contenant minimum 3 caracteres : ')
        verifierDonnee=verifierNoms(prenom,3)
   
    date=input('Saisir la date de naissance sous le format jj/mm/aa : ')
    verifierDonnee=verifierDate(date)
    while not verifierDonnee[0]:
        print(verifierDonnee[1])
        date=input('Saisir la date de naissance sous le format jj/mm/aa : ')
        verification=verifierDate(date)
    date=verifierDonnee[1]
  
    classe=input('Saisir la classe entre 6 em et 3em A ou B : ')
    verifierDonnee=verifierClasse(classe)
    while not verifierDonnee[0]:
        print(verifierDonnee[1])
        classe=input('Saisir la classe entre 6 em et 3em A ou B : ')
        verifierDonnee=verifierClasse(classe)
    classe=verifierDonnee[1]
    
    print("Saisir la note sous le format nom_matiere[note_devoir_1 |note_devoir_2 |note_devoir_n... : note_examen]")
    note=input("Les matieres sont separées par le caracteres \'#\': ")
    verifierDonnee=verifierNote(decomposerNote(note))
    while not verifierDonnee[0]:
        print(verifierDonnee[1])
        note=input("Veuillez respecter le format defini :")
        verifierDonnee=verifierNote(decomposerNote(note))
    note=verifierDonnee[1]
    donnee_valide.append(["ABBDYY",num,nom,prenom,date,classe,note])
    print("Les données ont été enregistrées")
    
def modifierDonneeInvalide(liste,numero):
    resultat=rechercherInfo(liste,numero)
    if resultat==[]:
        return False,'Le numero saisie est incorrecte'
    if resultat[1]!='invalide':
        return False,'Cette donnée n\'appartient pas aux donnees invalides'
    #On initialise les données invalides avec leurs anciennes valeurs
    code,num,nom,prenom,date,classe,note=resultat[0][0],resultat[0][1],resultat[0][2],resultat[0][3],resultat[0][4],resultat[0][5],resultat[0][6]
    champ_invalide=resultat[0][7]
    problemes=resultat[0][7]
    print("\t"+"Problèmes rencontrés :")
    print("\t"+"-"*140)
    print("\t| {0:13} | {1:120} |".format("Champs","Raisons d\'invalidité"))
    print("\t"+"-"*140)
    for i in range(len(problemes)):
        print("\t| {0:13} | {1:120} |".format(problemes[i][0],str(problemes[i][1]).replace(",","").replace("[","").replace("(","").replace("'","").replace('"',"").replace(")","").replace("]","")))
    print("\t"+"-"*140)
    for i in range(len(champ_invalide)):
        if champ_invalide[i][0]=='Numero':
            num=input('Saisir un numero contenant 7 caracteres majuscule et/ou numeriques : ')
            verification=verifierNumero(num)
            while not verification[0]:
                print(verification[1])
                num=input('Saisir un numero contenant 7 caracteres majuscule et/ou numeriques : ')
                verification=verifierNumero(num)
        if champ_invalide[i][0]=='Nom':
            nom=input('Saisir un nom contenant minimum 2 caracteres : ')
            verification=verifierNoms(nom,2)
            while not verification[0]:
                print(verification[1])
                nom=input('Saisir un nom contenant minimum 2 caracteres : ')
                verification=verifierNoms(nom,2)
        if champ_invalide[i][0]=='Prenom':
            prenom=input('Saisir un prénom contenant minimum 3 caracteres : ')
            verification=verifierNoms(prenom,3)
            while not verification[0]:
                print(verification[1])
                prenom=input('Saisir un prénom contenant minimum 3 caracteres : ')
                verification=verifierNoms(prenom,3)
        if champ_invalide[i][0]=='Date':
            date=input('Saisir la date de naissance sous le format jj/mm/aa : ')
            verification=verifierDate(date)
            while not verification[0]:
                print(verification[1])
                date=input('Saisir la date de naissance sous le format jj/mm/aa : ')
                verification=verifierDate(date)
            date=verification[1]
        if champ_invalide[i][0]=='Classe':
            classe=input('Saisir la classe entre 6 em et 3em A ou B : ')
            verification=verifierClasse(classe)
            while not verification[0]:
                print(verification[1])
                classe=input('Saisir la classe entre 6 em et 3em A ou B : ')
                verification=verifierClasse(classe)
            classe=verification[1]
        
        if champ_invalide[i][0]=='Note': 
            print("Saisir la note sous le format nom_matiere[note_devoir_1 |note_devoir_2 |note_devoir_n... : note_examen]")
            note=input("Les matieres sont separées par le caracteres \'#\': ")
            verification=verifierNote(decomposerNote)
            while not verification[0]:
                print(verification[1])
                note=input('Veuillez respecter le format defini :')
            note=verification[1]
       
    indexe=0
    for i in range(len(liste[1])):
        if liste[1][i][1]==numero:
            indexe=i
            break
    liste[1].remove(liste[1][indexe])
    liste[0].append([code,num,nom,prenom,date,classe,date,note])
    return True,'La donnée appartient maintenant aux données valides !!!'  
    
#FINPARTIE AJOUT ET MODIFICATIONS DES DONNÉES

######################################################

#MENU POUR LES CHOIX DE FORMATS DES FICHIERS
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
    while not a.isdigit():
        a=input("\t\t\t\t Veuilez choisir parmi les options ci-dessus : ")
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

#FINMENU POUR LES CHOIX DE FORMATS DES FICHIERS

######################################################
 
#CREATION DES FICHIERS OUTPUT
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
