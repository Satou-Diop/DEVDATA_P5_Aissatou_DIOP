#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 07:38:45 2023

@author: aissatou
"""


class Eleve:
    
    def __init__(self,code,numero,nom,prenom,date_naissance,classe,notes):
        self.code=code
        self.numero=numero
        self.nom = nom
        self.prenom=prenom
        self.date_naissance=date_naissance
        self.classe=classe
        self.notes=notes
        
    #On definit les getters 
    def get_code(self):
        return self.code
    
    def get_numero(self):
        return self.numero
    
    def get_nom(self):
        return self.nom
    
    def get_prenom(self):
        return self.prenom
    
    def get_date_naissance(self):
        return self.date_naissance
    
    def get_classe(self):
        return self.classe
    
    def get_notes(self):
        return self.notes
    
    def get_moyenne(self):
        return self.moyenne
    
    def get_problemes(self):
        return self.problemes

      
    #On definit les getters
    def set_code(self, x):
        self._code = x
        
    def set_numero(self, x):
            self.numero = x
            
    def set_nom(self, x):
            self.nom = x
            
    def set_prenom(self, x):
            self.prenom = x
            
    def set_date_naissance(self, x):
            self.date_naissance = x
            
    def set_classe(self, x):
            self.classe = x
            
    def set_notes(self, x):
            self.notes = x
    
    def set_moyenne(self, x):
            self.moyenne = x
            
    def set_problemes(self, x):
            self.problemes = x