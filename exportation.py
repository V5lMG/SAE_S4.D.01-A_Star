def exporter_vers_txt(plateau, plateau_avec_chemin, nom_fichier):
    """
    Enregistre deux plateaux dans un fichier texte.

    :param plateau: Liste de listes représentant le plateau initial.
    :param plateau_avec_chemin: Liste de listes représentant le plateau avec chemin généré.
    :param nom_fichier: Nom du fichier de sortie (avec extension .txt).
    """
    chemin = f'{nom_fichier}.txt'

    try:
        with open(chemin, 'w', encoding='utf-8') as fichier:
            fichier.write("Plateau de jeu :\n")
            for ligne in plateau:
                fichier.write(' '.join(map(str, ligne)) + "\n")

            fichier.write("\nPlateau avec chemin :\n")
            for ligne in plateau_avec_chemin:
                fichier.write(' '.join(map(str, ligne)) + "\n")

        print(f"Le plateau a été exporté avec succès dans '{nom_fichier}'.")
        exit()

    except Exception as e:
        print(f"Erreur lors de l'export : {e}")