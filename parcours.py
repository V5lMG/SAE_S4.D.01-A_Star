import math
from plateau import Plateau


class A_star:
    """Implémente A* par défaut et bascule sur Dijkstra si nécessaire."""

    def __init__(self, plateau, heuristique="V"):
        """
        Initialise l'algorithme.
        :param plateau: Instance de Plateau.
        :param heuristique: Type d'heuristique ('V' pour Ville, 'O' pour Oiseau, 'N' pour Dijkstra).
        """
        self.plateau = plateau
        self.type_heuristique = heuristique
        self.debut, self.fin = self.trouver_debut_fin()
        self.distances = {}
        self.precedents = {}
        self.explorees = set()
        self.nombre_cases_explorees = 0
        self.taille_chemin_final = 0
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

    def calcul_heuristique(self, a, b):
        """Retourne la distance heuristique entre deux points selon l'heuristique choisie."""
        if self.type_heuristique == "V":  # Distance de Manhattan
            return abs(b[0] - a[0]) + abs(b[1] - a[1])
        elif self.type_heuristique == "O":  # Distance Euclidienne
            return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        elif self.type_heuristique == "N":  # Dijkstra (pas d'heuristique)
            return 0
        else:
            raise ValueError(f"Heuristique inconnue : {self.type_heuristique}")

    def executer(self):
        """Exécute l'algorithme avec la bonne heuristique."""
        if not self.debut or not self.fin:
            print("Erreur : Départ ou arrivée introuvables.")
            return [], set()

        # Initialisation des distances et de la file de priorité
        self.distances = {(i, j): float('inf') for i in
                          range(self.plateau.largeur) for j in
                          range(self.plateau.longueur)}
        self.distances[self.debut] = 0
        file_priorite = [(0, self.debut)]  # (priorité, (x, y))

        self.precedents[self.debut] = None

        while file_priorite:
            file_priorite.sort()  # Tri manuel pour simuler le comportement d'un tas
            _, (x, y) = file_priorite.pop(
                0)  # Extraire la case avec la plus basse priorité

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

                        # Vérification de la validité de `self.fin`
                        if not (0 <= self.fin[0] < self.plateau.largeur and 0 <=
                                self.fin[1] < self.plateau.longueur):
                            print(f"Erreur : Arrivée hors limites : {self.fin}")
                            return [], set()

                        # Calcul de la priorité avec l'heuristique choisie
                        priorite = nouvelle_distance + self.calcul_heuristique(
                            (nx, ny), self.fin)

                        file_priorite.append(
                            (priorite, (nx, ny)))  # Ajouter à la liste
                        file_priorite.sort()  # Réordonner la liste
                        self.explorees.add((nx, ny))
                        self.nombre_cases_explorees += 1

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

    def afficher_bilan(self):
        print("")
        print(f"Nombre de cases visistées {self.nombre_cases_explorees}")
        print(f"Taille du chemin final : {self.taille_chemin_final}")
        print("")

    def afficher_resultat(self):
        """Affiche le plateau avec le chemin et les explorations."""
        grille_affichage = [[case.type_case for case in ligne] for ligne in
                            self.plateau.cases]

        # Marquer les cases explorées
        for x, y in self.explorees:
            if grille_affichage[x][y] == "O":
                grille_affichage[x][y] = "*"


        # Marquer le chemin final
        for x, y in self.chemin:
            if grille_affichage[x][y] not in ["D", "A"]:
                grille_affichage[x][y] = "."
                self.taille_chemin_final += 1

        # String de l'heuristique choisi
        if self.type_heuristique == "V":
            heuristique_p = "Ville (Manhattan)"
        elif self.type_heuristique == "O":
            heuristique_p = "Oiseau (Euclidienne)"
        else:
            heuristique_p = "Dijkstra (Sans heuristique)"

        # Affichage du plateau
        print(f"\nPlateau avec chemin trouvé par l'heuristique {heuristique_p} :")
        for ligne in grille_affichage:
            print(" ".join(ligne))

        self.afficher_bilan()
        return grille_affichage

# Test
if __name__ == "__main__":
    plateau_test = Plateau(10, 15, 0, False)

    # Lancer A* avec heuristique Ville
    algo = A_star(plateau_test, heuristique="V")
    algo.executer()
    algo.afficher_resultat()

    # Lancer A* avec heuristique Oiseau
    algo_oiseau = A_star(plateau_test, heuristique="O")
    algo_oiseau.executer()
    algo_oiseau.afficher_resultat()

    # Lancer Dijkstra (heuristique null)
    algo_dijkstra = A_star(plateau_test, heuristique="N")
    algo_dijkstra.executer()
    algo_dijkstra.afficher_resultat()
