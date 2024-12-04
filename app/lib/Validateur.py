class Validateur:
    """
    Classe pour valider les données utilisateur.
    """

    def est_valide(self, données):
        """
        Vérifie si les données fournies sont valides.

        :param données: dict, les données à valider ("nom" et "Prenom")
        :return: bool, True si les données sont valides, False sinon
        """
        if not isinstance(données, dict):
            return False

        # Vérifie que 'nom' est une chaine non vide
        if "nom" not in données or not isinstance(données["nom"], str) or not données["nom"].strip():
            return False

        # Vérifie que 'Prenom' est une chaine non vide
        if "Prenom" not in données or not isinstance(données["Prenom"], str) or not données["Prenom"].strip():
            return False

        return True