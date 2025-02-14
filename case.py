class Case:
    def __init__(self, x, y, type_case):
        self.x = x
        self.y = y
        self.type_case = type_case  # 'O', 'X', 'D', 'A'
        self.visited = False  # Pour marquer les cases explorées
        self.parent = None  # Utilisé pour reconstruire le chemin

    def est_traversable(self):
        return self.type_case != 'X'

    def __repr__(self):
        return self.type_case