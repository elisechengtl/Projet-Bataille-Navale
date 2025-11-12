class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    @property
    def positions(self):
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        else:
            return [(self.ligne, self.colonne + i) for i in range(self.longueur)]

    def coulé(self, grille):
        for (l, c) in self.positions:
            index = l * grille.nombre_colonnes + c
            if grille.matrice[index] != 'x':
                return False
        return True
