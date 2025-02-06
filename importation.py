# 1) Importer le plateau
def importer_plateau(chemin_fichier):
    # Lire le fichier et stocker les lignes
    try:
        with open(chemin_fichier, "r") as fichier:
            plateau = [ligne.strip() for ligne in fichier]
    except FileNotFoundError:
        print("Erreur : fichier introuvable.")
        return None

    # Vérification simple : afficher un message si le fichier est vide
    if not plateau:
        print("Erreur : le fichier est vide.")
        return None

    # Vérification plateau
    if verification_plateau(plateau):
        # Affichage du plateau
        print("Le plateau a été importé avec succès :")
        for ligne in plateau:
            print(ligne)

    return plateau # Pour lecture avec algorithme de Dijkstra

# 2) Vérification du plateau
def verification_plateau(plateau):
    # Vérification que le plateau est rectangulaire
    longueur_ligne = len(plateau[0])  # Prendre la longueur de la première ligne
    for ligne in plateau:
        if len(ligne) != longueur_ligne:  # Si une ligne n'a pas la même longueur
            print("Erreur : le plateau n'est pas rectangulaire.")
            return False

    # Vérification de l'unicité de 'D' (départ) et 'A' (arrivée)
    nb_depart = sum(ligne.count('D') for ligne in plateau)
    nb_arrivee = sum(ligne.count('A') for ligne in plateau)

    if nb_depart != 1:
        print("Erreur : il doit y avoir un et un seul départ (D).")
        return False
    if nb_arrivee != 1:
        print("Erreur : il doit y avoir une et une seule arrivée (A).")
        return False

    # Vérification des cases valides (X, O, D, A)
    for ligne in plateau:
        for case in ligne:
            if case not in 'X ODA':  # Si un caractère n'est pas valide
                print(f"Erreur : caractère non valide '{case}' trouvé dans le plateau.")
                return False

    # Si toutes les vérifications passent
    return True


# Exemple d'utilisation
#chemin = "test.txt"
# plateau = importer_plateau(chemin)