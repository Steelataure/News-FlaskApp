from flask import Flask
app = Flask(__name__)

# Les routes pourront être définies dans le fichier views.py
from views import index
app.add_url_rule('/', view_func=index)
# Ajoute d'autres routes ici si nécessaire

if __name__ == '__main__':
    app.run(debug=True)
