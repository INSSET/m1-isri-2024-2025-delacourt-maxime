from app.lib.Validateur import Validateur

class FichierVisiteur:

    def __init__(self, chemin_fichier):
        self.chemin_fichier = chemin_fichier

    def ajout(self, nom, prenom):

        if Validateur.valider_nom_prenom(nom) and Validateur.valider_nom_prenom(prenom):
            with open(self.chemin_fichier, 'a', encoding='utf-8') as fichier:
                fichier.write(f"{nom},{prenom}\n")
            return True
        return False

    def tout_lire(self):

        try:
            with open(self.chemin_fichier, 'r', encoding='utf-8') as fichier:
                return [ligne.strip() for ligne in fichier.readlines()]
        except FileNotFoundError:
            return []