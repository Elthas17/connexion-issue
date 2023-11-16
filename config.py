import os



class Config:
    """Base config vars."""


    # API
    CORS_HEADERS = 'Content-Type'
    ENV = 'development'

class DevelopmentConfig(Config):

    # flask
    DEBUG = True
    TESTING = True
    FLASK_DEBUG = True

    # sqlalchemy
    SQLALCHEMY_ECHO = True

class StagingConfig(Config):

    # flask
    DEBUG = True
    TESTING = True
    FLASK_DEBUG = True


class ProductionConfig(Config):
    # flask
    DEBUG = False
    TESTING = False
    FLASK_DEBUG = False










