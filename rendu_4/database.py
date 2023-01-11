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
    
def emprunterLivre(login, titre):
    # on part du principe qu'il n'y a pas deux livres avec le même titre
    sql = """SELECT e.id FROM exemplaire e NATURAL JOIN RESSOURCE r JOIN Contribution c ON r.code = c.code JOIN Pret p ON e.id = p.exemplaire
    WHERE c.type = 'Auteur' AND e.etat != 'Perdu' AND LOWER(r.titre) = ? AND p.date_retour IS NOT NULL"""
    cur.execute(sql, [titre.lower()])
    raw = cur.fetchone()
    if(len(raw) == 0):
        print("Erreur : aucun exemplaire n'est disponible pour le livre intitulé " + titre)
    else:
        exemplaire = raw[0]
        sql = "INSERT INTO Pret VALUES(?, ?, date('now'), 7, NULL)"
        cur.execute(sql, (exemplaire, login))
        conn.commit()
        print("Emprunt enregistré, veuillez le rendre dans 7 jours")

def emprunterFilm(login, titre):
    # on part du principe qu'il n'y a pas deux films avec le même titre
    sql = """SELECT e.id FROM exemplaire e NATURAL JOIN RESSOURCE r JOIN Contribution c ON r.code = c.code JOIN Pret p ON e.id = p.exemplaire
    WHERE c.type = 'Realisateur' AND e.etat != 'Perdu' AND LOWER(r.titre) = ? AND p.date_retour IS NOT NULL"""
    cur.execute(sql, [titre.lower()])
    raw = cur.fetchone()
    if(len(raw) == 0):
        print("Erreur : aucun exemplaire n'est disponible pour le film intitulé " + titre)
    else:
        exemplaire = raw[0]
        sql = "INSERT INTO Pret VALUES(?, ?, date('now'), 7, NULL)"
        cur.execute(sql, (exemplaire, login))
        conn.commit()
        print("Emprunt enregistré, veuillez le rendre dans 7 jours")

def emprunterMusique(login, titre):
    # on part du principe qu'il n'y a pas deux musiques avec le même titre
    sql = """SELECT e.id FROM exemplaire e NATURAL JOIN RESSOURCE r JOIN Contribution c ON r.code = c.code JOIN Pret p ON e.id = p.exemplaire
    WHERE (c.type = 'Interprete' OR c.type='Compositeur') AND e.etat != 'Perdu' AND LOWER(r.titre) = ? AND p.date_retour IS NOT NULL"""
    cur.execute(sql, [titre.lower()])
    raw = cur.fetchone()
    if(len(raw) == 0):
        print("Erreur : aucun exemplaire n'est disponible pour la musiquee intitulé " + titre)
    else:
        exemplaire = raw[0]
        sql = "INSERT INTO Pret VALUES(?, ?, date('now'), 7, NULL)"
        cur.execute(sql, (exemplaire, login))
        conn.commit()
        print("Emprunt enregistré, veuillez le rendre dans 7 jours")

def emprunterRessource(login):
    if not checkCompteActif(login):
        print("Impossible d'emprunter : votre compte n'est pas actif")
        return
    typeEmprunt = input("Veuillez saisir le type de ressource que vous souhaitez emprunter ('L':Livre, 'F':Film, 'M':Musique) : ")
    titre = input("Veuillez saisir le nom de la ressource que vous souhaitez emprunter: ")
    if(typeEmprunt == 'L'):
        emprunterLivre(login, titre)
    elif(typeEmprunt == 'F'):
        emprunterFilm(login, titre)
    elif(typeEmprunt == 'M'):
        emprunterMusique(login, titre)
    else:
        emprunterRessource(login)

def checkCompteActif(login):
    requete = "Select 1 from Adherent where login = ? and carte_active = true"
    cur.execute(requete, [login])
    return cur.fetchone()

def creerDegradation(login):
    # on cherche le premier id disponible pour une nouvelle dégradation
    sql = "SELECT count(*) from degradation"
    cur.execute(sql)
    raw = cur.fetchone()
    firstIdAvailable = raw[0] + 1

    # on ajoute la dégradation
    sql = "INSERT INTO Degradation VALUES(?, false, ?)"
    cur.execute(sql, (firstIdAvailable, login))
    conn.commit()
    print("Une sanction de type \"dégradation\" ajoutée pour l'utilisateur " + login)

