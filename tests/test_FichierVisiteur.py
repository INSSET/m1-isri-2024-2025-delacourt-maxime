import pytest
from app.lib.FichierVisiteur import FichierVisiteur
import os

CHEMIN_TEST = "test_Fichier.txt"


@pytest.fixture
def setup_fichier():

    if os.path.exists(CHEMIN_TEST):
        os.remove(CHEMIN_TEST)
    yield

    if os.path.exists(CHEMIN_TEST):
        os.remove(CHEMIN_TEST)


def test_ajout_visiteur_valide(setup_fichier):
    fichier = FichierVisiteur(CHEMIN_TEST)
    assert fichier.ajout("Alice", "Bob")
    assert os.path.exists(CHEMIN_TEST)


def test_lecture_visiteurs(setup_fichier):
    fichier = FichierVisiteur(CHEMIN_TEST)
    fichier.ajout("Alice", "Bob")
    fichier.ajout("Eve", "William")
    visiteurs = fichier.tout_lire()
    assert visiteurs == ["Alice,Bob", "Eve,William"]


def test_ajout_visiteur_invalide(setup_fichier):
    fichier = FichierVisiteur(CHEMIN_TEST)
    assert not fichier.ajout("Jean--Pierre", "Jean")
    assert fichier.tout_lire() == []
