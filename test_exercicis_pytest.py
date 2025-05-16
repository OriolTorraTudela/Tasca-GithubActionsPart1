# Importem les funcions del fitxer original
from Solucio_prova_escrita_5 import llibres_per_categoria, esta_disponible, usuari_te_prestecs, dies_prestec_total
import pytest

biblioteca = [
    {
        "llibre": "El Quixot",
        "autor": "Cervantes",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Joan", "dies": 15, "retornat": True},
            {"usuari": "Maria", "dies": 20, "retornat": False},
            {"usuari": "Pere", "dies": 12, "retornat": True}
        ]
    },
    {
        "llibre": "1984",
        "autor": "Orwell",
        "categoria": "ciència-ficció",
        "prestecs": [
            {"usuari": "Pere", "dies": 10, "retornat": True},
            {"usuari": "Anna", "dies": 25, "retornat": True},
            {"usuari": "Marta", "dies": 18, "retornat": False}
        ]
    }
]

@pytest.mark.parametrize("categoria, resultat_esperat", [
    ("novel·la", ["El Quixot"]),
    ("ciència-ficció", ["1984"]),
    ("fantasia", []),
])
def test_llibres_per_categoria(categoria, resultat_esperat):
    """
    Prova que verifica si es retornen els llibres correctes segons la categoria especificada.
    """
    assert llibres_per_categoria(biblioteca, categoria) == resultat_esperat

@pytest.mark.parametrize("llibre, resultat_esperat", [
    ("El Quixot", False),  # Té préstecs no retornats
    ("1984", False),       # També té préstecs no retornats
    ("Inexistent", True),  # Llibre que no existeix a la base de dades
])
def test_esta_disponible(llibre, resultat_esperat):
    """
    Prova que verifica si un llibre està disponible per préstec.
    """
    assert esta_disponible(biblioteca, llibre) == resultat_esperat

@pytest.mark.parametrize("usuari, resultat_esperat", [
    ("Joan", False),  # Ha retornat tots els seus préstecs
    ("Maria", True),  # Té un préstec no retornat
    ("Anna", False),  # Ha retornat tots els seus préstecs
])
def test_usuari_te_prestecs(usuari, resultat_esperat):
    """
    Prova que comprova si un usuari té préstecs pendents.
    """
    assert usuari_te_prestecs(biblioteca, usuari) == resultat_esperat

@pytest.mark.parametrize("llibre, resultat_esperat", [
    ("El Quixot", 47),  # 15 + 20 + 12
    ("1984", 53),       # 10 + 25 + 18
    ("Inexistent", 0),  # Llibre inexistent
])
def test_dies_prestec_total(llibre, resultat_esperat):
    """
    Prova que comprova la suma total de dies d'un llibre prestat.
    """
    assert dies_prestec_total(biblioteca, llibre) == resultat_esperat