def rendreRessource(login):
    print("Retour d'une ressource.\nEn cas d'oubli des infos concernant la ressource, retourner au menu et selectionner l'option \"Voir mes ressources en cours d'emprunt\"")
    titre = input("Veuillez saisir le nom de la ressource que vous souhaitez rendre : ")
    nouvelEtat = input("Veuillez saisir l'état de la ressource rendue ('N':neuf, 'B':bon, 'A':abimé, 'P':perdu) : ")
    dateEmprunt = input("Veuillez saisir la date de l'emprunt (AAA-MM-JJ) : ")
    
    #on récupère l'id et l'ancien etat de l'examplaire
    sql = """SELECT e.id, e.etat FROM Pret p JOIN exemplaire e ON e.id = p.exemplaire 
    NATURAL JOIN Ressource r WHERE p.date_emprunt = ? AND p.adherent = ? AND LOWER(r.titre) = ?"""
    cur.execute(sql, (dateEmprunt, login, titre.lower()))
    raws = cur.fetchall()
    if(len(raws) != 1): 
        print("Erreur, il ne devrait y avoir qu'un seul resultat a la requete !")
        exit(1)
    exemplaire = raws[0][0]
    ancienEtat = raws[0][1]
    if((ancienEtat=="Neuf" or ancienEtat=="Bon") and (nouvelEtat=="A")):
        creerDegradation(login)
    if(nouvelEtat=="P"):
        creerDegradation(login)
            
    #On met a jour l'état de l'exemplaire
    sql = "UPDATE Exemplaire SET etat = ? WHERE id = ?"
    if(nouvelEtat == 'A'):
        cur.execute(sql, ("Abime", exemplaire))
    if(nouvelEtat == 'N'):
        cur.execute(sql, ("Neuf", exemplaire))
    if(nouvelEtat == 'P'):
        cur.execute(sql, ("Perdu", exemplaire))
    if(nouvelEtat == 'B'):
        cur.execute(sql, ("Bon", exemplaire))
    conn.commit()

    #on met a jour la date retour du pret
    sql = "UPDATE Pret SET date_retour = date('now') WHERE date_emprunt = ? AND adherent = ? AND exemplaire = ?"
    cur.execute(sql, (dateEmprunt, login, exemplaire))
    conn.commit()
    print("Retour de la ressource effectué avec succès")

    


def afficherEmpruntsEnCours(login):
    # attention, modifs a faire pour une bd différente de sqlite
    sql = """SELECT R.code, R.titre, R.dateApparition, Contributeur.nom, Contributeur.prenom, Contribution.type, P.date_emprunt, P.duree
    FROM Contributeur 
    JOIN Contribution ON Contributeur.id = Contribution.id 
    JOIN Ressource R ON Contribution.code = R.code 
    JOIN Exemplaire E ON E.code = R.code
    JOIN Pret P ON P.exemplaire = E.id
    WHERE date_retour IS NULL AND P.adherent = ? 
    AND Contribution.type <> 'Acteur' """ 
    # date(P.date_emprunt, P.duree || ' days') > strftime('%Y-%m-%d','now')
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
    sql = "SELECT count(*) FROM Degradation WHERE adherent = ? AND remboursementFait = false"
    cur.execute(sql, [login])
    result = cur.fetchone()
    print("Dégradations non remboursées : %d" % result[0])

    sql = "SELECT count(*) FROM Degradation WHERE adherent = ? AND remboursementFait = true"
    cur.execute(sql, [login])
    result = cur.fetchall()
    print("Dégradations remboursées : %d" % result[0])
        

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

def desactiverCompte(login):
    sql = "UPDATE Adherent SET carte_active = false WHERE login = ?"
    cur.execute(sql, [login])
    conn.commit()

def activerCompte(login):
    sql = "UPDATE Adherent SET carte_active = true WHERE login = ?"
    cur.execute(sql, [login])
    conn.commit()

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
        emprunterRessource(login)    # vérifier qu'il reste des exemplaires disponibles pour pouvoir emprunter la ressource
        print()
        menuAdherent(login)
    elif(choix == 3):
        rendreRessource(login)
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
    
def menuPersonnel(login):
    choix = int(input("""Menu Personnel:
    1. Voir emprunts en cours d'un utilisateur
    2. Voir sanctions d'un utilisateur
    3. Désactiver un compte utilisateur
    4. Activer un compte utilisateur
    5. Quitter
    Choix : """))

    verifierChoix(choix, 5)

    if(choix == 1):
        afficherEmpruntsEnCours(input("Login de l'utilisateur : "))
        print("")
        menuPersonnel(login)
    elif(choix == 2):
        afficherSanctions(input("Login de l'utilisateur : "))    # vérifier qu'il reste des exemplaires disponibles pour pouvoir emprunter la ressource
        print()
        menuPersonnel(login)
    elif(choix == 3):
        desactiverCompte(input("Login de l'utilisateur : "))
        print()
        menuPersonnel(login)
    elif(choix == 4):
        activerCompte(input("Login de l'utilisateur : "))
        print()
        menuPersonnel(login)


def connexion_compte():
    login = input("Connexion\nlogin : ") 
    pwd = input("mot de passe: ")
    if(estAdherent(login, pwd)):
        isAdherent = True
        menuAdherent(login)
    elif(estPersonnel(login, pwd)):
        menuPersonnel(login)
    else:
        print("Aucun utilisateur ne correspond dans la base de donnée !\nVeuillez réessayer (Ctrl+C pour quitter)\n")
        connexion_compte()


connexion_compte()
