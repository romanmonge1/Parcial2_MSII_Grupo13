from funciones.dividir_monge import dividir_monge

def test_dividir_monge_normal():
    assert dividir_monge(10, 2) == 5

def test_dividir_monge_cero():
    assert dividir_monge(5, 0) is None