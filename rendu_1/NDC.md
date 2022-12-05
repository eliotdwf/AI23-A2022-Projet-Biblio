# Projet Biblio - Note de clarification

## Objectif
Concevoir un système de gestion pour une bibliothèque municipale qui souhaite informatiser ses 
activités : catalogage, consultations, gestion des utilisateurs, prêts, etc.

## Objets
- ressource (livre, film, enregistrement musical)
- contributeur
- utilisateur (membre du personnel, adhérent)
- prêt

## Propriétés des objets

### Ressource
- code
- titre
- liste de contributeurs
- date d’apparition
- éditeur
- genre
- code de classification
- état (neuf, bon, abîmé, perdu)

#### Livre
- ISBN
- résumé
- langue

#### Film
- longueur
- langue
- synopsis

#### Enregistrement musical
- longueur

### Contributeur
- nom
- prénom
- date de naissance
- nationalité

### Utilisateur
- login
- mot de passe
- nom
- prenom
- email
- adresse
- fonctions d’administration (oui, non)

#### Membre du personnel : pas de propriété supplémentaire.

#### Adhérent
- date de naissance
- numéro de téléphone
- carte (active, inactive)

### Prêt
- date
- durée

## Contraintes

### Ressource



### Prêt



## Fonctions

