import pytest
from cine import Pelicula

def test_vender_entradas_suficientes():
    pelicula = Pelicula("Test Movie", 100, 10)
    resultado = pelicula.vender_entradas(10) 
    assert resultado == "Has comprado 10 entradas para Test Movie. Total: $100"
    assert pelicula.asientos_disponibles == 90 

def test_vender_entradas_insuficientes():
    pelicula = Pelicula("Test Movie", 50, 10)
    resultado = pelicula.vender_entradas(60) 
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 50 asientos."
    assert pelicula.asientos_disponibles == 50

def test_vender_cero_entradas():
    pelicula = Pelicula("Test Movie", 100, 10)
    resultado = pelicula.vender_entradas(0) 
    assert resultado == "Has comprado 0 entradas para Test Movie. Total: $0"
    assert pelicula.asientos_disponibles == 100

def test_vender_entradas_negativas():
    pelicula = Pelicula("Test Movie", 100, 10)
    with pytest.raises(ValueError):
        pelicula.vender_entradas(-5)
