import math
from plateau import Plateau


class A_star:
    """Implémente A* par défaut et bascule sur Dijkstra si nécessaire."""

    def __init__(self, plateau, heuristique):
        """
        Initialise l'algorithme.
        :param plateau: Instance de Plateau.
        :param heuristique: Type d'heuristique ('V' pour Ville, 'O' pour Oiseau, 'N' pour Dijkstra).
        """
        self.plateau = plateau
        self.type_heuristique = heuristique

        self.debut, self.fin = self.trouver_debut_fin()
        self.distances = {self.debut: 0}                    # Dictionnaire des distances depuis le départ
        self.precedents = {}                                # Dictionnaire pour reconstruire le chemin
        self.cases_explorees = set()                        # Ensemble des cases déjà explorées
        self.en_attente = {self.debut}                      # Ensemble des cases en attente d'exploration

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
        return (    0 <= x < self.plateau.largeur
                and 0 <= y < self.plateau.longueur
                and self.plateau.cases[x][y].est_traversable())

    def calcul_heuristique(self, case_actuelle, arrive):
        """Retourne la distance heuristique entre deux points selon l'heuristique choisie."""
        # Calcul de h
        if   self.type_heuristique == "V":     # Distance de Manhattan
            return abs(case_actuelle[0] - arrive[0]) + abs(case_actuelle[1] - arrive[1])
        elif self.type_heuristique == "O":     # Distance Euclidienne
            return math.sqrt((case_actuelle[0] - arrive[0]) ** 2 + (case_actuelle[1] - arrive[1]) ** 2)
        elif self.type_heuristique == "N":     # Dijkstra (pas d'heuristique)
            return 0

        else:
            raise ValueError(f"Heuristique inconnue : {self.type_heuristique}")

    def cout_total(self, case):
        return self.distances[case] + self.calcul_heuristique(case, self.fin)

    def cout_total_puis_heuristique(self, case):
        return self.cout_total(case), self.calcul_heuristique(case, self.fin)

    def executer(self):
        """Exécute l'algorithme A*."""

        # Gérer les erreurs
        if not self.debut or not self.fin:
            print("Erreur : Départ ou arrivée introuvables.")
            return

        # Droite, Bas, Gauche, Haut
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Boucle principale
        while self.en_attente:
            # Cas ou le départ / l'arrivé est bloqué dans les obstacles
            if not self.en_attente:
                print("Erreur : Aucune solution trouvée, l'algorithme est bloqué.")
                return self.nombre_cases_explorees

            # Trier d'abord par le coût total f = g + h, puis par h seul en cas d'égalité
            case_actuelle = min(self.en_attente, key=self.cout_total_puis_heuristique)

            # Si on atteint la case d'arrivée, on arrête l'algorithme
            if case_actuelle == self.fin:
                self.chemin = self.reconstruire_chemin()
                return self.nombre_cases_explorees

            # Marquer la case actuelle comme explorée
            self.en_attente.remove(case_actuelle)
            self.cases_explorees.add(case_actuelle)
            self.nombre_cases_explorees += 1

            # Explorer les voisins valides
            voisins = []
            for dx, dy in directions:
                # Calcul des coordonnées du voisin en fonction de la direction actuelle
                voisin_x, voisin_y = case_actuelle[0] + dx, case_actuelle[1] + dy
                voisin = (voisin_x, voisin_y)

                # Vérifier si le voisin est dans les limites et traversable
                if self.est_valide(voisin_x, voisin_y) and voisin not in self.cases_explorees:
                    nouveau_cout = self.distances[case_actuelle] + 1  # Coût du déplacement (g)

                    # Mettre à jour le coût et le chemin si on trouve un meilleur chemin vers ce voisin
                    if voisin not in self.distances or nouveau_cout < self.distances[voisin]:
                        # Met à jour g (distance depuis le départ)
                        self.distances[voisin] = nouveau_cout
                        # Enregistre le voisin
                        self.precedents[voisin] = case_actuelle
                        # Ajoute le voisin à la liste avec f = g + h
                        voisins.append((self.cout_total(voisin), voisin))

            # Trier les voisins en fonction de f = g + h pour explorer en priorité les plus prometteurs
            voisins.sort()

            # Ajouter les voisins triés à la liste des cases à explorer
            for _, voisin in voisins:
                self.en_attente.add(voisin)


    def reconstruire_chemin(self):
        """Reconstruit le chemin optimal."""
        chemin = []
        actuel = self.fin
        while actuel:
            chemin.append(actuel)
            actuel = self.precedents.get(actuel)
        return chemin[::-1]  # Inversé pour partir du départ

    def afficher_bilan(self):
        print(f"\nNombre de cases visitées (départ en arrivé compris) : {self.nombre_cases_explorees + 1}") # +1 pour ajouter le départ
        print(f"Taille du chemin final                              "
              f": {self.taille_chemin_final    + 2}\n") # +2 pour ajouter le départ et l'arrivée

    def afficher_resultat(self):
        """Affiche le plateau avec le chemin et les explorations."""
        grille_affichage = [[case.type_case for case in ligne] for ligne in self.plateau.cases]

        # Marquer les cases explorées
        for x, y in self.cases_explorees:
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
            heuristique_p = "Sans heuristique (Dijkstra)"

        # Affichage du plateau
        print(f"\nPlateau avec chemin trouvé par l'heuristique {heuristique_p} :")
        for ligne in grille_affichage:
            print(" ".join(ligne))

        self.afficher_bilan()
        return grille_affichage


# Test
if __name__ == "__main__":
    plateau_test = Plateau(10, 10, 0, False)

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