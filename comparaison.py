import matplotlib.pyplot as plt
from parcours import A_star
from plateau import Plateau
import time

class ComparaisonAStarDijkstra:

    def __init__(self, largeur, longueur, max_taux):
        self.largeur = largeur
        self.longueur = longueur
        self.taux_cases_interdites = list(range(0, max_taux))  # Plage de taux de cases interdites
        self.moy_cases_visitees_h_null   = []
        self.moy_cases_visitees_h_oiseau = []
        self.moy_cases_visitees_h_ville  = []
        self.moy_temps_h_null            = []
        self.moy_temps_h_ville           = []
        self.moy_temps_h_oiseau          = []
        self.iteration                   = 3                  # Nombre d'itérations par défaut

    def executer(self):
        """Exécute la comparaison entre A* et Dijkstra et stocke les résultats."""
        for taux in self.taux_cases_interdites:
            cases_visitees_h_null   = []
            cases_visitees_h_ville  = []
            cases_visitees_h_oiseau = []
            temps_h_null            = []
            temps_h_ville           = []
            temps_h_oiseau          = []

            # Nombre d'itérations par défaut
            for _ in range(self.iteration):
                plateau = Plateau(self.largeur, self.longueur, taux / 100, True)

                # Exécution de A* avec heuristique null (Dijkstra)
                algo_heuristique_null = A_star(plateau, heuristique="N")
                start = time.time()
                nombre_cases_explorees_h_null = algo_heuristique_null.executer()
                if nombre_cases_explorees_h_null is not None:
                    cases_visitees_h_null.append(nombre_cases_explorees_h_null)
                temps_h_null.append(time.time() - start)

                # Exécution de A* avec heuristique ville
                algo_heuristique_ville = A_star(plateau, heuristique="V")
                start = time.time()
                nombre_cases_explorees_h_ville = algo_heuristique_ville.executer()
                if nombre_cases_explorees_h_ville is not None:
                    cases_visitees_h_ville.append(nombre_cases_explorees_h_ville)
                temps_h_ville.append(time.time() - start)

                # Exécution de A* avec heuristique oiseau
                algo_heuristique_oiseau = A_star(plateau, heuristique="O")
                start = time.time()
                nombre_cases_explorees_h_oiseau = algo_heuristique_oiseau.executer()
                if nombre_cases_explorees_h_oiseau is not None:
                    cases_visitees_h_oiseau.append(nombre_cases_explorees_h_oiseau)
                temps_h_oiseau.append(time.time() - start)

            # Stockage des moyennes pour chaque heuristique de l'algorithme A*
            self.moy_cases_visitees_h_null.append(sum(cases_visitees_h_null) / self.iteration)
            self.moy_cases_visitees_h_ville.append(sum(cases_visitees_h_ville) / self.iteration)
            self.moy_cases_visitees_h_oiseau.append(sum(cases_visitees_h_oiseau) / self.iteration)
            self.moy_temps_h_null.append(sum(temps_h_null) / self.iteration)
            self.moy_temps_h_ville.append(sum(temps_h_ville) / self.iteration)
            self.moy_temps_h_oiseau.append(sum(temps_h_oiseau) / self.iteration)

        # Affichage des résultats après l'exécution
        self.afficher_graphiques()

    def afficher_graphiques(self):
        """Affiche les graphiques pour les trois heuristiques de A*"""
        plt.figure(figsize=(10, 5))  # Taille du graphique

        # Comparaison du nombre de cases visitées
        plt.subplot(1, 2, 1)
        plt.plot(self.taux_cases_interdites, self.moy_cases_visitees_h_null,
                 label="Heuristique null", marker="o")
        plt.plot(self.taux_cases_interdites, self.moy_cases_visitees_h_ville,
                 label="Heuristique ville", marker="s")
        plt.plot(self.taux_cases_interdites, self.moy_cases_visitees_h_oiseau,
                 label="Heuristique oiseau", marker="v")
        plt.xlabel('Taux de cases interdites (%)')
        plt.ylabel('Moyenne des cases visitées')
        plt.title('Comparaison du nombre moyen de cases visitées')
        plt.legend()

        # Comparaison du temps d'exécution
        plt.subplot(1, 2, 2)
        plt.plot(self.taux_cases_interdites, self.moy_temps_h_null,
                 label="Heuristique null", marker="o")
        plt.plot(self.taux_cases_interdites, self.moy_temps_h_ville,
                 label="Heuristique ville", marker="s")
        plt.plot(self.taux_cases_interdites, self.moy_temps_h_oiseau,
                 label="Heuristique oiseau", marker="v")
        plt.xlabel('Taux de cases interdites (%)')
        plt.ylabel('Temps moyen d\'exécution (s)')
        plt.title('Comparaison du temps moyen d\'exécution')
        plt.legend()

        # Titre global
        plt.suptitle(
            f"Comparaison des heuristiques avec l'algorithme A* sur {self.iteration} itérations.",
            fontsize=14, fontweight='bold')

        plt.tight_layout()
        plt.savefig("comparaison.png")
        plt.show()

# Exécution de la comparaison
if __name__ == "__main__":
    comparaison = ComparaisonAStarDijkstra(largeur=50, longueur=125, max_taux=30)
    comparaison.executer()
