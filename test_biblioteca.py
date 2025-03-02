import pytest
from biblioteca import Libro, Biblioteca

def test_libro_atributos():
    libro = Libro("El principito", "Antoine de Saint-Exupéry", 1943)
    assert libro.titulo == "El principito"
    assert libro.autor == "Antoine de Saint-Exupéry"
    assert libro.anio == 1943
    assert libro.prestado is False

def test_libro_str():
    libro = Libro("1984", "George Orwell", 1949)
    assert str(libro) == "1984 de George Orwell (1949) - disponible"
    libro.prestado = True
    assert str(libro) == "1984 de George Orwell (1949) - prestado"

def test_agregar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    biblioteca.agregar_libro(libro)
    assert len(biblioteca.libros) == 1
    assert biblioteca.libros[0].titulo == "Cien años de soledad"

def test_eliminar_libro_existente():
    biblioteca = Biblioteca()
    libro = Libro("Don Quijote", "Miguel de Cervantes", 1605)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("Don Quijote")
    assert len(biblioteca.libros) == 0

def test_eliminar_libro_inexistente():
    biblioteca = Biblioteca()
    biblioteca.eliminar_libro("Libro Fantasma")
    assert len(biblioteca.libros) == 0

def test_buscar_libro_existente():
    biblioteca = Biblioteca()
    libro = Libro("La Odisea", "Homero", -800)
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.buscar_libro("La Odisea")
    assert resultado is not None
    assert resultado.titulo == "La Odisea"

def test_buscar_libro_inexistente():
    biblioteca = Biblioteca()
    resultado = biblioteca.buscar_libro("Libro Desconocido")
    assert resultado is None

def test_listar_libros():
    biblioteca = Biblioteca()
    libro1 = Libro("El Hobbit", "J.R.R. Tolkien", 1937)
    libro2 = Libro("Drácula", "Bram Stoker", 1897)
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    lista = biblioteca.listar_libros()
    assert len(lista) == 2
    assert "El Hobbit" in lista[0]
    assert "Drácula" in lista[1]

def test_prestar_libro_disponible():
    biblioteca = Biblioteca()
    libro = Libro("Fahrenheit 451", "Ray Bradbury", 1953)
    biblioteca.agregar_libro(libro)
    mensaje = biblioteca.prestar_libro("Fahrenheit 451")
    assert mensaje == "Has pedido prestado el libro 'Fahrenheit 451'."
    assert libro.prestado is True

def test_prestar_libro_prestado():
    biblioteca = Biblioteca()
    libro = Libro("Moby Dick", "Herman Melville", 1851)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("Moby Dick")
    mensaje = biblioteca.prestar_libro("Moby Dick")
    assert mensaje == "El libro 'Moby Dick' ya está prestado."

def test_prestar_libro_inexistente():
    biblioteca = Biblioteca()
    mensaje = biblioteca.prestar_libro("Libro No Registrado")
    assert mensaje == "El libro 'Libro No Registrado' no se encuentra en la biblioteca."

def test_devolver_libro_prestado():
    biblioteca = Biblioteca()
    libro = Libro("Crimen y Castigo", "Fiódor Dostoievski", 1866)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("Crimen y Castigo")
    mensaje = biblioteca.devolver_libro("Crimen y Castigo")
    assert mensaje == "Has devuelto el libro 'Crimen y Castigo'."
    assert libro.prestado is False

def test_devolver_libro_no_prestado():
    biblioteca = Biblioteca()
    libro = Libro("Los miserables", "Victor Hugo", 1862)
    biblioteca.agregar_libro(libro)
    mensaje = biblioteca.devolver_libro("Los miserables")
    assert mensaje == "El libro 'Los miserables' no estaba prestado."

def test_devolver_libro_inexistente():
    biblioteca = Biblioteca()
    mensaje = biblioteca.devolver_libro("Libro Inexistente")
    assert mensaje == "El libro 'Libro Inexistente' no se encuentra en la biblioteca."
