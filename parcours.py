import generation
import math

# Représentation du plateau de jeu
plateau = generation.generation_plateau(50, 50, 0.15, True)

# Contient les vecteurs de déplacement pour les 4 directions cardinales : droite, bas, gauche, haut
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Trouver les coordonnées de départ et d'arrivée
def trouver_debut_fin(plateau):
    debut = fin = 0

    # Parcours chaque ligne du tableau
    for i, ligne in enumerate(plateau):

        # Parcours chaque case du tableau
        for j, case in enumerate(ligne):
            if case == 'D':
                debut = (i, j)
            elif case == 'A':
                fin = (i, j)
    return debut, fin

# Vérifier si une case est valide pour être explorée,
# C'est-à-dire qu'elle est à l'intérieur des limites du plateau, qu'elle n'est pas un obstacle (X),
# ni déjà marquée dans le chemin (*).
def est_valide(plateau, x, y):
    return      (0 <= x < len(plateau)         # Si l'abscisse (x) est dans le plateau
            and 0 <= y < len(plateau[0])       # Si l'ordonnée (x) est dans le plateau
            and plateau[x][y] not in ['X'])    # Vérifie que la case n'est pas un mur (X)

# Calcul de la distance heuristique
def heuristique(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Algorithme de Dijkstra
def dijkstra(plateau):
    debut, fin = trouver_debut_fin(plateau)

    # Création de la liste des distances avec des valeurs infinies
    distances = [[float('inf')] * len(plateau[0]) for _ in range(len(plateau))]
    distances[debut[0]][debut[1]] = 0
    # Affiche les distances de chaque depuis le départ (initialisées à infini)
#    for ligne in distances:
#        print(" ".join(map(str, ligne)))

    # File de case de priorité pour explorer les cases avec la plus petite distance en premier
    case_prioritaire = [(0, debut)] # Seulement la case de départ pour initialisation

    # Dictionnaire pour retracer le chemin une fois l'arrivée atteinte
    precedente = {debut: None}

    # Ensemble pour stocker les cases réellement explorées
    explorees = {debut}

    while case_prioritaire:
        # Trie la liste en fonction de la priorité
        case_prioritaire.sort()

        # Récupère l'élément avec la plus petite priorité
        distance_actuelle, (x, y) = case_prioritaire.pop(0)

        # Si nous avons atteint l'arrivée, on sort de la boucle
        if (x, y) == fin:
            break

        # Exploration des voisins (droite, bas, gauche, haut)
        for dx, dy in directions:
            nouveau_x, nouveau_y = x + dx, y + dy

            if est_valide(plateau, nouveau_x, nouveau_y) and (nouveau_x, nouveau_y) not in explorees:
                nouvelle_distance = distance_actuelle + 1
                if nouvelle_distance < distances[nouveau_x][nouveau_y]:
                    distances[nouveau_x][nouveau_y] = nouvelle_distance

                    # Ajoute la distance et les coordonnées dans le tableau des priorités
                    case_prioritaire.append((nouvelle_distance, (nouveau_x, nouveau_y)))

                    # Trie la liste pour maintenir l'ordre de priorité
                    case_prioritaire.sort()

                    # Récupère les coordonnées pour retracer le chemin
                    precedente[(nouveau_x, nouveau_y)] = (x, y)
                    explorees.add((nouveau_x, nouveau_y))  # Marquer la case comme explorée

    # Recréation du chemin le plus court en partant de la fin
    chemin = []
    actuel = fin
    while actuel:
        chemin.append(actuel)
        actuel = precedente.get(actuel)

    # Inversion du chemin pour qu'il parte de 'D' à 'A'
    chemin = chemin[::-1]
    return chemin, explorees

# Algorithme de A*
def a_star(plateau):
    debut, fin = trouver_debut_fin(plateau)

    # Création de la liste des distances avec des valeurs infinies
    distances = [[float('inf')] * len(plateau[0]) for _ in range(len(plateau))]
    distances[debut[0]][debut[1]] = 0

    # File de case de priorité pour explorer les cases avec la plus petite distance en premier
    case_prioritaire = [(0, debut)]  # Seulement la case de départ pour initialisation

    # Dictionnaire pour retracer le chemin une fois l'arrivée atteinte
    precedente = {debut: None}

    # Ensemble pour stocker les cases réellement explorées
    explorees = {debut}

    while case_prioritaire:
        # Trie la liste en fonction de la priorité (distance + heuristique)
        case_prioritaire.sort()

        # Récupère l'élément avec la plus petite priorité
        distance_actuelle, (x, y) = case_prioritaire.pop(0)

        # Si nous avons atteint l'arrivée, on sort de la boucle
        if (x, y) == fin:
            break

        # Exploration des voisins (droite, bas, gauche, haut)
        for dx, dy in directions:
            nouveau_x, nouveau_y = x + dx, y + dy

            if est_valide(plateau, nouveau_x, nouveau_y) and (nouveau_x, nouveau_y) not in explorees:
                nouvelle_distance = distance_actuelle + 1

                if nouvelle_distance < distances[nouveau_x][nouveau_y]:
                    distances[nouveau_x][nouveau_y] = nouvelle_distance

                    # Ajoute la distance, l'heuristique et les coordonnées dans le tableau des priorités
                    priorite = heuristique((nouveau_x, nouveau_y), fin)
                    case_prioritaire.append((priorite, (nouveau_x, nouveau_y)))

                    # Trie la liste pour maintenir l'ordre de priorité
                    case_prioritaire.sort()

                    # Récupère les coordonnées pour retracer le chemin
                    precedente[(nouveau_x, nouveau_y)] = (x, y)
                    explorees.add((nouveau_x, nouveau_y))  # Marquer la case comme explorée

    # Recréation du chemin le plus court en partant de la fin
    chemin = []
    actuel = fin
    while actuel:
        chemin.append(actuel)
        actuel = precedente.get(actuel)

    # Inversion du chemin pour qu'il parte de 'D' à 'A'
    chemin = chemin[::-1]
    return chemin, explorees


# Affichage du plateau avec les explorations (*) et le chemin (.)
def affichage_chemin(plateau, chemin, explorees, choix):
    plateau_avec_chemin = [ligne[:] for ligne in plateau]  # Copie du plateau original
    nbr_cases_visitees = 0

    # Marquer les cases explorées par des points (*) uniquement si elles ont été réellement atteintes
    for (x, y) in explorees:
        if plateau_avec_chemin[x][y] == 'O':  # Marquer uniquement les cases atteignables
            plateau_avec_chemin[x][y] = '*'
            nbr_cases_visitees = nbr_cases_visitees + 1

    # Marquer le chemin avec des étoiles (.)
    for (x, y) in chemin:
        if plateau_avec_chemin[x][y] not in ['D', 'A']:
            plateau_avec_chemin[x][y] = '.'

    if choix == "C":
        return plateau_avec_chemin, nbr_cases_visitees

    # Affichage du plateau de départ
    print("Plateau de départ :")
    for ligne in plateau:
        print(' '.join(ligne))
    print()

    # Affichage du plateau avec le chemin
    print("Plateau avec le chemin trouvé par Dijkstra :")
    for ligne in plateau_avec_chemin:
        print(' '.join(ligne))

    return plateau_avec_chemin, nbr_cases_visitees

# Exécution de l'algorithme
# dijkstra(plateau)
