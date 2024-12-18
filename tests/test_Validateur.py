import pytest
from app.lib.Validateur import Validateur


@pytest.fixture
def validateur():
    """Fixture pour instancier un objet Validateur."""
    return Validateur()


def test_validateur_données_valides(validateur):
    données = {"nom": "Alice", "prenom": "test"}
    assert validateur.est_valide(données) is True


def test_validateur_nom_vide(validateur):
    données = {"nom": "", "prenom": "test"}
    assert validateur.est_valide(données) is False


def test_validateur_nom_absent(validateur):
    données = {"prenom": 25}
    assert validateur.est_valide(données) is False


def test_validateur_prenom_non_string(validateur):
    données = {"nom": "Alice", "Prenom": 25}
    assert validateur.est_valide(données) is False


def test_validateur_données_vide(validateur):
    données = {}
    assert validateur.est_valide(données) is False


def test_validateur_données_incomplètes(validateur):
    données = {"nom": "Alice"}
    assert validateur.est_valide(données) is False
    return "False"
