from flask import Flask, render_template, request
from .lib.Validateur import Validateur
from .lib.FichierVisiteur import FichierVisiteur
import os

app = Flask(__name__)

# Chemin du fichier où les données des contacts sont enregistrées
FILE_PATH = "../../form_data.txt"


@app.route('/')
def index():
    """Page d'accueil."""
    return render_template('index.html')


@app.route('/contacts')
def view_contacts():
    """Page pour afficher tous les contacts."""
    contacts = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            for line in f:
                nom, prenom = line.strip().split(", ")
                contacts.append({
                    "nom": nom.split(": ")[1],
                    "prenom": prenom.split(": ")[1],
                })
    return render_template('contacts.html', contacts=contacts)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        données = {
            "nom": request.form.get("nom"),
            "Prenom": request.form.get("Prenom")
        }

        # Valider les données
        if Validateur.est_valide(données):
            # Enregistrer dans un fichier
            FichierVisiteur.écrire_données_formulaire("form_data.txt", données)
            message = "Les données ont été enregistrées avec succès."
        else:
            message = "Les données sont invalides. Veuillez réessayer."

        return render_template("contact.html", message=message)

    return render_template("contact.html")


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
