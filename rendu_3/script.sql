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


-- CREATE
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
    PRIMARY KEY(exemplaire,adherent,date_emprunt),
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
    ISBN BIGINT NOT NULL,
    resume VARCHAR,
    langue VARCHAR NOT NULL,
    FOREIGN KEY (id) REFERENCES Ressource(code)
);

-- INSERTS

-- Adherents
INSERT INTO Adherent VALUES('tgarcher','banane','Garcher','Theodore','tgarcher@utc.fr','8 rue pouet','1990-01-01','0655555555',true,0);
INSERT INTO Adherent VALUES('jdoe','poire','Doe','John', 'jdoe@utc.fr','23 avenue truc','1999-02-02','0644444444',true,0);

-- Personnels
INSERT INTO Personnel VALUES('edewulf', 'carotte','Dewulf','Eliot','admin@biblio.fr','1 rue machin');

-- Ressources/Contributeurs/Contributions
INSERT INTO Ressource VALUES(1,'Le petit prince', '1943-04-06', 'Gallimard', 'Fable', 'R1');
INSERT INTO Contributeur VALUES(1, 'de Saint Exupery', 'Antoine', '1900-06-29', 'fr');
INSERT INTO Contribution VALUES(1, 1, 'Auteur');
INSERT INTO Ressource VALUES(2,'Le seigneur des anneaux', '1954-07-29', 'Hachette', 'Fantastique', 'R2');
INSERT INTO Contributeur VALUES(2, 'Tolkien', 'John Ronald Reuel', '1892-01-03', 'gb');
INSERT INTO Contribution VALUES(2, 2, 'Auteur');
INSERT INTO Ressource VALUES(3,'50 Nuances de Grey', '2011-05-03', 'Hachette', 'Erotique', 'R3');
INSERT INTO Contributeur VALUES(3, 'James', 'E.L.', '1963-06-01', 'us');
INSERT INTO Contribution VALUES(3, 3, 'Auteur');
INSERT INTO Ressource VALUES(4,'Hunger Games', '2008-09-14', 'Hachette', 'Science-fiction', 'R4');
INSERT INTO Contributeur VALUES(4, 'Collins', 'Suzanne', '1962-08-11', 'us');
INSERT INTO Contribution VALUES(4, 4, 'Auteur');
INSERT INTO Ressource VALUES(5,'Titanic', '1997-11-18', '20th Century Fox', 'Drame', 'R5');
INSERT INTO Contributeur VALUES(5, 'Cameron', 'James Francis', '1954-08-16', 'us');
INSERT INTO Contribution VALUES(5, 5, 'Realisateur');
INSERT INTO Contributeur VALUES(6, 'Lawrence', 'Jennifer', '1990-08-15', 'us');
INSERT INTO Contribution VALUES(6, 5, 'Acteur');
INSERT INTO Ressource VALUES(6,'La guerre des mondes', '2005-06-02', '20th Century Fox', 'Science-fiction', 'R6');
INSERT INTO Contributeur VALUES(7, 'Scott', 'Ridley', '1937-11-30', 'gb');
INSERT INTO Contribution VALUES(7, 6, 'Realisateur');
INSERT INTO Contributeur VALUES(8, 'Cruise', 'Tom', '1962-07-03', 'us');
INSERT INTO Contribution VALUES(8, 6, 'Acteur');
INSERT INTO Ressource VALUES(7,'Shining', '1980-05-23', '20th Century Fox', 'Horreur', 'R7');
INSERT INTO Contributeur VALUES(9, 'Kubrick', 'Stanley', '1928-07-26', 'us');
INSERT INTO Contribution VALUES(9, 7, 'Realisateur');
INSERT INTO Contributeur VALUES(10, 'Jack Nicholson', 'Jack', '1937-04-22', 'us');
INSERT INTO Contribution VALUES(10, 7, 'Acteur');
INSERT INTO Ressource VALUES(8,'Le labyrinthe', '2014-09-10', '20th Century Fox', 'Science-fiction', 'R8');
INSERT INTO Contributeur VALUES(11, 'Ball', 'Wes', '1973-09-24', 'us');
INSERT INTO Contribution VALUES(11, 8, 'Realisateur');
INSERT INTO Ressource VALUES(9,'La planète des singes', '1968-06-27', '20th Century Fox', 'Science-fiction', 'R9');
INSERT INTO Contributeur VALUES(12, 'Burton', 'Tim', '1958-08-25', 'us');
INSERT INTO Contribution VALUES(12, 9, 'Realisateur');
INSERT INTO Contributeur VALUES(13, 'Roddy McDowall', 'Roddy', '1928-12-17', 'us');
INSERT INTO Contribution VALUES(13, 9, 'Acteur');
INSERT INTO Ressource VALUES(10,'Paint it black - Rolling Stones', '1966-05-11', 'Capitol', 'Rock', 'R10');
INSERT INTO Contributeur VALUES(14, 'Jagger', 'Mick', '1943-07-26', 'gb');
INSERT INTO Contribution VALUES(14, 10, 'Interprete');
INSERT INTO Contributeur VALUES(15, 'Richards', 'Keith', '1943-12-18', 'gb');
INSERT INTO Contribution VALUES(15, 10, 'Interprete');
INSERT INTO Ressource VALUES(11,'The Doors - The Doors', '1967-01-04', 'Elektra', 'Rock', 'R11');
INSERT INTO Contributeur VALUES(16, 'Krieger', 'Robby', '1946-05-08', 'us');
INSERT INTO Contribution VALUES(16, 11, 'Interprete');
INSERT INTO Ressource VALUES(12,'The Beatles - Sgt. Pepper', '1967-06-01', 'Capitol', 'Rock', 'R12');
INSERT INTO Contributeur VALUES(17, 'Lennon', 'John', '1940-10-09', 'gb');
INSERT INTO Contribution VALUES(17, 12, 'Interprete');
INSERT INTO Contributeur VALUES(18, 'McCartney', 'Paul', '1942-06-18', 'gb');
INSERT INTO Contribution VALUES(18, 12, 'Interprete');
INSERT INTO Ressource VALUES(13,'Beethoven - Symphonie n°5', '1808-12-22', 'Capitol', 'Classique', 'R13');
INSERT INTO Contributeur VALUES(19, 'Beethoven', 'Ludwig van', '1770-12-16', 'de');
INSERT INTO Contribution VALUES(19, 13, 'Compositeur');
INSERT INTO Ressource VALUES(14,'Mozart - Requiem', '1791-05-05', 'Capitol', 'Classique', 'R14');
INSERT INTO Contributeur VALUES(20, 'Mozart', 'Wolfgang Amadeus', '1756-01-27', 'at');
INSERT INTO Contribution VALUES(20, 14, 'Compositeur');

