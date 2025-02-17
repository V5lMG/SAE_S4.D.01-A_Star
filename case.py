class Case:

    def __init__(self, x, y, type_case):
        self.x = x
        self.y = y
        self.type_case = type_case

    def est_traversable(self):
        """Retourne True si la case peut être traversée (pas un mur)."""
        return self.type_case != 'X'

    def est_depart(self):
        """Retourne True si la case est le point de départ."""
        return self.type_case == "D"

    def est_arrivee(self):
        """Retourne True si la case est le point d'arrivée."""
        return self.type_case == "A"

    def get_type(self):
        """Retourne le type de la case (utilisé pour l'exportation)."""
        return self.type_case

    def __repr__(self):
        """Affichage de la case dans la console ou dans un fichier."""
        return self.type_case
