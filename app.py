from flask import Flask, request, jsonify
import os

app = Flask(__name__)
    
   # Chemin du fichier où les données seront enregistrées
FILE_PATH = "form_data.txt"
    
@app.route('/')
def form():
    return '''
    <form method="POST" action="/submit">
        <label for="name">Nom :</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email :</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Envoyer</button>
    </form>
    '''
    
@app.route('/submit', methods=['POST'])
def submit_form():
    # Récupération des données du formulaire
    name = request.form.get('name')
    email = request.form.get('email')

    # Création ou ajout au fichier
    with open(FILE_PATH, 'a') as f:
      f.write(f"Nom: {name}, Email: {email}\n")

    return jsonify({"message": "Données enregistrées avec succès !"})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/contact')
def view_contacts():
    # Lecture des données du fichier
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            data = f.readlines()
    else:
        data = []

    # Génération de la table HTML
    table_rows = ""
    for line in data:
        name, email = line.strip().split(", ")
        name = name.split(": ")[1]  # Extrait le nom
        email = email.split(": ")[1]  # Extrait l'email
        table_rows += f"<tr><td>{name}</td><td>{email}</td></tr>"

    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Liste des contacts</title>
        <style>
            table {{
                border-collapse: collapse;
                width: 50%;
                margin: 20px auto;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f4f4f4;
            }}
        </style>
    </head>
    <body>
        <h1 style="text-align: center;">Liste des Contacts</h1>
        <table>
            <thead>
                <tr>
                    <th>Nom</th>
                    <th>Email</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </body>
    </html>
    """
