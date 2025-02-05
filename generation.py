import random

def generation_plateau(largeur, longueur, taux_cases_interdite, depart_arrivee_aleatoire):
    """
    Génère un plateau de jeu avec cases interdites, une case départ et une case arrivée.
    La largeur et la longueur minimale doivent être supérieures à 3.
    Le taux de cases interdites doit être compris entre 0 et 1.

    Paramètres :
        - largeur : nombre de lignes    (minimum 3)
        - longueur : nombre de colonnes (minimum 3)
        - taux_cases_interdite : taux de cases interdites (compris entre 0 et 1)
        - depart_arrivee_aleatoire : Si False, fixe la case départ en haut à gauche et la case arrivée en bas à droite.
                                     Si True, le positionnement de la case de départ et d'arrivée seront aléatoires.
    """

    # Vérifier que les paramètres sont valides
    if longueur < 3 :
        raise ValueError("La longueur doit être supérieure ou égale à 3.")
    if largeur < 3 :
        raise ValueError("La largeur doit être supérieure ou égale à 3.")
    if taux_cases_interdite < 0 or taux_cases_interdite > 1 :
        raise ValueError("Le taux de cases interdites doit être entre 0 et 1.")

    # Génération du plateau
    plateau = [ ["O" for _ in range(longueur)] for _ in range(largeur) ]

    # Ajouter les cases interdites aléatoirement
    for x in range(largeur):
        for y in range(longueur):
            if random.random() < taux_cases_interdite:
                plateau[x][y] = "X"

    # Ajouter le départ et l'arrivée
    if not depart_arrivee_aleatoire:
        # Case départ en haut à gauche
        x_depart = 0
        y_depart = 0
        # Case arrivée en bas à droite
        x_arrivee = largeur - 1
        y_arrivee = longueur - 1
    else:
        # Placement aléatoire du départ
        x_depart = random.randint(0, largeur - 1)
        y_depart = random.randint(0, longueur - 1)

        # Générer toutes les positions possibles sauf celle du départ
        positions_possibles = []
        for x in range(largeur):
            for y in range(longueur):
                if (x, y) != (x_depart, y_depart):
                    positions_possibles.append((x, y))

        # Sélectionner une position d'arrivée aléatoire
        x_arrivee, y_arrivee = random.choice(positions_possibles)

    plateau[x_depart][y_depart] = "D"
    plateau[x_arrivee][y_arrivee] = "A"

    # Afficher ligne par ligne
    for ligne in plateau:
        print(" ".join(map(str, ligne)))


# exemple d'utilisation
# generation_plateau(4, 10, 0.2, False)
