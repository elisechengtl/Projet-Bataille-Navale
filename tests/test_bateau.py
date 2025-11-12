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
