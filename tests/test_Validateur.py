import pytest
from app.lib.Validateur import Validateur

@pytest.mark.parametrize("nom, resultat_attendu", [
    ("Jean", True),
    ("Jean-Pierre", True),
    ("Jean Paul", True),

    ("E6", False),
    ("", False),
    ("E"*268, False),
    ("-Jean", False),
    ("Jean-", False),
    ("Jean--Pierre", False),
    ("Jean     Pierre", False),
])
def test_valider_nom_prenom(nom, resultat_attendu):
    assert Validateur.valider_nom_prenom(nom) == resultat_attendu
