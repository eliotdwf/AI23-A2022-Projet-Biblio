#changer le module
import sqlite3

#connexion a la BD
conn = sqlite3.connect("../database.db")
cur = conn.cursor()

isAdherent = False
login = ""


def verifierChoix(choix, borneMax):
    while(choix < 1 or choix > borneMax):
        choix = int(input("Choix incorrect, veuillez réessayer : "))


def estAdherent(login, pwd):
    requete = "Select 1 from Adherent where login = ? and mdp = ?"
    cur.execute(requete, (login, pwd))
    return cur.fetchone()

def estPersonnel(login, pwd):
    requete = "Select 1 from personnel where login = ? and mdp = ?"
    cur.execute(requete, (login, pwd))
    return cur.fetchone()


def demanderTypeRessource():
    type = int(input("""Types de ressource:
    1. Film
    2. Livre
    3. Enregistrement musical\nChoix : """))
    verifierChoix(type, 3)
    if(type == 1):
        return "Film"
    elif(type == 2):
        return "Livre"
    elif(type == 3):
        return "Musique"
    else:
        print("ERREUR")
    
def afficherFilms(raws):
    for raw in raws:
        print("{")
        print("\tcode ressource : %d" % raw[0])
        print("\ttitre ressource : " + raw[1])
        print("\tdate apparition : " + raw[2])
        print("\tgenre : " + raw[3])
        print("\tlangue : " + raw[4])
        print("\tsynopsys : " + raw[5])
        print("\tréalisateur: " + raw[6] + " " + raw[7])
        print("}")

def chercherFilmByTitre(titre):
    sql = """
    SELECT Ressource.code, Ressource.titre, Ressource.dateApparition, Ressource.genre, Film.langue, Film.synopsis, Contributeur.nom, Contributeur.prenom 
    FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id 
    JOIN Ressource ON Contribution.code = Ressource.code JOIN Film ON Ressource.code = Film.id 
    WHERE LOWER(Ressource.titre) = ? AND Contribution.type = 'Realisateur'
    """
    cur.execute(sql, [titre.lower()])
    afficherFilms(cur.fetchall())
    
def chercherFilmByDate(date):
    sql = """
    SELECT Ressource.code, Ressource.titre, Ressource.dateApparition, Ressource.genre, Film.langue, Film.synopsis, Contributeur.nom, Contributeur.prenom 
    FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id JOIN Ressource ON Contribution.code = Ressource.code JOIN Film ON Ressource.code = Film.id 
    WHERE Ressource.dateApparition = ? AND Contribution.type = 'Realisateur'
    """
    cur.execute(sql, [date])
    afficherFilms(cur.fetchall())

def chercherFilmByRealisateur(real):
    sql = """
    SELECT Ressource.code, Ressource.titre, Ressource.dateApparition, Ressource.genre, Film.langue, Film.synopsis, Contributeur.nom, Contributeur.prenom 
    FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id JOIN Ressource ON Contribution.code = Ressource.code JOIN Film 
    ON Ressource.code = Film.id WHERE LOWER(Contributeur.nom) = ? AND Contribution.type = 'Realisateur'
    """
    cur.execute(sql, [real.lower()])
    afficherFilms(cur.fetchall())

def chercherLivreByTitre(titre):
    print("recherche du livre à implémenter")

def chercherLivreByDate(date):
    print("recherche du livre à implémenter")

def chercherLivreByAuteur(auteur):
    print("recherche du livre à implémenter")

def chercherMusiqueByTitre(titre):
    print("recherche de la musique à implémenter")

def chercherMusiqueByDate(date):
    print("recherche de la musique à implémenter")

def chercherMusiqueByAuteur(date):
    print("recherche de la musique à implémenter")


def demanderTypeRechercheFilm():
    choix = int(input("""Choix du type de recherche
        1. par titre de film
        2. par date d'apparition du film
        3. par nom du réalisateur
        Choix : """))
    verifierChoix(choix, 3)
    return choix

def demanderTypeRechercheLivre():
    choix = int(input("""Choix du type de recherche
        1. par titre du livre
        2. par date d'apparition du livre
        3. par nom de l'auteur
        Choix : """))
    verifierChoix(choix, 3)
    return choix

def demanderTypeRechercheMusique():
    choix = int(input("""Choix du type de recherche
        1. par titre de la musique
        2. par date d'apparition de la musique
        3. par nom de l'auteur
        Choix : """))
    verifierChoix(choix, 3)
    return choix

def chercherRessource():
    typeRessource = demanderTypeRessource()
    #titreRessource = ""
    #while(titreRessource == ""):
    #    titreRessource = input("titre de la ressource (not null): ")
    #dateRessource = input("date d'apparition  (AAAA-MM-JJ) : ")
    if(typeRessource == "Film"):
        typeRecherche = demanderTypeRechercheFilm()
        if(typeRecherche == 1):
            titre = input("titre du film : ")
            chercherFilmByTitre(titre)
        elif(typeRecherche == 2):
            date = input("date d'apparition (AAAA-MM-JJ) : ")
            chercherFilmByDate(date)
        else:
            realisateur = input("nom du réalisateur : ")
            chercherFilmByRealisateur(realisateur)

    elif(typeRessource == "Livre"):
        typeRecherche = demanderTypeRechercheLivre()
        if(typeRecherche == 1):
            titre = input("titre du livre : ")
            chercherLivreByTitre(titre)
        elif(typeRecherche == 2):
            date = input("date d'apparition (AAAA-MM-JJ) : ")
            chercherLivreByDate(date)
        else:
            auteur = input("nom de l'auteur : ")
            chercherLivreByAuteur(auteur)

    else:
        typeRecherche = demanderTypeRechercheMusique()
        if(typeRecherche == 1):
            titre = input("titre de la musique : ")
            chercherMusiqueByTitre(titre)
        elif(typeRecherche == 2):
            date = input("date d'apparition (AAAA-MM-JJ) : ")
            chercherMusiqueByDate(date)
        else:
            auteur = input("nom de l'auteur : ")
            chercherMusiqueByAuteur(auteur)
    

def menuAdherent():
    choix = int(input("""Menu Adhérent:
    1. Chercher une ressource
    2. Emprunter une ressource
    3. Rendre une ressource
    4. Voir mes ressources en cours d'emprunt
    5. Voir mes sanctions
    6. Quitter\nChoix : """))

    verifierChoix(choix, 6)

    if(choix == 1):
        chercherRessource()
        print("")
        menuAdherent()
    elif(choix == 2):
        emprunterRessource()
        print()
        menuAdherent()
    elif(choix == 3):
        rendreRessource()
        print()
        menuAdherent()
    elif(choix == 4):
        empruntsEnCours()
        print()
        menuAdherent()
    elif(choix == 5):
        afficherSanctions()
    



def connexion_compte():
    login = input("Connexion\nlogin : ") 
    pwd = input("mot de passe: ")
    if(estAdherent(login, pwd)):
        isAdherent = True
        menuAdherent()
    elif(estPersonnel(login, pwd)):
        #menu_personnel()
        print("Personnel")
    else:
        print("Aucun utilisateur ne correspond dans la base de donnée !\nVeuillez réessayer (Ctrl+C pour quitter)\n")
        connexion_compte()


chercherRessource()