import random


def generation_plateau(largeur, longueur, taux_cases_interdite, depart_arrivee_aleatoire):
    """
    Génère un plateau de jeu avec cases interdites, une case départ et une case arrivée.

    Paramètres :
        - largeur : nombre de colonnes
        - longueur : nombre de lignes
        - taux_cases_interdite : pourcentage (entre 0 et 1) de cases interdites
        - depart_arrivee_aleatoire : Si False, fixe la case départ en haut à gauche et la case arrivée en bas à droite.
                                     Si True, le positionnement de la case de départ et d'arrivée seront aléatoires.
    """

    # Vérifier que les paramètres sont valides
    if largeur < 3 :
        raise ValueError("La largeur doit être supérieure ou égale à 3.")
    if longueur < 3 :
        raise ValueError("La longueur doit être supérieure ou égale à 3.")
    if taux_cases_interdite < 0 or taux_cases_interdite > 1 :
        raise ValueError("Le taux de cases interdites doit être entre 0 et 1.")

    # Génération du plateau
    plateau = [ ["O" for _ in range(largeur)] for _ in range(longueur) ]

    # Ajouter le départ et l'arrivée si demandé
    if not depart_arrivee_aleatoire:
        plateau[0][0] = "D"  # Case départ en haut à gauche
        plateau[longueur - 1][largeur - 1] = "A"  # Case arrivée en bas à droite

    # Calcul du nombre de cases interdites
    total_cases = largeur * longueur
    cases_interdites = int(taux_cases_interdite * total_cases)

    # Ajouter les cases interdites aléatoirement
    for _ in range(cases_interdites):
        while True:
            x = random.randint(0, longueur - 1)
            y = random.randint(0, largeur - 1)
            # Vérifier que la case n'est ni départ ni arrivée, ni déjà interdite
            if plateau[x][y] == "O":
                plateau[x][y] = "X"
                break

    # Afficher ligne par ligne
    for ligne in plateau:
        print(" ".join(map(str, ligne)))


# exemple d'utilisation
generation_plateau(10, 10, 0.2, False)
