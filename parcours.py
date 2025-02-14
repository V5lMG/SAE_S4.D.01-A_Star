from heapq import heappop, heappush
from plateau import Plateau
import math

class Dijkstra:
    """Implémentation de l'algorithme de Dijkstra pour trouver le plus court chemin sur un plateau."""

    def __init__(self, plateau,):
        """
        Initialise l'algorithme avec un plateau.
        :param plateau: Objet Plateau contenant la grille de jeu.
        """
        self.plateau = plateau
        self.debut, self.fin = self.trouver_debut_fin()
        self.distances = {}  # Stocke les distances minimales
        self.precedents = {}  # Stocke les chemins parcourus
        self.explorees = set()  # Cases explorées
        self.chemin = []  # Stocke le chemin trouvé

    def trouver_debut_fin(self):
        """Trouve les coordonnées de départ et d'arrivée dans le plateau."""
        debut = fin = None
        for i in range(self.plateau.largeur):
            for j in range(self.plateau.longueur):
                case = self.plateau.grille[i][j]
                if case.est_depart():
                    debut = (i, j)
                elif case.est_arrivee():
                    fin = (i, j)
        return debut, fin

    def est_valide(self, x, y):
        """
        Vérifie si une case est valide (dans les limites et non interdite).
        """
        return (0 <= x < self.plateau.largeur
                and 0 <= y < self.plateau.longueur
                and not self.plateau.grille[x][y].est_interdite())

    def heuristique(a, b):
        """
        Calcul de la distance heuristique en vol d'oiseau
        """
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    def executer(self):
        """Exécute l'algorithme de Dijkstra pour trouver le chemin le plus court."""
        if not self.debut or not self.fin:
            print("❌ Impossible d'exécuter Dijkstra : départ ou arrivée manquants.")
            return [], set()

        # Initialisation des distances avec l'infini sauf pour la case de départ
        self.distances = {(i, j): float('inf') for i in range(self.plateau.largeur) for j in range(self.plateau.longueur)}
        self.distances[self.debut] = 0

        # File de priorité (tas) pour explorer les cases dans le bon ordre
        file_priorite = [(0, self.debut)]
        self.precedents[self.debut] = None

        while file_priorite:
            distance_actuelle, (x, y) = heappop(file_priorite)

            # Si nous avons atteint l'arrivée, on arrête
            if (x, y) == self.fin:
                break

            # Exploration des voisins (droite, bas, gauche, haut)
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy

                if self.est_valide(nx, ny) and (nx, ny) not in self.explorees:
                    nouvelle_distance = distance_actuelle + 1
                    if nouvelle_distance < self.distances[(nx, ny)]:
                        self.distances[(nx, ny)] = nouvelle_distance
                        self.precedents[(nx, ny)] = (x, y)
                        heappush(file_priorite, (nouvelle_distance, (nx, ny)))
                        self.explorees.add((nx, ny))  # Marquer comme exploré

        # Reconstruire le chemin le plus court
        self.chemin = self.reconstruire_chemin()
        return self.chemin, self.explorees

    def reconstruire_chemin(self):
        """Recrée le chemin à partir des précédents."""
        chemin = []
        actuel = self.fin
        while actuel:
            chemin.append(actuel)
            actuel = self.precedents.get(actuel)
        return chemin[::-1]  # Inverser pour partir de D → A

    def afficher_resultat(self):
        """Affiche le plateau avec les cases explorées et le chemin."""
        print("\n🔍 **Plateau avec chemin trouvé par Dijkstra :**")
        grille_affichage = [[case.get_type() for case in ligne] for ligne in self.plateau.grille]

        # Marquer les cases explorées
        for x, y in self.explorees:
            if grille_affichage[x][y] == "O":
                grille_affichage[x][y] = "*"

        # Marquer le chemin final
        for x, y in self.chemin:
            if grille_affichage[x][y] not in ["D", "A"]:
                grille_affichage[x][y] = "."

        # Affichage du plateau
        for ligne in grille_affichage:
            print(" ".join(ligne))
        print()

        return grille_affichage

# Test
if __name__ == "__main__":
    # Création d'un plateau pour tester
    plateau_test = Plateau(5, 7, 0.2, True)

    # Lancer Dijkstra
    algo = Dijkstra(plateau_test)
    chemin, explorees = algo.executer()
    algo.afficher_resultat()


# Algorithme de A*
# def a_star(plateau):
#     debut, fin = trouver_debut_fin(plateau)
#
#     # Création de la liste des distances avec des valeurs infinies
#     distances = [[float('inf')] * len(plateau[0]) for _ in range(len(plateau))]
#     distances[debut[0]][debut[1]] = 0
#
#     # File de case de priorité pour explorer les cases avec la plus petite distance en premier
#     case_prioritaire = [(0, debut)]  # Seulement la case de départ pour initialisation
#
#     # Dictionnaire pour retracer le chemin une fois l'arrivée atteinte
#     precedente = {debut: None}
#
#     # Ensemble pour stocker les cases réellement explorées
#     explorees = {debut}
#
#     while case_prioritaire:
#         # Trie la liste en fonction de la priorité (distance + heuristique)
#         case_prioritaire.sort()
#
#         # Récupère l'élément avec la plus petite priorité
#         distance_actuelle, (x, y) = case_prioritaire.pop(0)
#
#         # Si nous avons atteint l'arrivée, on sort de la boucle
#         if (x, y) == fin:
#             break
#
#         # Exploration des voisins (droite, bas, gauche, haut)
#         for dx, dy in directions:
#             nouveau_x, nouveau_y = x + dx, y + dy
#
#             if est_valide(plateau, nouveau_x, nouveau_y) and (nouveau_x, nouveau_y) not in explorees:
#                 nouvelle_distance = distance_actuelle + 1
#
#                 if nouvelle_distance < distances[nouveau_x][nouveau_y]:
#                     distances[nouveau_x][nouveau_y] = nouvelle_distance
#
#                     # Ajoute la distance, l'heuristique et les coordonnées dans le tableau des priorités
#                     priorite = heuristique((nouveau_x, nouveau_y), fin)
#                     case_prioritaire.append((priorite, (nouveau_x, nouveau_y)))
#
#                     # Trie la liste pour maintenir l'ordre de priorité
#                     case_prioritaire.sort()
