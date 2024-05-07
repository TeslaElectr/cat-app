from flask import Flask

from views import root_app
from views import cat_app
from models import db

from flask_migrate import Migrate

import config

app = Flask(__name__)

app.register_blueprint(root_app)
app.register_blueprint(cat_app)

app.config.update(
    SQLALCHEMY_DATABASE_URI=config.DB_URL,
    SECRET_KEY=config.SECRET_KEY,
)

db.init_app(app=app)
migrate = Migrate(app=app, db=db)







