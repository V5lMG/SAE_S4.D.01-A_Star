import parcours
import importation
import exportation
from parcours import Dijkstra
#import comparaison
from plateau import Plateau


class Application:
    def __init__(self):
        """Initialise l'application."""
        self.plateau = None  # Stocke le plateau généré ou importé

    def afficher_menu(self):
        """Affiche le menu principal et gère les choix de l'utilisateur."""
        choix = ""
        while choix != "Q":
            print("""
                Bienvenue sur notre application d'analyse de l'algorithme Dijkstra et A* !
                Veuillez saisir la lettre correspondante à l'action que vous voulez réaliser :
                    G - Génération d'un plateau de jeu
                    C - Comparaison d'algorithmes
                    I - Importation d'un plateau de jeu existant (.txt)
                    Q - Quitter l'application\n
            """)
            choix = input().strip().upper()

            if choix == "G":
                self.generer_plateau()
            #elif choix == "C":
                #self.comparer_algorithmes()
            elif choix == "I":
                self.importer_plateau()
            elif choix != "Q":
                print("❌ Choix invalide. Veuillez entrer G, C, I ou Q.")

    def generer_plateau(self):
        """Génère un plateau de jeu selon les paramètres de l'utilisateur."""
        largeur = self.saisir_valeur("la largeur du plateau (>= 3)", min_val=3)
        longueur = self.saisir_valeur("la longueur du plateau (>= 3)", min_val=3)
        taux = self.saisir_valeur("le taux de cases interdites (0-100)", min_val=0, max_val=100) / 100
        placement_aleatoire = self.saisir_oui_non("Placer départ/arrivée aléatoirement ? (O/N)")

        # Génération du plateau avec la classe Plateau
        self.plateau = Plateau(largeur, longueur, taux, placement_aleatoire)

        # Affichage du plateau généré
        print("\nPlateau généré :")
        self.plateau.afficher_plateau()

        # Exécution de l'algorithme de Dijkstra
        dijkstra = parcours.Dijkstra(self.plateau)

        # Affichage du plateau avec le chemin
        plateau_avec_chemin = dijkstra.afficher_resultat()

        # Exportation du plateau
        nom_fichier = input("Entrez un nom de fichier pour exporter le plateau : ").strip()
        exportateur = exportation.Exportateur(self.plateau, plateau_avec_chemin, nom_fichier)
        exportateur.exporter_vers_txt()

    # def comparer_algorithmes(self):
        #    """Compare les performances des algorithmes Dijkstra et A*."""
        #      print("Le lancement de la comparaison est en cours ...")
        #     comparateur = comparaison.Comparateur([])
    #     comparateur.comparaison("C")


    def importer_plateau(self):
        """Importe un plateau à partir d'un fichier texte."""
        chemin_fichier = input("\t\t\t\tEntrez le chemin du fichier .txt : ").strip()
        while not chemin_fichier.endswith(".txt"):
            print("❌ Erreur : le fichier doit être au format .txt.")
            chemin_fichier = input("Entrez un chemin valide : ").strip()

        importateur = importation.Importateur(chemin_fichier)
        self.plateau = importateur.importer_plateau()

        if self.plateau:
            print("📌 Plateau importé avec succès !")
            self.plateau.afficher_plateau()

    def saisir_valeur(self, message, min_val=None, max_val=None):
        """Demande à l'utilisateur une valeur numérique valide."""
        while True:
            try:
                valeur = int(input(f"Veuillez entrer {message} : ").strip())
                if (min_val is not None and valeur < min_val) or (max_val is not None and valeur > max_val):
                    raise ValueError
                return valeur
            except ValueError:
                print(f"❌ Erreur : La valeur doit être un entier entre {min_val} et {max_val}.")

    def saisir_oui_non(self, message):
        """Demande une réponse Oui/Non à l'utilisateur et retourne un booléen."""
        reponse = ""
        while reponse not in ["O", "N"]:
            reponse = input(f"{message} ").strip().upper()
            if reponse not in ["O", "N"]:
                print("❌ Réponse invalide. Entrez 'O' pour Oui ou 'N' pour Non.")
        return reponse == "O"


# Lancement de l'application
if __name__ == "__main__":
    app = Application()
    app.afficher_menu()
