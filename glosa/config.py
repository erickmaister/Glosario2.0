import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///glosario.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LANGUAGES = ['es', 'en', 'fr']
    BABEL_DEFAULT_LOCALE = 'es'
    BABEL_TRANSLATION_DIRECTORIES = 'translations'
    JSON_AS_ASCII = False