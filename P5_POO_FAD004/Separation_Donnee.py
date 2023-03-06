#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:26:37 2023

@author: aissatou
"""
import datetime
import Eleve as E

    
class Separation_Donnee():
    
      
    def verifierNumero(self,Eleve):
        if len(Eleve.get_numero())!=7 :
            return False,'Ne contient pas 7 caracteres'
        if not Eleve.get_numero().isalnum():
            return False,'Contient des caracteres spéciaux'
        if not Eleve.get_numero().isupper():
            return False,'Contient des caracteres en minuscules'
        return True,''
    

    def verifierClasse(self,Eleve):
        #Enlever les espaces
        Eleve.set_classe(Eleve.get_classe().replace(" ",""))
        if len(Eleve.get_classe())< 1:
            return False,'Classe non reinseignée'
        if not ('3' <= Eleve.get_classe()[0]<='6'):
            return False,'Classe ne se situe pas entre l\'intervalle 6em - 3em'
        if Eleve.get_classe()[-1] not in ['A','B','a','b']:
            return False,'Classe ne se situe pas entre l\'intervalle A et B'
        Eleve.set_classe(Eleve.get_classe()[0]+"em"+Eleve.get_classe()[-1])
        return True,''

    
    def verifierNom(self,Eleve):
        if len(Eleve.get_nom())==0:
            return False,'Vide'
        if len(Eleve.get_nom())<1:
            return False,'N\'atteint pas pas le nombre de caractères requis '
        if not Eleve.get_nom().replace(" ","").isalpha():
           return False,'Contient des caractères non autorisés'
        return True,''

    def verifierPrenom(self,Eleve):
        if len(Eleve.get_prenom())==0:
            return False,'Vide'
        if len(Eleve.get_prenom())<2:
            return False,'N\'atteint pas pas le nombre de caractères requis '
        if not Eleve.get_prenom().replace(" ","").isalpha():
           return False,'Contient des caractères non autorisés'
        return True,''
    
    def verifierDate(self,Eleve):
        if len(Eleve.get_date_naissance())==0:
            return False,'Date vide'
        date=Eleve.get_date_naissance().lstrip()
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
            Eleve.set_date_naissance(date1)
            return True,''
        except :
            return False,'La date saisie est incorrecte' 

    def decomposerNote(self,Eleve):
    	chaine=Eleve.get_notes().replace(" ","")
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

    def verifierNote(self,Eleve,notes):
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
    		Eleve.set_notes(dico_note)
    		return True,''
    	else :
    		return False,problemes
            
    def verifierDonnee(self,Eleve):
        #La fonction prend une liste 
        probleme=[]
        isValide=True
        resultat=self.verifierNumero(Eleve)
        if not resultat[0]:
            probleme.append(["Numero",resultat[1]])
            isValide=False  
       
        resultat=self.verifierNom(Eleve)
        if not resultat[0]:
            probleme.append(["Nom",resultat[1]])
            isValide=False 
 
        resultat=self.verifierPrenom(Eleve)
        if not resultat[0]:
            probleme.append(["Prenom",resultat[1]])
            isValide=False  
    
        resultat=self.verifierDate(Eleve)
        if not resultat[0]:
            probleme.append(["Date",resultat[1]])
            isValide=False 
        date=resultat[1]
   
        resultat=self.verifierClasse(Eleve)
        if not resultat[0]:
            probleme.append(["Classe",resultat[1]])
            isValide=False 


        resultat=self.verifierNote(Eleve,self.decomposerNote(Eleve))
        if not resultat[0]:
            probleme.append(["Note",resultat[1]])
            isValide=False
      
        return isValide,probleme	
    
    def trierDonnee(self,liste_eleve):  
        donnee_valide,donnee_invalide=[],[]  
        for Eleve in liste_eleve:
            result=self.verifierDonnee(Eleve)
            isValide=result[0]       
            if isValide:
                donnee_valide.append(Eleve)
            else:
                Eleve.set_problemes(result[1])
                donnee_invalide.append(Eleve)
        return donnee_valide,donnee_invalide
    
    def calculerMoyenne(self,note):
        somme_note,moyenne=0,0
        notes_devoirs=note[0]
        notes_exam=float(note[1])
        
        for i in range(len(notes_devoirs)):
            somme_note+=float(notes_devoirs[i])
            
        moyenne=(((somme_note/len(note[0])) + 2*notes_exam)/3) 
        
        return moyenne
    
    def recupererIndex(self,liste_eleve):
        liste_moyenne={}
        liste_index,liste=[],[]
        a=0
        moyenne=0
        for eleve in liste_eleve:
            moyenne=0
            for cle in eleve.get_notes().keys():
                moyenne+=self.calculerMoyenne(eleve.get_notes()[cle])
            moyenne=moyenne/len(eleve.get_notes())
            liste_moyenne[a]=(moyenne)
            eleve.set_moyenne(moyenne)
            liste.append(eleve)
            a+=1 
        liste_moyenne = dict(sorted(liste_moyenne.items(), key=lambda item:item[1],reverse=True))
       
        for i,j in liste_moyenne.items():
            liste_index.append(i)
            
        return liste_index
               
    def rechercherInfo(self,liste_eleve,eleve):
        #On recherche l element dans le données valides
        for i in range(len(liste_eleve[0])):
            if liste_eleve[0][i].get_numero()==eleve.get_numero():
                return liste_eleve[0][i],'valide'
        #On recherche l element dans le données invalides
        for i in range(len(liste_eleve[1])):
            if liste_eleve[1][i].get_numero()==eleve.get_numero():
                return liste_eleve[1][i],'invalide'
        return []

    def ajouterDonnee(self,liste_eleve):
        eleve=E.Eleve('ABBDYY','','','','','','')
        
        verifierDonnee=[]
        eleve.set_numero(input('Saisir un numero contenant 7 caracteres majuscule et/ou numeriques : '))
        verifierDonnee=self.verifierNumero(eleve)
        while not verifierDonnee[0]:
            print(verifierDonnee[1])
            eleve.set_numero(input('Saisir un numero contenant 7 caracteres majuscule et/ou numeriques : '))
            verifierDonnee=self.verifierNumero(eleve)
       
        eleve.set_nom(input('Saisir un nom contenant minimum 2 caracteres : '))
        verifierDonnee=self.verifierNom(eleve)
        while not verifierDonnee[0]:
            print(verifierDonnee[1])
            eleve.set_nom(input('Saisir un nom contenant minimum 2 caracteres : '))
            verifierDonnee=self.verifierNom(eleve)
            
        eleve.set_prenom(input('Saisir un prénom contenant minimum 3 caracteres : '))
        verifierDonnee=self.verifierPrenom(eleve)
        while not verifierDonnee[0]:
            print(verifierDonnee[1])
            eleve.set_prenom(input('Saisir un prénom contenant minimum 3 caracteres : '))
            verifierDonnee=self.verifierPrenom(eleve)
       
        eleve.set_date_naissance(input('Saisir la date de naissance sous le format jj/mm/aa : '))
        verifierDonnee=self.verifierDate(eleve)
        while not verifierDonnee[0]:
            print(verifierDonnee[1])
            eleve.set_date_naissance(input('Saisir la date de naissance sous le format jj/mm/aa : '))
            verifierDonnee=self.verifierDate(eleve)
       
      
        eleve.set_classe(input('Saisir la classe entre 6 em et 3em A ou B : '))
        verifierDonnee=self.verifierClasse(eleve)
        while not verifierDonnee[0]:
            print(verifierDonnee[1])
            eleve.set_classe(input('Saisir la classe entre 6 em et 3em A ou B : '))
            verifierDonnee=self.verifierClasse(eleve)
       
        
        print("Saisir la note sous le format nom_matiere[note_devoir_1 |note_devoir_2 |note_devoir_n... : note_examen]")
        eleve.set_notes(input("Les matieres sont separées par le caracteres \'#\': "))
        verifierDonnee=self.verifierNote(eleve,self.decomposerNote(eleve))
        while not verifierDonnee[0]:
            print(verifierDonnee[1])
            eleve.set_notes(input("Veuillez respecter le format defini :"))
            verifierDonnee=self.verifierNote(eleve,self.decomposerNote(eleve))
       
        liste_eleve.append(eleve)
        print("Les données ont été enregistrées")
        
              
    def modifierDonneeInvalide(self,liste_eleve,eleve):
        resultat=self.rechercherInfo(liste_eleve,eleve)
        if resultat==[]:
            return False,'Le numero saisie est incorrecte'
        if resultat[1]!='invalide':
            return False,'Cette donnée n\'appartient pas aux donnees invalides'
        #On initialise les données invalides avec leurs anciennes valeurs
        
        champ_invalide=eleve.get_problemes()
        problemes=eleve.get_problemes()
        print("\t"+"Problèmes rencontrés :")
        print("\t"+"-"*140)
        print("\t| {0:13} | {1:120} |".format("Champs","Raisons d\'invalidité"))
        print("\t"+"-"*140)
        for i in range(len(problemes)):
            print("\t| {0:13} | {1:120} |".format(problemes[i][0],str(problemes[i][1]).replace(",","").replace("[","").replace("(","").replace("'","").replace('"',"").replace(")","").replace("]","")))
        print("\t"+"-"*140)
        for i in range(len(champ_invalide)):
            if champ_invalide[i][0]=='Numero':
                eleve.set_numero(input('Saisir un numero contenant 7 caracteres majuscule et/ou numeriques : '))
                verification=self.verifierNumero(eleve)
                while not verification[0]:
                    print(verification[1])
                    eleve.set_numero(input('Saisir un numero contenant 7 caracteres majuscule et/ou numeriques : '))
                    verification=self.verifierNumero(eleve)
                    
            if champ_invalide[i][0]=='Nom':
                eleve.set_nom(input('Saisir un nom contenant minimum 2 caracteres : '))
                verification=self.verifierNom(eleve)
                while not verification[0]:
                    print(verification[1])
                    eleve.set_nom(input('Saisir un nom contenant minimum 2 caracteres : '))
                    verification=self.verifierNom(eleve)
                    
            if champ_invalide[i][0]=='Prenom':
                eleve.set_prenom(input('Saisir un prénom contenant minimum 3 caracteres : '))
                verification=self.verifierPrenom(eleve)
                while not verification[0]:
                    print(verification[1])
                    eleve.set_prenom(input('Saisir un prénom contenant minimum 3 caracteres : '))
                    verification=self.verifierPrenom(eleve)
                    
            if champ_invalide[i][0]=='Date':
                eleve.set_date_naissance(input('Saisir la date de naissance sous le format jj/mm/aa : '))
                verification=self.verifierDate(eleve)
                while not verification[0]:
                    print(verification[1])
                    eleve.set_date_naissance(input('Saisir la date de naissance sous le format jj/mm/aa : '))
                    verification=self.verifierDate(eleve)
                
            if champ_invalide[i][0]=='Classe':
                eleve.set_classe(input('Saisir la classe entre 6 em et 3em A ou B : '))
                verification=self.verifierClasse(eleve)
                while not verification[0]:
                    print(verification[1])
                    eleve.set_classe(input('Saisir la classe entre 6 em et 3em A ou B : '))
                    verification=self.verifierClasse(eleve)
            
            if champ_invalide[i][0]=='Note': 
                print("Saisir la note sous le format nom_matiere[note_devoir_1 |note_devoir_2 |note_devoir_n... : note_examen]")
                eleve.set_notes(input("Les matieres sont separées par le caracteres \'#\': "))
                verification=self.verifierNote(eleve,self.decomposerNote(eleve))
                while not verification[0]:
                    print(verification[1])
                    eleve.set_notes(input("Veuillez respecter le format defini :"))
                    verification=self.verifierNote(eleve,self.decomposerNote(eleve))
                
        indexe=0
        for i in range(len(liste_eleve[1])):
            if liste_eleve[1][i].get_numero()==eleve.get_numero():
                indexe=i
                break
        liste_eleve[1].remove(liste_eleve[1][indexe])
        liste_eleve[0].append(eleve)
        return True,'La donnée appartient maintenant aux données valides !!!'  
    
