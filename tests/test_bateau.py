from bateau import Bateau

def test_bateau_valeurs_explicites():
    b = Bateau(2, 7, 5, True)
    assert b.ligne == 2
    assert b.colonne == 7
    assert b.longueur == 5
    assert b.vertical is True

def test_bateau_valeurs_par_defaut():
    b = Bateau(0, 0)
    assert b.ligne == 0
    assert b.colonne == 0
    assert b.longueur == 1  
    assert b.vertical is False  

def test_positions_horizontal():
    b = Bateau(2, 3, longueur=3)
    assert b.positions == [(2, 3), (2, 4), (2, 5)]

def test_positions_vertical():
    b = Bateau(2, 3, longueur=3, vertical=True)
    assert b.positions == [(2, 3), (3, 3), (4, 3)]

def test_coule_true():
    g = Grille(3, 3)
    b = Bateau(1, 0, longueur=2, vertical=False)
    g.ajoute(b)
    g.tirer(1, 0)
    g.tirer(1, 1)
    assert b.coulé(g) is True

def test_coule_false():
    g = Grille(3, 3)
    b = Bateau(1, 0, longueur=3, vertical=False)
    g.ajoute(b)
    g.tirer(1, 0)
    g.tirer(1, 1)
    assert b.coulé(g) is False
