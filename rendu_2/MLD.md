# Modèle Logique de Données

### Adherent(#login:string, mdp:string, nom:string, prenom:string, mail:string, adresse:string, ddn:date, num_tel:string, carte_active:boolean, nb_emprunts:integer)
> carte NOT NULL, nom NOT NULL, prenom NOT NULL, email UNIQUE NOT NULL, mdp NOT NULL, ddn NOT NULL  
> nb_emprunts >= 0

### Personnel(#login:string, mdp:string, nom:string, prenom:string, mail:string, adresse:string)
> nom NOT NULL, prenom NOT NULL email UNIQUE NOT NULL, mdp NOT NULL

### Degradation(#id:integer, remboursement_fait:boolean, adherent=>Adherent.login)
> remboursement_fait NOT NULL

### Retard(#id:integer, debut_suspension:Date, nb_jours_retard:integer, adherent=>Adherent.login)
> debut_suspension NOT NULL, nb_jours_retard NOT NULL et > 0

### Exemplaire(#id:integer, code=>Ressources.code, etat:{Neuf, Bon, Abimé, Perdu})
> etat NOT NULL

### Pret(#exemplaire=>Exemplaire.id, #adherent=>Adherent.login, #date:Date, duree:integer)
> durée NOT NULL, check(Projection(Jointure(Pret, Adherent, Pret.adherent = Adherent.id), Adherent.nb_emprunts) < 5)

### Ressources(#code:string, titre:string, date_apparition:date, editeur:string, genre:string, code_classification:string)
> titre NOT NULL, date_apparition NOT NULL, code_classification NOT NULL

### Livre(#id=>Ressources.code, ISBN:string, resume:string, langue:string)
> ISBN NOT NULL, langue NOT NULL

### Film(#id=>Ressources.code, longueur:integer, langue:string, synopsis:string)
> longueur NOT NULL, langue NOT NULL

### EnregistrementMusical(#id=>Ressources.code, longueur:integer)
> longueur NOT NULL

### Contributeur(#id:integer, nom:string, prenom:string, ddn:date, nationalite:string)
> nom NOT NULL, prenom NOT NULL, ddn NOT NULL

### Contribution(#id=>Contributeur.id, #code=>Ressources.code, type:{Compositeur, Realisateur, Auteur, Interprete, Acteur})
> type NOT NULL

## Choix héritage:
- Héritage par classe fille pour les tables Adhérent et Personnel car la classe mère est abstraite et parce que la classe fille Adhérent possède des associations.
- Héritage par classe fille pour les tables Degradation et Retard car une Sanction est de type Degradation OU Retard mais pas les 2 (héritage exclusif), de plus la classe Sanction est abstraite.
- Héritage par référence pour la table Ressource qui n'est pas abstraite et permet de mettre en commun beaucoup d'attributs, tout en facilitant l'association entre Ressource et Exemplaire.

