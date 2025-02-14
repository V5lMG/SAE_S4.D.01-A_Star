import random
import case

class Plateau:
    def __init__(self, largeur, longueur, taux_cases_interdite,
                 depart_arrivee_aleatoire):
        self.largeur = largeur
        self.longueur = longueur
        self.cases = []
        self.depart = None
        self.arrivee = None
        self.generer_plateau(taux_cases_interdite, depart_arrivee_aleatoire)

    def generer_plateau(self, taux_cases_interdite, depart_arrivee_aleatoire):
        # Création d'un plateau vide
        self.cases = [[case.Case(x, y, 'O') for y in range(self.longueur)] for x in
                      range(self.largeur)]

        # Ajout des cases interdites
        for x in range(self.largeur):
            for y in range(self.longueur):
                if random.random() < taux_cases_interdite:
                    self.cases[x][y].type_case = 'X'

        # Positionner le départ et l'arrivée
        if not depart_arrivee_aleatoire:
            self.depart = self.cases[0][0]
            self.arrivee = self.cases[self.largeur - 1][self.longueur - 1]
        else:
            self.depart = random.choice(
                [case for row in self.cases for case in row if
                 case.type_case == 'O'])
            self.arrivee = random.choice(
                [case for row in self.cases for case in row if
                 case.type_case == 'O' and case != self.depart])

        self.depart.type_case = 'D'
        self.arrivee.type_case = 'A'

    def afficher_plateau(self):
        for ligne in self.cases:
            print(' '.join(str(case) for case in ligne))

    def get_case(self, x, y):
        if 0 <= x < self.largeur and 0 <= y < self.longueur:
            return self.cases[x][y]
        return None

if __name__ == "__main__":
    plateau = Plateau(8, 8, 0.2, True)
    print("Plateau généré :")
    plateau.afficher_plateau()
