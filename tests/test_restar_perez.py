from funciones.restar_perez import restar_perez

def test_restar_perez_positivos():
    assert restar_perez(10, 4) == 6

def test_restar_perez_negativos():
    assert restar_perez(5, 10) == -5
