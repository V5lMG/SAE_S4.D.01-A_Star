from plateau import Plateau

class Exportateur:

    def __init__(self, plateau, plateau_avec_chemin, nom_fichier):
        """
        Initialise l'exportateur avec le plateau et le nom du fichier.

        :param plateau: Objet Plateau représentant le plateau initial.
        :param plateau_avec_chemin: Grille modifiée représentant le plateau avec le chemin trouvé.
        :param nom_fichier: Nom du fichier de sortie (sans extension).
        """
        self.plateau = plateau
        self.plateau_avec_chemin = self.convertir_en_plateau(plateau, plateau_avec_chemin)
        self.nom_fichier = f"{nom_fichier}.txt"

    def convertir_en_plateau(self, plateau_original, grille_affichee):
        """Convertit une grille affichée (liste de listes) en un objet Plateau."""
        nouveau_plateau = Plateau(plateau_original.largeur, plateau_original.longueur, 0, False)  # Plateau vide
        for x in range(plateau_original.largeur):
            for y in range(plateau_original.longueur):
                nouveau_plateau.cases[x][y].type_case = grille_affichee[x][y]  # Mettre à jour les types de cases
        return nouveau_plateau

    def exporter_vers_txt(self):
        """Enregistre les plateaux dans un fichier texte."""
        try:
            with open(self.nom_fichier, 'w', encoding='utf-8') as fichier:
                fichier.write("Plateau de jeu :\n")
                self.ecrire_plateau(fichier, self.plateau)

                fichier.write("\nPlateau avec chemin :\n")
                self.ecrire_plateau(fichier, self.plateau_avec_chemin)
                fichier.flush()

            print(f"\nLe plateau a été exporté avec succès dans '{self.nom_fichier}'.")

        except Exception as e:
            print(f"❌ Erreur lors de l'export : {e}")

    def ecrire_plateau(self, fichier, plateau):
        """Écrit un plateau dans le fichier."""
        for ligne in plateau.cases:
            fichier.write(' '.join(case.get_type() for case in ligne) + "\n")

if __name__ == "__main__":
    # Création d'un plateau factice
    largeur, longueur = 10, 10
    plateau_test = Plateau(largeur, longueur, 0.2, True)

    # Création d'un chemin factice
    plateau_avec_chemin_test = [[plateau_test.cases[x][y].type_case for y in range(longueur)] for x in range(largeur)]
    for i in range(min(largeur, longueur)):  # On trace un chemin diagonal pour le test
        plateau_avec_chemin_test[i][i] = '.'  # 'X' pour représenter un chemin

    # Création de l'exportateur et test d'exportation
    exportateur = Exportateur(plateau_test, plateau_avec_chemin_test, "test_export")
    exportateur.exporter_vers_txt()