-- Livres
INSERT INTO Livre VALUES(1, 9782070413095, 'Un petit garçon part à la recherche dun astéroïde qui a atterri sur la terre', 'fr');
INSERT INTO Livre VALUES(2, 9782070413095, 'Frodon tente de détruire lanneau de pouvoir dans une épopée incroyable.', 'en');
INSERT INTO Livre VALUES(3, 9782070413095, 'Une jeune femme découvre le sadomasochisme avec un milliardaire.', 'fr');
INSERT INTO Livre VALUES(4, 9782070413095, 'Une jeune fille doit survivre dans un monde post-apocalyptique.', 'en');

-- Films
INSERT INTO Film VALUES(5,194,'en','Un jeune homme et une jeune femme tombent amoureux à bord du Titanic, un paquebot qui fait route vers les Etats-Unis. Mais le destin en décidera autrement...');
INSERT INTO Film VALUES(6,116,'en','Un vaisseau spatial est envoyé sur Mars pour y découvrir si la planète est habitable. Mais les Martiens ne sont pas très accueillants...');
INSERT INTO Film VALUES(7,146,'en','Jack Torrance, un écrivain alcoolique, accepte un poste de gardien de nuit dans un hôtel isolé. Il y retrouve son épouse et son fils, qui sont tous les trois hantés par des fantômes...');
INSERT INTO Film VALUES(8,113,'en','Thomas, un jeune garçon, se retrouve piégé dans un labyrinthe. Il doit trouver une sortie avant que...');
INSERT INTO Film VALUES(9,120,'en','Les singes prennent le pouvoir!!!');

