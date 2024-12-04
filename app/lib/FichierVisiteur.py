class FichierVisiteur:
    """
    Classe pour gérer les fichiers (lecture et écriture).
    """

    def lire_fichier(self, chemin):
        """
        Lit le contenu d'un fichier.

        :param chemin: str, le chemin du fichier à lire
        :return: str, le contenu du fichier
        """
        try:
            with open(chemin, 'r', encoding='utf-8') as fichier:
                return fichier.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Le fichier '{chemin}' n'existe pas.")

    def écrire_données_formulaire(self, chemin, données):
        """
        Ajoute les données d'un formulaire dans un fichier.

        :param chemin: str, le chemin du fichier
        :param données: dict, les données à enregistrer
        """
        with open(chemin, 'a', encoding='utf-8') as fichier:
            fichier.write(f"Nom: {données['nom']}, Prenom: {données['Prenom']}\n")