from flask import Flask
from app.views import index  # Chemin complet du package contenant views.py

app = Flask(__name__)

app.add_url_rule('/', view_func=index)

if __name__ == '__main__':
    app.run(debug=True)
