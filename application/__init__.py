# Flask application factory https://hackersandslackers.com/flask-application-factory
import connexion


def create_app(config_name):
    app = connexion.FlaskApp(__name__)
    app.add_api("openapi.yaml")
    app.config.from_object(config_name)

    with app.app_context():

        return app
