from connexion import FlaskApp


def create_app(config_name):
    app = FlaskApp(__name__)
    app.add_api("openapi.yaml")
    app.app.config.from_object(config_name)
    return app
