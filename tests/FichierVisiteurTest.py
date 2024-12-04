import pytest
from app.lib.FichierVisiteur import FichierVisiteur


@pytest.fixture
def fichier_visiteur():
    """Fixture pour instancier un objet FichierVisiteur."""
    return FichierVisiteur()


@pytest.fixture
def fichier_temporaire(tmp_path):
    """Créer un fichier temporaire pour les tests."""
    chemin_fichier = tmp_path / "rapport/test_fichier.txt"
    chemin_fichier.write_text("Ligne initiale\n")
    return chemin_fichier


def test_lire_fichier_existant(fichier_visiteur, fichier_temporaire):
    contenu = fichier_visiteur.lire_fichier(fichier_temporaire)
    assert contenu == "Ligne initiale\n"


def test_lire_fichier_inexistant(fichier_visiteur):
    with pytest.raises(FileNotFoundError):
        fichier_visiteur.lire_fichier("fichier_inexistant.txt")


def test_écrire_dans_fichier(fichier_visiteur, tmp_path):
    chemin_fichier = tmp_path / "test_écriture.txt"
    données = {"nom": "Alice", "Prenom": "test"}
    fichier_visiteur.écrire_données_formulaire(chemin_fichier, données)

    contenu = chemin_fichier.read_text()
    assert contenu.strip() == "Nom: Alice, Prenom: test"


def test_ajout_dans_fichier(fichier_visiteur, fichier_temporaire):
    données = {"nom": "Bob", "âge": 'testiing'}
    fichier_visiteur.écrire_données_formulaire(fichier_temporaire, données)
    contenu = fichier_temporaire.read_text()
    lignes = contenu.strip().split("\n")
    assert len(lignes) == 2
    assert lignes[-1] == "Nom: Bob, Prenom: test"