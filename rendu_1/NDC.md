(en markdown svp)
# Projet Biblio - Note de clarification

## Objectif
Concevoir un système de gestion pour une bibliothèque municipale qui souhaite informatiser ses activités : catalogage, consultations, gestion des utilisateurs, prêts, etc.

## Objets
- Ressource  
  > Ce sont les différentes offres de la bibliothèques. Ces ressources sont de 3 catégories : Livre, Film et Enregistrement musicaux.
- Contributeur
  > Ce sont les "personnes" à l'origine d'une ressource. 
- Utilisateur
  > De différentes catégories : adhérent ou membre du staff.
- Prêt


# Propriétés des objets

## **Ressource**
- code (**unique**)  
- titre  
- liste de contributeurs  
- date d’apparition  
- éditeur  
- genre  
- code de classification 
- état (neuf, bon, abîmé, perdu) 

#### **Livre**
- ISBN  
- résumé  
- langue

#### **Film**
- longueur
- langue
- synopsis

#### **Enregistrement musical**
- longueur

## **Contributeur**
- nom
- prénom
- date de naissance
- nationalité
- type (auteur, compositeur, interprète, acteur, réalisateur)

## **Utilisateur**
- login
- mot de passe
- nom
- prenom
- email
- adresse
- fonctions d’administration (oui, non)

### **Membre du personnel**
  > Pas de propriété supplémentaire.

#### **Adhérent**
- date de naissance
- numéro de téléphone
- carte (active, inactive)

## **Prêt**
- date
- durée

# Contraintes

## **Ressources**
    Livre                  -> Les contributeurs sont les auteurs.
    Enregistrement musical -> Les contributeurs sont des compositeurs et des interprètes
    Film                   -> Les contributeurs sont des réalisateurs et des acteurs
- Une ressource n'est empruntable que si celle-ci est en bon état ou neuve.


## **Prêt**
- Chaque emprunt est à durée limitée
- Un utilisateur ne peut emprunter qu'un nombre limité d'oeuvre à la fois
- Un adhérent peut être sanctionné :
  - retard -> impossible d'emprunter pendant le nombre de jour de retard.
  - dégradation ou perte -> impossible d'emprunter tant que le document n'est pas remboursé.
  - En cas de sanction répétées -> mise sur blacklist de l'adhérent.
  
# **Fonctions - Consultation et modifications des données**
## ***Possible uniquement pour les membres du staff***
- Gestion des adhérents
  > Ajouter, modifier ou supprimer
- Gestion des prêts
  > Créer un nouvel emprunt
- Gestion des ressources
  > Description, disponibilité, ajouter ou supprimer, état

## ***Pour tous les utilisateurs***
- La bibliothèque à également besoin de permettre aux adhérents de rechercher des documents et de gérer leurs emprunts
  > Accès à l'état d'un document  
  Consultation et modification du profil  
  Emprunts en cours

