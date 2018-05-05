import os


class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = "SECRET_KEY"

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    VAR_DIR = ROOT_DIR + '/var/'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
