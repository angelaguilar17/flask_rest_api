
from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')  # lee lo guardado en .env


class developmentConfig(Config):
    DEBUG = True


config = {
    'development': developmentConfig
}
