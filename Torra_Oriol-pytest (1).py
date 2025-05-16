import pytest
from prova_escrita_05 import llibres_per_categoria, esta_disponible, usuari_te_prestecs, dies_prestec_total

# Prova per la funció llibres_per_categoria
@pytest.mark.parametrize("categoria, esperat", [
    ("novel·la", ["El Quixot", "Crim i Càstig"]),
    ("ciència-ficció", ["1984"]),
    ("fantasia", ["El Senyor dels Anells"]),
])

def test_llibres_per_categoria(categoria, esperat):
    """
    Prova la funció llibres_per_categoria.
    Comprova si es retornen els llibres correctes per a la categoria indicada.
    """
    biblioteca = [
        {"llibre": "El Quixot", "categoria": "novel·la"},
        {"llibre": "1984", "categoria": "ciència-ficció"},
        {"llibre": "El Senyor dels Anells", "categoria": "fantasia"},
        {"llibre": "Crim i Càstig", "categoria": "novel·la"}
    ]
    assert llibres_per_categoria(biblioteca, categoria) == esperat


# Prova per la funció esta_disponible
@pytest.mark.parametrize("llibre, esperat", [
    ("El Senyor dels Anells", False),
    ("1984", True),
    ("El Quixot", True),
])

def test_esta_disponible(llibre, esperat):
    """
    Prova la funció esta_disponible.
    Comprova si el llibre està disponible per al préstec.
    """
    biblioteca = [
        {"llibre": "El Quixot", "prestecs": [{"usuari": "Joan", "retornat": True}]},
        {"llibre": "1984", "prestecs": [{"usuari": "Pere", "retornat": True}]},
        {"llibre": "El Senyor dels Anells", "prestecs": [{"usuari": "Maria", "retornat": False}]}
    ]
    assert esta_disponible(biblioteca, llibre) == esperat


# Prova per la funció usuari_te_prestecs
@pytest.mark.parametrize("usuari, esperat", [
    ("Pere", True),
    ("Anna", False),
    ("Marta", False),
])

def test_usuari_te_prestecs(usuari, esperat):
    """
    Prova la funció usuari_te_prestecs.
    Comprova si l'usuari té llibres sense retornar.
    """
    biblioteca = [
        {"llibre": "El Quixot", "prestecs": [{"usuari": "Joan", "retornat": True}]},
        {"llibre": "1984", "prestecs": [{"usuari": "Pere", "retornat": False}]},
        {"llibre": "El Senyor dels Anells", "prestecs": [{"usuari": "Pere", "retornat": False}]}
    ]
    assert usuari_te_prestecs(biblioteca, usuari) == esperat


# Prova per la funció dies_prestec_total
@pytest.mark.parametrize("llibre, esperat", [
    ("El Senyor dels Anells", 67),
    ("1984", 53),
    ("El Quixot", 47),
])

def test_dies_prestec_total(llibre, esperat):
    """
    Prova la funció dies_prestec_total.
    Comprova si el nombre de dies total per un llibre és correcte.
    """
    biblioteca = [
        {"llibre": "El Quixot", "prestecs": [{"usuari": "Joan", "dies": 15}, {"usuari": "Maria", "dies": 20}]},
        {"llibre": "1984", "prestecs": [{"usuari": "Pere", "dies": 10}, {"usuari": "Anna", "dies": 25}]},
        {"llibre": "El Senyor dels Anells", "prestecs": [{"usuari": "Maria", "dies": 30}, {"usuari": "Joan", "dies": 22}]}
    ]
    assert dies_prestec_total(biblioteca, llibre) == esperat
