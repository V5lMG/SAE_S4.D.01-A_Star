from case import Case
from plateau import Plateau

class Importateur:
    def __init__(self, fichier):
        self.fichier = fichier

    def importer_plateau(self):
        """Lit un fichier et importe le plateau sous forme d'un objet Plateau avec ses cases."""
        try:
            with open(self.fichier, "r") as fichier:
                lignes = [ligne.strip().replace(" ", "") for ligne in fichier]
        except FileNotFoundError:
            print(f"Erreur : fichier '{self.fichier}' introuvable.")
            return None

        if not lignes:
            print("Erreur : le fichier est vide.")
            return None

        largeur = len(lignes)
        longueur = len(lignes[0])

        # Vérification que le plateau est bien rectangulaire
        if any(len(ligne) != longueur for ligne in lignes):
            print("Erreur : le plateau n'est pas rectangulaire.")
            return None

        # Création de l'objet Plateau
        plateau = Plateau(largeur, longueur, 0, False)
        cases = []

        depart = None
        arrivee = None

        # Construction du plateau avec les objets Case
        for x, ligne in enumerate(lignes):
            row = []
            for y, char in enumerate(ligne):
                case_obj = Case(x, y, char)
                row.append(case_obj)

                if char == 'D':
                    if depart:
                        print("Erreur : plusieurs points de départ détectés.")
                        return None
                    depart = case_obj

                elif char == 'A':
                    if arrivee:
                        print("Erreur : plusieurs points d'arrivée détectés.")
                        return None
                    arrivee = case_obj

            cases.append(row)

        # Vérification de la présence unique de D et A
        if not depart:
            print("Erreur : aucun point de départ ('D') trouvé.")
            return None
        if not arrivee:
            print("Erreur : aucun point d'arrivée ('A') trouvé.")
            return None

        # Mise à jour du plateau avec les cases importées
        plateau.cases = cases
        plateau.depart = depart
        plateau.arrivee = arrivee

        print("Le plateau a été importé avec succès !")
        return plateau


if __name__ == "__main__":
    chemin_fichier = "test_import.txt"  # Remplace avec le chemin réel du fichier
    importateur = Importateur(chemin_fichier)

    plateau = importateur.importer_plateau()
    if plateau:
        print("Plateau importé :")
        plateau.afficher_plateau()
