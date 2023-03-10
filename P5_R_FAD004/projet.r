#setwd("/home/aissatou/Bureau/Sonatel Academy/004 R") 
library(stringr)
liste_donnee <- read.csv("Donnée.csv",sep=",",header=TRUE)

verifierNumero <- function(numero){
  if( nchar(numero) != 7)
    return(F)
  return(str_detect(numero, "[A-Z0-9]{7}"))
}

verifierNom <- function(nom){
  if(nchar(nom)<2 ){
    return(F)
  }
  motif<- "^[[:alpha:]]{2,}"
  if (is.na(str_match(nom, motif)))
    return(F)
  if (str_match(nom, motif) == nom)
    return(T)
  else
    return(F)
}

verifierPrenom <- function(prenom){
  if(nchar(prenom)<3 )
  {
    return(F)
  }
  motif<- "^[[:alpha:]]{3,}"
  if (is.na(str_match(prenom, motif)))
    return(F)
  if (str_match(prenom, motif)== prenom)
    return(T)
  else
    return(F)
}

verifierClasse <- function(classe){
  motif <- "[3-6]{1}[[:alpha:]]+[aAbB]$"
  classe=str_replace_all(classe, " ", "")
  if (is.na(str_extract(string = classe, pattern = motif)))
  {
    return ('')
  }
  classe=
    return(paste(substring(classe,1,1),"em",str_to_upper(substring(classe,nchar(classe),nchar(classe))) ,sep=""))
}

verifierDate <- function(date){
  if(str_detect(date, "[[:alpha:]]"))
  {
    return('')
  }
  
  date1<-''
  liste_format=c("%d/%m/%Y","%d-%m-%Y","%d:%m:%Y","%d %m %Y","%d_%m_%Y","%;%m;%Y","%d|%m|%Y")
  for( format in liste_format )
  {
    date1<-as.Date(date,format)
    if (!is.na(date1))
      break
  }
  if (!is.na(date1))
  {
    date1=str_replace_all(date1, "-", "/")
    return(date1)
  }     
  else return('')
}

decomposerNote <- function(note){
  format_note <- "[[:alpha:]]+[\\[ ]+([:digit:]+[\\ , ]?[\\ . ]?[:digit:]+[\\ | ]?)+[\\: ]{1}[:digit:]+[\\ , ]?[\\ . ]?[:digit:]?[\\] ]?"
  liste_note=str_extract_all(note, format_note)[[1]]
  if(length(liste_note)==0)
    return('')
  return(liste_note)
}

verifierNote <- function(liste_note){
  liste=list()
  liste_matiere=c("MATH","FRANCAIS","FRANÇAIS","SVT","ANGLAIS","HG","PC","SCIENCE_PHYSIQUE")
  nom_matiere  <- "[[:alpha:]]+"
  format_note <- "[:digit:]+[\\ , ]?[\\ . ]?[:digit:]+" 
  for (i in liste_note){
    matiere=str_extract_all(i,nom_matiere)[[1]]
    
    if(!any(liste_matiere==str_to_upper(matiere)))
    {
      return('')
    }
    notes=str_extract_all(i,format_note)[[1]]
    liste[[matiere]]<-notes
  }
  return(liste)
}

a<-0
b<-0
donnee_valide<-data.frame(CODE=character(),Numero=character(),Nom=character(), Prénom=character(), Date.de.naissance=character(),Classe=character(),Note=character())
donnee_invalide<-data.frame(CODE=character(),Numero=character(),Nom=character(), Prénom=character(), Date.de.naissance=character(),Classe=character(),Note=character())
taille<-length(liste_donnee[,1])
for (i in 1:taille){
  isValide <- T
  if(!verifierNumero(liste_donnee[,2][i])){
    isValide<-F
  }
  if(!verifierNom(liste_donnee[,3][i])){
    isValide<-F
  }
  if(!verifierPrenom(liste_donnee[,4][i])){
    isValide<-F
  }
  date<-verifierDate(liste_donnee[,5][i])
  if(date==''){
    isValide<-F
  }
  classe<-verifierClasse(liste_donnee[,6][i])
  if(classe=='')  {
    isValide<-F
  }
  note=verifierNote(decomposerNote(liste_donnee[,7][i]))
  if( note[1] =='')
  {
    isValide<-F
  }
  if (isValide){
    a=a+1
    donnee_valide[a,]<-liste_donnee[i,]
  }
  else{
    b=b+1
    donnee_invalide[b,]<-liste_donnee[i,]
  }
  
}
print(a)
View(donnee_invalide)
View(donnee_valide)
write.csv(donnee_valide,"Valide_CSV.csv")
write.csv(donnee_invalide,"Invalide_CSV.csv")

library(jsonlite)
write_json(donnee_valide, "Valide_JSON.json")
write_json(donnee_invalide,"Invalide_JSON.json")
library(yaml)
write_yaml(donnee_valide, "Valide_YAML.yaml")
write_yaml(donnee_invalide,"Invalide_YAML.yaml")
library(XML)
write.xml(donnee_valide, "Valide_XML.xml")
write.xml(donnee_invalide,"Invalide_XML.xml")