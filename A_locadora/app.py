import os

from flask import Flask

from controllers import locadora_bp
from dados_iniciais import popular_dados
from models import db


def criar_app():
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="views/static"
    )

    pasta = os.path.abspath(os.path.dirname(__file__))

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///" + os.path.join(pasta, "locadora.db")
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(locadora_bp)

    @app.route("/")
    def home():
        return """
        <h1>Locadora</h1>
        <a href="/locadora/">Acessar sistema da locadora</a>
        """

    with app.app_context():
        db.create_all()

        try:
            popular_dados()
        except:
            pass

    return app


app = criar_app()

if __name__ == "__main__":
    app.run(debug=True)