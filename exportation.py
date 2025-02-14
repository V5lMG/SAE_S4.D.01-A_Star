class Exportateur:
    def __init__(self, plateau, plateau_avec_chemin, nom_fichier):
        """
        Initialise l'exportateur avec le plateau et le nom du fichier.

        :param plateau: Objet Plateau représentant le plateau initial.
        :param plateau_avec_chemin: Objet Plateau représentant le plateau avec le chemin trouvé.
        :param nom_fichier: Nom du fichier de sortie (sans extension).
        """
        self.plateau = plateau
        self.plateau_avec_chemin = plateau_avec_chemin
        self.nom_fichier = f"{nom_fichier}.txt"

    def exporter_vers_txt(self):
        """Enregistre les plateaux dans un fichier texte."""
        try:
            with open(self.nom_fichier, 'w', encoding='utf-8') as fichier:
                fichier.write("Plateau de jeu :\n")
                self._ecrire_plateau(fichier, self.plateau)

                fichier.write("\nPlateau avec chemin :\n")
                self._ecrire_plateau(fichier, self.plateau_avec_chemin)

            print(f"Le plateau a été exporté avec succès dans '{self.nom_fichier}'.")
        except Exception as e:
            print(f"Erreur lors de l'export : {e}")

    def _ecrire_plateau(self, fichier, plateau):
        """Écrit un plateau dans le fichier."""
        for ligne in plateau.cases:
            fichier.write(' '.join(str(case) for case in ligne) + "\n")


# Exemple d'utilisation
if __name__ == "__main__":
    from plateau import Plateau

    # Création d'un plateau d'exemple
    plateau = Plateau(8, 8, 0.2, True)
    # Simulons un autre plateau qui sera celui avec chemin
    plateau_avec_chemin = Plateau(8, 8, 0.2, True)

    exportateur = Exportateur(plateau, plateau_avec_chemin, "plateau_exporte")
    exportateur.exporter_vers_txt()
