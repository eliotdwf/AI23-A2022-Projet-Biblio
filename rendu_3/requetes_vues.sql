-- code et titre des ressources empruntées et date d'emprunt
SELECT r.code, r.titre, p.date_emprunt FROM Ressource r
NATURAL JOIN Exemplaire e
INNER JOIN Pret p ON p.exemplaire = e.id;


--nombre total d'emprunts 
SELECT count(*) FROM Ressource r
NATURAL JOIN Exemplaire e
INNER JOIN Pret p ON p.exemplaire = e.id;


-- vue qui permet de comptabiliser le nombre d'emprunts par ressource
CREATE VIEW v_nb_emprunts_par_ressource AS
    SELECT count(date_emprunt) AS nb_emprunts, r.code, r.titre FROM Ressource r
    NATURAL JOIN Exemplaire e
    INNER JOIN Pret p ON p.exemplaire = e.id
    GROUP BY r.code;

-- vue qui permet de comptabiliser le nombre d'emprunts par adhérent
CREATE VIEW v_nb_emprunts_par_adherent AS
SELECT count(date_emprunt) as nb_emprunts, a.nom, a.prenom FROM Adherent a
INNER JOIN Pret p ON p.adherent = a.login
GROUP BY a.nom, a.prenom;

-- ressource la + empruntée
SELECT max(nb_emprunts), code, titre
FROM v_nb_emprunts_par_ressource
GROUP BY v_nb_emprunts_par_ressource.code, v_nb_emprunts_par_ressource.titre;

-- adhérent avec le plus d'emprunts
SELECT max(nb_emprunts), nom, prenom
FROM v_nb_emprunts_par_adherent
GROUP BY v_nb_emprunts_par_adherent.nom, v_nb_emprunts_par_adherent.prenom;

-- enregistrements musicaux plus long que 200 secondes
SELECT Ressource.code, Ressource.titre, Ressource.dateApparition, EnregistrementMusical.longueur
FROM EnregistrementMusical JOIN Ressource ON Ressource.code = EnregistrementMusical.id 
WHERE EnregistrementMusical.longueur >= 200;

-- Toutes les ressources ayant un contributeur de type Réalisateur
SELECT Ressource.code, Ressource.titre, Ressource.dateApparition, Ressource.genre, Film.langue, Film.synopsis, Contributeur.nom, Contributeur.prenom 
FROM Contributeur JOIN Contribution ON Contributeur.id = Contribution.id 
                  JOIN Ressource ON Contribution.code = Ressource.code 
                  JOIN Film ON Ressource.code = Film.id 
WHERE Contribution.type = "Realisateur"

-- Dernière ressource empruntée par un adhérent
SELECT Ressource.code, Ressource.titre ,Pret.adherent, max(Pret.date_emprunt) AS "Date d'emprunt", Pret.duree
FROM Pret JOIN Exemplaire ON Pret.exemplaire = Exemplaire.id
          JOIN Ressource ON Exemplaire.code = Ressource.code
GROUP BY Pret.adherent;
