import matplotlib.pyplot as plt
from parcours import A_star
from plateau import Plateau
import time

class ComparaisonAStarDijkstra:

    def __init__(self, largeur, longueur, max_taux):
        self.largeur = largeur
        self.longueur = longueur
        self.taux_cases_interdites = list(range(max_taux))  # Converti en liste pour éviter les erreurs d'indexation
        self.moy_cases_visitees_dijkstra = []
        self.moy_cases_visitees_a_star   = []
        self.moy_temps_dijkstra          = []
        self.moy_temps_a_star            = []
        self.iteration                   = 5                # Nombre d'itération par défaut

    def executer(self):
        """Exécute la comparaison entre A* et Dijkstra et stocke les résultats."""
        for taux in self.taux_cases_interdites:
            cases_visitees_dijkstra = []
            cases_visitees_a_star   = []
            temps_dijkstra          = []
            temps_a_star            = []

            # Nombre d'itéarion par défaut = 50
            for _ in range(self.iteration):
                plateau = Plateau(self.largeur, self.longueur, taux / 100, True)

                # Exécution de Dijkstra (sur la place publique o_o)
                algo_dijkstra = A_star(plateau, use_a_star=False)
                start = time.time()
                _, cases_explorees_dijkstra = algo_dijkstra.executer()
                temps_dijkstra.append(time.time() - start)
                cases_visitees_dijkstra.append(len(cases_explorees_dijkstra))

                # Exécution de A*
                algo_a_star = A_star(plateau, use_a_star=True)
                start = time.time()
                _, cases_explorees_a_star = algo_a_star.executer()
                temps_a_star.append(time.time() - start)
                cases_visitees_a_star.append(len(cases_explorees_a_star))

            # Stockage des moyennes pour chaque algorithmes
            self.moy_cases_visitees_dijkstra.append(sum(cases_visitees_dijkstra) / 50)
            self.moy_cases_visitees_a_star.append(sum(cases_visitees_a_star) / 50)
            self.moy_temps_dijkstra.append(sum(temps_dijkstra) / 50)
            self.moy_temps_a_star.append(sum(temps_a_star) / 50)

        # Affichage des résultats après l'exécution
        self.afficher_graphiques()

    def afficher_graphiques(self):
        """Affiche les graphiques comparant A* et Dijkstra."""
        plt.figure(figsize=(10, 5))

        # Comparaison du nombre de cases visitées
        plt.subplot(1, 2, 1)
        plt.plot(self.taux_cases_interdites, self.moy_cases_visitees_dijkstra, label="Dijkstra", marker="o")
        plt.plot(self.taux_cases_interdites, self.moy_cases_visitees_a_star, label="A*", marker="s")
        plt.xlabel('Taux de cases interdites (%)')
        plt.ylabel('Moyenne des cases visitées')
        plt.title('Comparaison du nombre moyen de cases visitées')
        plt.legend()

        # Comparaison du temps d'exécution
        plt.subplot(1, 2, 2)
        plt.plot(self.taux_cases_interdites, self.moy_temps_dijkstra, label="Dijkstra", marker="o")
        plt.plot(self.taux_cases_interdites, self.moy_temps_a_star, label="A*", marker="s")
        plt.xlabel('Taux de cases interdites (%)')
        plt.ylabel('Temps moyen d\'exécution (s)')
        plt.title('Comparaison du temps moyen d\'exécution')
        plt.legend()

        # Titre global
        plt.suptitle(f"Comparaison entre l'algorithme A* et Dijkstra sur {self.iteration} itérations. ",
                     fontsize=14, fontweight='bold')

        plt.tight_layout()
        plt.savefig("comparaison.png")
        plt.show()

# Exécution de la comparaison
if __name__ == "__main__":
    comparaison = ComparaisonAStarDijkstra(largeur=50, longueur=125, max_taux=30)
    comparaison.executer()