import re


class Validateur:
    @staticmethod
    def valider_nom_prenom(valeur):

        if not (2 <= len(valeur) <= 60):
            return False

        if not re.match(r"^[a-zA-Z]([- a-zA-Z]{0,58}[a-zA-Z])?$", valeur):
            return False

        if "--" in valeur or "  " in valeur:
            return False

        if valeur.count('-') > 5 or valeur.count(' ') > 5:
            return False

        return True
