#changer le module
import sqlite3

#connexion a la BD
conn = sqlite3.connect("../database.db")
cur = conn.cursor()

isAdherent = False


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
    if(raws):
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
    else: 
        print("Aucun résultat !")

def chercherFilmByTitre(titre):
    sql = """
    SELECT R.code, R.titre, R.dateApparition, R.genre, F.langue, F.synopsis, Contributeur.nom, Contributeur.prenom 
    FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id JOIN Ressource R ON Contribution.code = R.code 
    JOIN Film F ON R.code = F.id WHERE LOWER(R.titre) = ? AND Contribution.type = 'Realisateur'
    """
    cur.execute(sql, [titre.lower()])
    afficherFilms(cur.fetchall())
    
def chercherFilmByDate(date):
    sql = """
    SELECT R.code, R.titre, R.dateApparition, R.genre, F.langue, F.synopsis, Contributeur.nom, Contributeur.prenom 
    FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id JOIN Ressource R ON Contribution.code = R.code 
    JOIN Film F ON R.code = F.id WHERE R.dateApparition = ? AND Contribution.type = 'Realisateur'
    """
    cur.execute(sql, [date])
    afficherFilms(cur.fetchall())

def chercherFilmByRealisateur(real):
    sql = """
    SELECT R.code, R.titre, R.dateApparition, R.genre, F.langue, F.synopsis, Contributeur.nom, Contributeur.prenom 
    FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id JOIN Ressource R ON Contribution.code = R.code 
    JOIN Film F ON R.code = F.id WHERE LOWER(Contributeur.nom) = ? AND Contribution.type = 'Realisateur'
    """
    cur.execute(sql, [real.lower()])
    afficherFilms(cur.fetchall())

def afficherLivres(raws):
    if(raws):
        for raw in raws:
            print("{")
            print("\tcode ressource : %d" % raw[0])
            print("\ttitre ressource : " + raw[1])
            print("\tdate apparition : " + raw[2])
            print("\téditeur : " + raw[3])
            print("\tgenre : " + raw[4])
            print("\tlangue : " + raw[5])
            print("\trésumé : " + raw[6])
            print("\tauteur: " + raw[7] + " " + raw[8])
            print("}")
    else: 
        print("Aucun résultat !")

def chercherLivreByTitre(titre):
    sql = """
    SELECT R.code, R.titre, R.dateApparition, R.editeur, R.genre, L.langue, L.resume, Contributeur.nom, Contributeur.prenom 
    FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id JOIN Ressource R ON Contribution.code = R.code 
    JOIN Livre L ON R.code = L.id WHERE LOWER(R.titre) = ? AND Contribution.type = 'Auteur'
    """
    cur.execute(sql, [titre.lower()])
    afficherLivres(cur.fetchall())


def chercherLivreByDate(date):
    sql = """
    SELECT R.code, R.titre, R.dateApparition, R.editeur, R.genre, L.langue, L.resume, Contributeur.nom, Contributeur.prenom 
    FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id JOIN Ressource R ON Contribution.code = R.code 
    JOIN Livre L ON R.code = L.id WHERE R.dateApparition = ? AND Contribution.type = 'Auteur'
    """
    cur.execute(sql, [date])
    afficherLivres(cur.fetchall())

def chercherLivreByAuteur(auteur):
    sql = """
    SELECT R.code, R.titre, R.dateApparition, R.editeur, R.genre, L.langue, L.resume, Contributeur.nom, Contributeur.prenom 
    FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id JOIN Ressource R ON Contribution.code = R.code 
    JOIN Livre L ON R.code = L.id WHERE LOWER(Contributeur.nom) = ? AND Contribution.type = 'Auteur'
    """
    cur.execute(sql, [auteur.lower()])
    afficherLivres(cur.fetchall())

def afficherMusiques(raws):
    if(raws):
        for raw in raws:
            print("{")
            print("\tcode ressource : %d" % raw[0])
            print("\ttitre ressource : " + raw[1])
            print("\tdate apparition : " + raw[2])
            print("\tgenre : " + raw[3])
            print("\tlongueur (en secondes) : %d" % raw[4])
            print("\tauteur : " + raw[5] + " " + raw[6] + " (" + raw[7] + ")")
            print("}")
    else:
        print("Aucun résultat !")
    

def chercherMusiqueByTitre(titre):
    sql = """
    SELECT R.code, R.titre, R.dateApparition, R.genre, EM.longueur, Contributeur.nom, Contributeur.prenom, Contribution.type 
    FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id JOIN Ressource R ON Contribution.code = R.code 
    JOIN EnregistrementMusical EM ON R.code = EM.id 
    WHERE LOWER(R.titre) = ? AND (Contribution.type = 'Compositeur' OR Contribution.type = 'Interprete')
    """
    cur.execute(sql, [titre.lower()])
    afficherMusiques(cur.fetchall())

def chercherMusiqueByDate(date):
    sql = """
    SELECT R.code, R.titre, R.dateApparition, R.genre, EM.longueur, Contributeur.nom, Contributeur.prenom, Contribution.type
    FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id JOIN Ressource R ON Contribution.code = R.code 
    JOIN EnregistrementMusical EM ON R.code = EM.id 
    WHERE R.dateApparition = ? AND (Contribution.type = 'Compositeur' OR Contribution.type = 'Interprete')
    """
    cur.execute(sql, [date])
    afficherMusiques(cur.fetchall())

