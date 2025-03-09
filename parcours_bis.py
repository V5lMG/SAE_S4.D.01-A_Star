import math
from plateau import Plateau


class A_star:
    """Implémente A* avec l'heuristique de Manhattan."""

    def __init__(self, plateau):
        """
        Initialise l'algorithme de recherche A* avec l'heuristique de Manhattan.

        :param plateau: Instance de la classe Plateau contenant la grille du jeu.

        Attributs :
        - self.plateau : Référence au plateau contenant les cases.
        - self.debut : Coordonnées du point de départ (x, y).
        - self.fin : Coordonnées du point d'arrivée (x, y).
        - self.distances : Dictionnaire stockant la distance minimale connue pour chaque case.
        - self.precedents : Dictionnaire permettant de reconstruire le chemin optimal.
        - self.explorees : Ensemble des cases déjà explorées.
        - self.nombre_cases_explorees : Compteur du nombre de cases visitées durant la recherche.
        - self.taille_chemin_final : Longueur du chemin optimal trouvé.
        - self.chemin : Liste des coordonnées représentant le chemin optimal trouvé.
        """
        self.plateau = plateau
        self.debut, self.fin = self.trouver_debut_fin()
        self.distances = {}
        self.precedents = {}
        self.explorees = set()
        self.nombre_cases_explorees = 0
        self.taille_chemin_final = 0
        self.chemin = []
        # Directions (droite, bas, gauche, haut, diagonales)
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 4 directions pour Manhattan

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

    def calcul_heuristique(self, a, b):
        """Retourne la distance heuristique de Manhattan entre deux points."""
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

    def executer(self):
        """Exécute l'algorithme A* avec l'heuristique de Manhattan."""
        # Initialisation des distances et de la file d'attente
        self.distances[self.debut] = 0  # Distance du point de départ
        self.precedents[self.debut] = None  # Pas de précédent pour le départ
        self.explorees.add(self.debut)  # Ajouter le point de départ aux explorées
        self.nombre_cases_explorees += 1

        # Utilisation d'une liste pour explorer les cases (file de priorité basée sur f = g + h)
        open_list = [(0 + self.calcul_heuristique(self.debut, self.fin), self.debut)]

        while open_list:
            # Extraire le noeud avec la plus petite valeur f
            open_list.sort()
            _, current = open_list.pop(0)

            # Si on a atteint l'objectif, on reconstruit le chemin
            if current == self.fin:
                self.chemin = self.reconstruire_chemin()
                self.taille_chemin_final = len(self.chemin) - 1  # Ne pas compter le départ
                return

            # Explorer les voisins
            for direction in self.directions:
                voisin = (current[0] + direction[0], current[1] + direction[1])

                if self.est_valide(voisin[0], voisin[1]) and voisin not in self.explorees:
                    # Calcul de la distance g pour le voisin
                    g = self.distances[current] + 1  # 1 pour chaque déplacement
                    # Calcul de la fonction f = g + h (distance réelle + heuristique)
                    f = g + self.calcul_heuristique(voisin, self.fin)

                    if voisin not in self.distances or g < self.distances[voisin]:
                        # Mettre à jour la distance et le précédent
                        self.distances[voisin] = g
                        self.precedents[voisin] = current
                        open_list.append((f, voisin))  # Ajouter le voisin à la liste ouverte
                        self.explorees.add(voisin)  # Marquer le voisin comme exploré
                        self.nombre_cases_explorees += 1

    def reconstruire_chemin(self):
        """Reconstruit le chemin optimal."""
        chemin = []
        actuel = self.fin
        while actuel:
            chemin.append(actuel)
            actuel = self.precedents.get(actuel)
        return chemin[::-1]  # Inversé pour partir du départ

    def afficher_bilan(self):
        print("")
        print(f"Nombre de cases visitées : {self.nombre_cases_explorees}")  # Ajouter une case pour compter le départ
        print(f"Taille du chemin final : {self.taille_chemin_final}")  # Ajouter deux pour compter le départ et l'arrivée
        print("")

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
                self.taille_chemin_final += 1

        # Affichage du plateau
        print(f"\nPlateau avec chemin trouvé par l'heuristique de Manhattan :")
        for ligne in grille_affichage:
            print(" ".join(ligne))

        self.afficher_bilan()
        return grille_affichage


# Test
if __name__ == "__main__":
    plateau_test = Plateau(10, 10, 0, False)

    # Lancer A* avec heuristique Manhattan
    algo = A_star(plateau_test)
    algo.executer()
    algo.afficher_resultat()
