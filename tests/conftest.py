import pytest
from app.lib.Validateur import Validateur
from app.lib.FichierVisiteur import FichierVisiteur


@pytest.fixture
def validateur():
    """
    Fixture pour fournir une instance de Validateur pour les tests.
    """
    return Validateur()


@pytest.fixture
def fichier_visiteur():
    """
    Fixture pour fournir une instance de FichierVisiteur pour les tests.
    """
    return FichierVisiteur()


@pytest.fixture
def fichier_temporaire(tmp_path):
    """
    Fixture pour créer un fichier temporaire pour les tests de FichierVisiteur.
    Retourne le chemin du fichier temporaire.
    """
    chemin_fichier = tmp_path / "rapport/test_fichier.txt"
    chemin_fichier.write_text("Ligne initiale\n")
    return chemin_fichier