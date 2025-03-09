import math
import time


def a_star(grille, depart, arrivee):
    """Implémente l'algorithme A* sans utiliser heapq, avec affichage des cases visitées."""

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Droite, Gauche, Bas, Haut
    open_set = [(0, depart)]  # Liste des nœuds à explorer

    came_from = {}
    g_score = {depart: 0}
    f_score = {depart: calcul_heuristique(depart, arrivee)}

    # Copie de la grille pour affichage
    grille_visu = [row[:] for row in grille]

    while open_set:
        # Trier et récupérer le meilleur
        open_set.sort(key=lambda x: x[0])
        _, current = open_set.pop(0)

        # Afficher la grille avec les cases visitées
        grille_visu[current[0]][current[1]] = "V"
        afficher_grille(grille_visu)
        time.sleep(0.2)  # Pause pour voir l'évolution

        if current == arrivee:
            return reconstruire_chemin(came_from, depart, arrivee, grille_visu)

        for dx, dy in directions:
            voisin = (current[0] + dx, current[1] + dy)

            if 0 <= voisin[0] < len(grille) and 0 <= voisin[1] < len(grille[0]) and grille[voisin[0]][voisin[1]] == 0:
                tentative_g_score = g_score[current] + 1

                if voisin not in g_score or tentative_g_score < g_score[voisin]:
                    came_from[voisin] = current
                    g_score[voisin] = tentative_g_score
                    f_score[voisin] = tentative_g_score + calcul_heuristique(voisin, arrivee)

                    open_set.append((f_score[voisin], voisin))

    return None  # Aucun chemin trouvé


def calcul_heuristique(a, b):
    """Retourne la distance heuristique entre deux points (Manhattan)."""
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def reconstruire_chemin(came_from, depart, arrivee, grille_visu):
    """Reconstruit le chemin final et l'affiche."""
    chemin = []
    current = arrivee

    while current in came_from:
        chemin.append(current)
        current = came_from[current]

    chemin.append(depart)
    chemin.reverse()

    # Marquer le chemin dans la grille
    for x, y in chemin:
        grille_visu[x][y] = "*"

    afficher_grille(grille_visu)
    return chemin


def afficher_grille(grille):
    """Affiche la grille avec les cases visitées et le chemin final."""
    print("\n".join(" ".join(str(cell) for cell in row) for row in grille))
    print("\n" + "-" * 20 + "\n")


# Grille de test (0 = libre, 1 = mur)
grille = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

depart = (0, 0)
arrivee = (4, 4)

chemin = a_star(grille, depart, arrivee)
print("Chemin trouvé :", chemin)
