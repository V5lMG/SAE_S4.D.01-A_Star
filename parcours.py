import math
from plateau import Plateau

class A_star:
    """Implémente A* par défaut et bascule sur Dijkstra si nécessaire."""

    def __init__(self, plateau, use_a_star=True):
        """
        Initialise l'algorithme.
        :param plateau: Instance de Plateau.
        :param use_a_star: Utiliser A* (True) ou Dijkstra (False).
        """
        self.plateau = plateau
        self.use_a_star = use_a_star
        self.debut, self.fin = self.trouver_debut_fin()
        self.distances = {}
        self.precedents = {}
        self.explorees = set()
        self.chemin = []

    def trouver_debut_fin(self):
        """Identifie les coordonnées du départ et de l'arrivée."""
        debut = fin = None
        for i in range(self.plateau.largeur):
            for j in range(self.plateau.longueur):
                case = self.plateau.cases[i][j]
                if case.est_depart():
                    debut = (i, j)
                elif case.est_arrivee():
                    fin = (i, j)
        return debut, fin

    def est_valide(self, x, y):
        """Vérifie si une case est dans les limites et traversable."""
        return (0 <= x < self.plateau.largeur
                and 0 <= y < self.plateau.longueur
                and self.plateau.cases[x][y].est_traversable())

    def heuristique(self, a, b):
        """Retourne la distance heuristique entre deux points."""
        if self.use_a_star:
            # Calcul de l'heuristique
            dist = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
            return dist
        else:
            return 0

    def executer(self):
        """Exécute A* ou Dijkstra selon la configuration."""
        if not self.debut or not self.fin:
            print("Erreur : Départ ou arrivée introuvables.")
            return [], set()

        # Initialisation des distances et de la file de priorité
        self.distances = {(i, j): float('inf') for i in range(self.plateau.largeur) for j in range(self.plateau.longueur)}
        self.distances[self.debut] = 0
        file_priorite = [(0, self.debut)]
        self.precedents[self.debut] = None

        while file_priorite:
            file_priorite.sort() # Tri basé sur la priorité (premier élément du tuple)
            _, (x, y) = file_priorite.pop(0)

            # Si arrivée atteinte, on stoppe
            if (x, y) == self.fin:
                break

            # Exploration des voisins (droite, bas, gauche, haut)
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy

                if self.est_valide(nx, ny):
                    nouvelle_distance = self.distances[(x, y)] + 1

                    if nouvelle_distance < self.distances[(nx, ny)]:
                        self.distances[(nx, ny)] = nouvelle_distance
                        self.precedents[(nx, ny)] = (x, y)

                        # Vérification que les coordonnées sont valides avant d'appliquer l'heuristique
                        if not (0 <= nx < self.plateau.largeur and 0 <= ny < self.plateau.longueur):
                            print(f"Coordonnées invalides : ({nx}, {ny})")
                            continue  # Ignore ces coordonnées invalides

                        # Vérifier que `self.fin` contient des valeurs correctes
                        if not (0 <= self.fin[0] < self.plateau.largeur and 0 <= self.fin[1] < self.plateau.longueur):
                            print(f"Erreur : Arrivée (fin) hors limites : {self.fin}")
                            return [], set()

                        # Calcul de la priorité avec une heuristique (si A* est utilisé)
                        try:
                            priorite = nouvelle_distance + self.heuristique((nx, ny), self.fin)
                        except ValueError as e:
                            print(f"Erreur lors du calcul de l'heuristique : {e}")
                            continue

                        file_priorite.append((priorite, (nx, ny)))
                        file_priorite.sort()
                        self.explorees.add((nx, ny))

        # Reconstruire le chemin
        self.chemin = self.reconstruire_chemin()
        return self.chemin, self.explorees

    def reconstruire_chemin(self):
        """Reconstruit le chemin optimal."""
        chemin = []
        actuel = self.fin
        while actuel:
            chemin.append(actuel)
            actuel = self.precedents.get(actuel)
        return chemin[::-1]  # Inversé pour partir du départ
    
    def afficher_resultat(self):
        """Affiche le plateau avec le chemin et les explorations."""
        grille_affichage = [[case.type_case for case in ligne] for ligne in self.plateau.cases]

        # Marquer les cases explorées
        for x, y in self.explorees:
            if grille_affichage[x][y] == "O":
                grille_affichage[x][y] = "*"

        # Marquer le chemin final
        for x, y in self.chemin:
            if grille_affichage[x][y] not in ["D", "A"]:
                grille_affichage[x][y] = "."

        # Affichage du plateau
        print("\nPlateau avec chemin trouvé :")
        for ligne in grille_affichage:
            print(" ".join(ligne))
        print()

        return grille_affichage

# Test
if __name__ == "__main__":
   plateau_test = Plateau(10, 10, 0.2, True)
   # Lancer A* (par défaut)
   algo = A_star(plateau_test, use_a_star=True)
   algo.executer()
   algo.afficher_resultat()
   # Lancer Dijkstra (sans heuristique)
   algo_dijkstra = A_star(plateau_test, use_a_star=False)
   algo_dijkstra.executer()
   algo_dijkstra.afficher_resultat()
