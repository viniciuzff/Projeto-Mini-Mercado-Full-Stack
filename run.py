import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from flask import Flask
from config.data_base import init_db
from routes import init_routes

def create_app():
    """
    Função que cria e configura a aplicação Flask.
    """
    app = Flask(__name__)

    init_db(app)

    init_routes(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
