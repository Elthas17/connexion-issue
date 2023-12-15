# Flask application factory https://hackersandslackers.com/flask-application-factory
import connexion


def create_app(config_name):
    connex_app = connexion.App(__name__)
    connex_app.add_api('openapi.yaml')
    app = connex_app.app  # the Flask app
    app.config.from_object(config_name)

    with app.app_context():

        return app