def chercherMusiqueByAuteur(auteur):
    sql = """
    SELECT R.code, R.titre, R.dateApparition, R.genre, EM.longueur, Contributeur.nom, Contributeur.prenom, Contribution.type
    FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id JOIN Ressource R ON Contribution.code = R.code 
    JOIN EnregistrementMusical EM ON R.code = EM.id 
    WHERE LOWER(Contributeur.nom) = ? AND (Contribution.type = 'Compositeur' OR Contribution.type = 'Interprete')
    """
    cur.execute(sql, [auteur.lower()])
    afficherMusiques(cur.fetchall())


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
        3. par nom de famille l'auteur
        Choix : """))
    verifierChoix(choix, 3)
    return choix

def demanderTypeRechercheMusique():
    choix = int(input("""Choix du type de recherche
        1. par titre de la musique
        2. par date d'apparition de la musique
        3. par nom de famille du compositeur ou de l'interprète
        Choix : """))
    verifierChoix(choix, 3)
    return choix

def chercherRessource():
    typeRessource = demanderTypeRessource()
    if(typeRessource == "Film"):
        typeRecherche = demanderTypeRechercheFilm()
        if(typeRecherche == 1):
            titre = input("titre du film : ")
            chercherFilmByTitre(titre)
        elif(typeRecherche == 2):
            date = input("date d'apparition (AAAA-MM-JJ) : ")
            chercherFilmByDate(date)
        else:
            realisateur = input("nom de fammille du réalisateur : ")
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
            auteur = input("nom de famille l'auteur : ")
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
            auteur = input("nom de fammille de l'auteur : ")
            chercherMusiqueByAuteur(auteur)
    

def emprunterRessource():
    print("a implémenter")

def rendreRessource():
    print("a implémenter")

    


def afficherEmpruntsEnCours(login):
    # attention, modifs a faire pour une bd différente de sqlite
    sql = """SELECT R.code, R.titre, R.dateApparition, Contributeur.nom, Contributeur.prenom, Contribution.type, P.date_emprunt, P.duree
    FROM Contributeur 
    JOIN Contribution ON Contributeur.id = Contribution.id 
    JOIN Ressource R ON Contribution.code = R.code 
    JOIN Exemplaire E ON E.code = R.code
    JOIN Pret P ON P.exemplaire = E.id
    WHERE date(P.date_emprunt, P.duree || ' days') > strftime('%Y-%m-%d','now') AND P.adherent = ? 
    AND Contribution.type <> 'Acteur' """ 
    # remplacer les fonctions pour le calcul de la date
    # cf https://librecours.net/module/bdd0/fonctions/pres/co/date.html?mode=html et fonciton now() 

    cur.execute(sql, [login])
    raws = cur.fetchall()
    if(raws):
        for raw in raws:
            print("{")
            print("\tcode ressource : %d" % raw[0])
            print("\ttitre ressource : " + raw[1])
            print("\tdate apparition : " + raw[2])
            print("\tcontributeur : " + raw[3] + " " + raw[4] + " (" + raw[5] + ")")
            print("\tdate emprunt : " + raw[6])
            print("\tdurée de l'emprunt : %d" % raw[7])
            print("}")
    else:
        print("Aucun emprunt en cours !")

def afficherDegradations(login):
    sql = "SELECT * FROM Degradation WHERE adherent = ?"
    cur.execute(sql, [login])
    raws = cur.fetchall()
    if(raws):    
        print("Dégradations (%d):" % len(raws))
        for raw in raws:
            if(raw[1]):
                remboursementFait = "oui"
            else: 
                remboursementFait = "non"
            print("\t- remboursement effectué ? " + remboursementFait)
    else:
        print("Aucune dégradation pour l'utilisateur " + login)
        

def afficherRetards(login):
    sql = "SELECT * FROM Retard WHERE adherent = ?"
    cur.execute(sql, [login])
    raws = cur.fetchall()
    if(raws):    
        print("Retards (%d):" % len(raws))
        for raw in raws:
            print("\t{")
            print("\t\t- Date début suspension : " + raw[1])
            print("\t\t- Nombre de jours de retard : %d" % raw[2])
            print("\t}")
    else:
        print("Aucun retard pour l'utilisateur " + login)


def afficherSanctions(login):
    afficherDegradations(login)
    afficherRetards(login)



def menuAdherent(login):
    choix = int(input("""Menu Adhérent:
    1. Chercher une ressource
    2. Emprunter une ressource
    3. Rendre une ressource
    4. Voir mes ressources en cours d'emprunt
    5. Voir mes sanctions
    6. Quitter
    Choix : """))

    verifierChoix(choix, 6)

    if(choix == 1):
        chercherRessource()
        print("")
        menuAdherent(login)
    elif(choix == 2):
        emprunterRessource()    # vérifier qu'il reste des exemplaires disponibles pour pouvoir emprunter la ressource
        print()
        menuAdherent(login)
    elif(choix == 3):
        rendreRessource()   # détruire la ligne de pret de l'exemplaire emprunté, vérifier l'état et la date de rendu pour voir si il faut ajouter des sanctions
        print()
        menuAdherent(login)
    elif(choix == 4):
        afficherEmpruntsEnCours(login)   
        print()
        menuAdherent(login)
    elif(choix == 5):
        afficherSanctions(login)
        print()
        menuAdherent(login)
    



def connexion_compte():
    login = input("Connexion\nlogin : ") 
    pwd = input("mot de passe: ")
    if(estAdherent(login, pwd)):
        isAdherent = True
        menuAdherent(login)
    elif(estPersonnel(login, pwd)):
        print("menu du personnel à implémenter")
    else:
        print("Aucun utilisateur ne correspond dans la base de donnée !\nVeuillez réessayer (Ctrl+C pour quitter)\n")
        connexion_compte()


connexion_compte()