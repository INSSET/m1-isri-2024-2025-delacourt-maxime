from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)
# Chemin du fichier où les données des contacts sont enregistrées
FILE_PATH = "form_data.txt"
@app.route('/')
def index():
    """Page d'accueil."""
    return render_template('index.html')\
@app.route('/form', methods=['GET', 'POST'])
def form():
    """Page de formulaire pour ajouter des contacts."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # Enregistrer les données dans un fichier
        with open(FILE_PATH, 'a') as f:
            f.write(f"Nom: {name}, Email: {email}\n")

        # Rediriger vers la liste des contacts après soumission
        return redirect(url_for('view_contacts'))

    return render_template('form.html')
@app.route('/contacts')
def view_contacts():
    """Page pour afficher tous les contacts."""
    contacts = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            for line in f:
                name, email = line.strip().split(", ")
                contacts.append({
                    "name": name.split(": ")[1],
                    "email": email.split(": ")[1],
                })
    return render_template('contacts.html', contacts=contacts)
if __name__ == '__main__':
    app.run(debug=True)