-- EnregistrementsMusicaux
INSERT INTO EnregistrementMusical VALUES(10, 180);
INSERT INTO EnregistrementMusical VALUES(11, 190);
INSERT INTO EnregistrementMusical VALUES(12, 200);
INSERT INTO EnregistrementMusical VALUES(13, 210);
INSERT INTO EnregistrementMusical VALUES(14, 220);

-- Exemplaires
INSERT INTO Exemplaire VALUES(1,1,'Neuf');
INSERT INTO Exemplaire VALUES(2,1,'Bon');
INSERT INTO Exemplaire VALUES(3,2,'Bon');
INSERT INTO Exemplaire VALUES(4,2,'Neuf');
INSERT INTO Exemplaire VALUES(5,3,'Neuf');
INSERT INTO Exemplaire VALUES(6,3,'Neuf');
INSERT INTO Exemplaire VALUES(7,3,'Bon');
INSERT INTO Exemplaire VALUES(8,4,'Bon');
INSERT INTO Exemplaire VALUES(9,5,'Bon');
INSERT INTO Exemplaire VALUES(10,5,'Neuf');
INSERT INTO Exemplaire VALUES(11,6,'Neuf');
INSERT INTO Exemplaire VALUES(12,6,'Bon');
INSERT INTO Exemplaire VALUES(13,7,'Neuf');
INSERT INTO Exemplaire VALUES(14,8,'Bon');
INSERT INTO Exemplaire VALUES(15,9,'Neuf');
INSERT INTO Exemplaire VALUES(16,9,'Neuf');
INSERT INTO Exemplaire VALUES(17,10,'Bon');
INSERT INTO Exemplaire VALUES(18,11,'Bon');
INSERT INTO Exemplaire VALUES(19,11,'Neuf');
INSERT INTO Exemplaire VALUES(20,11,'Bon');
INSERT INTO Exemplaire VALUES(21,12,'Bon');
INSERT INTO Exemplaire VALUES(22,13,'Neuf');
INSERT INTO Exemplaire VALUES(23,14,'Neuf');
INSERT INTO Exemplaire VALUES(24,14,'Bon');

-- Prets
INSERT INTO Pret VALUES(1,'tgarcher','2016-01-01',7);
INSERT INTO Pret VALUES(2,'tgarcher','2016-03-21',7);
INSERT INTO Pret VALUES(3,'tgarcher','2016-04-17',7);
INSERT INTO Pret VALUES(4,'tgarcher','2016-05-01',7);
INSERT INTO Pret VALUES(5,'tgarcher','2016-05-15',7);
INSERT INTO Pret VALUES(6,'tgarcher','2016-05-29',7);
INSERT INTO Pret VALUES(7,'tgarcher','2016-06-12',7);
INSERT INTO Pret VALUES(8,'tgarcher','2016-06-26',7);
INSERT INTO Pret VALUES(9,'tgarcher','2016-07-10',7);
INSERT INTO Pret VALUES(10,'jdoe','2016-07-24',7);
INSERT INTO Pret VALUES(11,'jdoe','2016-08-07',7);
INSERT INTO Pret VALUES(12,'jdoe','2016-08-21',7);
INSERT INTO Pret VALUES(13,'jdoe','2016-09-04',7);
INSERT INTO Pret VALUES(14,'jdoe','2016-09-18',7);
INSERT INTO Pret VALUES(15,'jdoe','2016-10-02',7);
INSERT INTO Pret VALUES(16,'jdoe','2016-10-16',7);
INSERT INTO Pret VALUES(17,'jdoe','2016-10-30',7);
INSERT INTO Pret VALUES(18,'jdoe','2016-11-13',7);

-- Retards/Degradations
INSERT INTO Retard VALUES(1, '2022-02-22', 7, 'tgarcher');
INSERT INTO Degradation VALUES(1, false, 'tgarcher');