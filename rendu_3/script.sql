DROP TABLE IF EXISTS Adherent CASCADE;
DROP TABLE IF EXISTS Personnel CASCADE;
DROP TABLE IF EXISTS Ressource CASCADE;
DROP TABLE IF EXISTS Exemplaire CASCADE;
DROP TABLE IF EXISTS Pret CASCADE;
DROP TABLE IF EXISTS Degradation CASCADE;
DROP TABLE IF EXISTS Retard CASCADE;
DROP TABLE IF EXISTS Contributeur CASCADE;
DROP TABLE IF EXISTS Contribution CASCADE;
DROP TABLE IF EXISTS EnregistrementMusical CASCADE;
DROP TABLE IF EXISTS Film CASCADE;
DROP TABLE IF EXISTS Livre CASCADE;

CREATE TABLE Adherent(
    login VARCHAR PRIMARY KEY,
    mdp VARCHAR NOT NULL,
    nom VARCHAR NOT NULL,
    prenom VARCHAR NOT NULL,
    mail VARCHAR NOT NULL,
    adresse VARCHAR,
    ddn DATE NOT NULL,
    num_tel VARCHAR,
    carte_active BOOLEAN NOT NULL,
    nb_emprunts INTEGER CHECK(nb_emprunts>=0)
);

CREATE TABLE Personnel(
    login VARCHAR PRIMARY KEY,
    mdp VARCHAR NOT NULL,
    nom VARCHAR NOT NULL,
    prenom VARCHAR NOT NULL,
    mail VARCHAR NOT NULL,
    adresse VARCHAR
);

CREATE TABLE Ressource(
    code INTEGER PRIMARY KEY,
    titre VARCHAR NOT NULL,
    dateApparition DATE NOT NULL,
    editeur VARCHAR,
    genre VARCHAR,
    codeClassification VARCHAR NOT NULL
);

CREATE TABLE Exemplaire(
    id INTEGER,
    code INTEGER,
    etat VARCHAR check(etat IN ('Neuf','Bon','Abime','Perdu')) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(code) REFERENCES Ressource(code)
);

CREATE TABLE Pret(
    exemplaire INTEGER,
    adherent VARCHAR,
    date_emprunt DATE,
    duree INTEGER NOT NULL,
    PRIMARY KEY(exemplaire,adherent),
    FOREIGN KEY(exemplaire) REFERENCES Exemplaire(id),
    FOREIGN KEY(adherent) REFERENCES Adherent(login)
);

CREATE TABLE Degradation(
    id INTEGER PRIMARY KEY,
    remboursementFait BOOLEAN NOT NULL,
    adherent VARCHAR,
    FOREIGN KEY (adherent) REFERENCES Adherent(login)
);

CREATE TABLE Retard(
    id INTEGER PRIMARY KEY,
    debut_suspension DATE NOT NULL,
    nb_jours_retard INTEGER NOT NULL CHECK (nb_jours_retard > 0),
    adherent VARCHAR,
    FOREIGN KEY (adherent) REFERENCES Adherent(login)
);

CREATE TABLE Contributeur(
    id INTEGER PRIMARY KEY,
    nom VARCHAR NOT NULL,
    prenom VARCHAR NOT NULL,
    ddn DATE,
    nationalite VARCHAR
);

CREATE TABLE Contribution(
    id INTEGER,
    code INTEGER,
    type VARCHAR CHECK (type IN ('Compositeur', 'Realisateur', 'Auteur', 'Interprete', 'Acteur')) NOT NULL,
    PRIMARY KEY (id, code),
    FOREIGN KEY (id) REFERENCES Contributeur(id),
    FOREIGN KEY (code) REFERENCES Ressource(code)
);

CREATE TABLE EnregistrementMusical(
    id INTEGER PRIMARY KEY,
    longueur INTEGER NOT NULL,
    FOREIGN KEY (id) REFERENCES Ressource(code)
);

CREATE TABLE Film(
    id INTEGER PRIMARY KEY,
    longueur INTEGER NOT NULL,
    langue VARCHAR NOT NULL,
    synopsis VARCHAR,
    FOREIGN KEY (id) REFERENCES Ressource(code)
);

CREATE TABLE Livre(
    id INTEGER PRIMARY KEY,
    ISBN INTEGER NOT NULL,
    resume VARCHAR,
    langue VARCHAR NOT NULL,
    FOREIGN KEY (id) REFERENCES Ressource(code)
);