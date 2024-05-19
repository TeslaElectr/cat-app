# DB_URL = "postgresql+psycopg://user:password@localhost:5432/catdb"
# SECRET_KEY = "72970e69eeee063cd7c706736d861759e5e395751fae80dc89a71a5991b3115c"

from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg://user:password@localhost:5432/catdb",
)


class Config:
    TESTING = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SECRET_KEY = "" 
    

class DevelopmentConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "b65a50a2fdb48bbae1352af577ac27765ff65167631267b3e1a3be302917aa7c"